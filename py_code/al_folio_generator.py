from pelican.generators import Generator
from pelican.contents import Content
import logging
from pelican import signals
import os, yaml
from markdown import Markdown 

log = logging.getLogger(__name__)

class ListItem(Content):
    mandatory_properties = None 
    allowed_statuses = ('published', 'hidden', 'draft')
    default_status = 'published'
    default_template = None 

    def _expand_settings(self, key):
        klass = 'draft_news' if self.status == 'draft' else None
        return super()._expand_settings(key, klass)


class ALFolioGenerator(Generator):
    '''
    Custom generator for data needed by the al-folio theme.
    Reads YAML files, runs URL replacement / Markdown for
    specified dictionary members.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md = Markdown() 

    def content_pass(self, input, strip_p_tags=False):
        md_data = self.md.reset().convert(input)
        converted_content = ListItem(content=md_data,
                            metadata=None, 
                            settings=self.settings,
                            source_path=None, 
                            context=self.context)

        result = converted_content.content 
        if strip_p_tags:
            result = result.replace("<p>", "").replace("</p>", "") 

        return result 

    def generate_context(self):
        news = teaching = None

        if os.path.exists('content/pages/news.yml'):
            try:
                with open(f"content/pages/news.yml", "rb") as stream:
                    news = yaml.safe_load(stream)
                    for element in news:
                        element["content"] = self.content_pass(element["content"])
            except Exception as e:
                log.error(f"Error loading news! {e}") 
        self.context["news"] = news


        fields_to_process = [('title', True), ('content', False)]
        if os.path.exists('content/data/teaching.yml'):
            try:
                with open(f"content/data/teaching.yml", "rb") as stream:
                    teaching = yaml.safe_load(stream)
                    for element in teaching:
                        for field, strip_p_tags in fields_to_process:
                            element[field] = self.content_pass(element[field], strip_p_tags=strip_p_tags)
            except Exception as e:
                log.error(f"Error loading teaching! {e}") 
        self.context["teaching"] = teaching 


def get_generators(pelican_object):
    return ALFolioGenerator

def register():
    signals.get_generators.connect(get_generators)