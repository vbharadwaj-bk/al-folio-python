from __future__ import annotations

from textwrap import dedent
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.serializers import _escape_attrib_html
import re

from jinja2 import Environment, FileSystemLoader

class TemplateBlockExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            'filters': ['filters-', 'JINJA filters to include in environment. Default: None.']
        }
        """ Default configuration options. """
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        """ Add `FencedBlockPreprocessor` to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.register(TemplateBlockPreprocessor(md, self.getConfigs()), 'template_block', 175)


class TemplateBlockPreprocessor(Preprocessor):
    """ 
    Find and extract template blocks.
    This extension renders any template block it finds 
    using Jinja and outputs an error if template
    rendering fails. 
    """

    TEMPLATE_BLOCK_RE = re.compile(
        dedent(r'''
            (?P<fence>^!TEMPLATE!)[ ]*
            \n                                       # newline (end of opening fence)
            (?P<template>.*?)(?<=\n)                 # the template 
            (?P=fence)[ ]*$                          # closing fence
        '''),
        re.MULTILINE | re.DOTALL | re.VERBOSE
    )

    def __init__(self, md, config):
        super().__init__(md)
        self.config = config
        filters = self.config.get('filters', None)
        self.env = Environment(loader=FileSystemLoader(searchpath='al_folio_theme/templates/_includes/'))

        for key in filters:
            self.env.filters[key] = filters[key]

        self.figure_import = '{% from "figure.html" import figure with context %}\n'


    def run(self, lines):
        """ Match and store Template Blocks in the `HtmlStash`. """

        text = "\n".join(lines)
        while 1:
            m = self.TEMPLATE_BLOCK_RE.search(text)
            if m:
                template_input = m.group('template')
                if 'figure(' in template_input:
                    template_input = self.figure_import + template_input
                template_rendered = None
                # Load the template
                try:
                    template = self.env.from_string(template_input)  
                    data = {} 
                    template_rendered = template.render(data)
                except Exception as e:
                    template_rendered = f'<p>JINJA TEMPLATE ERROR: {e}</p>'
                text = f'{text[:m.start()]}\n{template_rendered}\n{text[m.end():]}'

            else:
                break
        return text.split("\n")
