from pelican.generators import Generator
from pelican.contents import Content
import logging
from pelican import signals
import os, yaml
from markdown import Markdown
from operator import itemgetter

log = logging.getLogger(__name__)

class ListItem(Content):
    mandatory_properties = None 
    allowed_statuses = ('published', 'hidden', 'draft')
    default_status = 'published'
    default_template = None 

    def _expand_settings(self, key):
        klass = 'draft_news' if self.status == 'draft' else None
        return super()._expand_settings(key, klass)

def content_pass(gen, md, input, strip_p_tags=False):
    md_data = md.reset().convert(input)
    converted_content = ListItem(content=md_data,
                        metadata=None, 
                        settings=gen.settings,
                        source_path=None, 
                        context=gen.context)

    result = converted_content.content 
    if strip_p_tags:
        result = result.replace("<p>", "").replace("</p>", "") 

    return result 

class ALFolioGenerator(Generator):
    '''
    Custom generator for data needed by the al-folio theme.
    Reads YAML files, runs URL replacement / Markdown for
    specified dictionary members.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md = Markdown(extensions=["extra"])

    def generate_context(self):
        pass


def process_content_fields(page_generator):
    md = Markdown(extensions=["extra"])
    gen = page_generator

    # Load teaching
    key = "pages/teaching.md"
    if key in gen.context["generated_content"]:
        article = gen.context["generated_content"][key]
        fields_to_process = [('title', True), ('content', False)]

        if "courses" in article.metadata:
            try:
                for element in article.metadata["courses"]:
                    for field, strip_p_tags in fields_to_process:
                        element[field] = content_pass(gen, md, element[field], strip_p_tags=strip_p_tags)
                gen.context["teaching"] = article.metadata["courses"]
            except Exception as e:
                log.error(f"Error loading teaching! {e}") 

    # Load news
    key = "pages/news.md"
    if key in gen.context["generated_content"]:
        article = gen.context["generated_content"][key]
        fields_to_process = [('content', False)]

        if "entries" in article.metadata:
            try:
                for element in article.metadata["entries"]:
                    for field, strip_p_tags in fields_to_process:
                        element[field] = content_pass(gen, md, element[field], strip_p_tags=strip_p_tags)
                gen.context["news"] = article.metadata["entries"]
            except Exception as e:
                log.error(f"Error loading news! {e}")

    dropdowns = [] 
    if "dropdowns" in gen.context["SITE"]: 
        dropdowns = gen.context["SITE"]["dropdowns"]
        for el in dropdowns:
            for i, child in enumerate(el["children"]):
                if child != "divider":
                    str_to_process = child + '{: class="dropdown-item" }'
                    el["children"][i] = content_pass(gen, md, str_to_process, strip_p_tags=True)


    # Sort pages for the navigation bar
    pages = gen.context["pages"]

    sorted_pages = []
    for page in pages:
        if "nav_order" in page.metadata:
            nav_order = page.metadata["nav_order"]
        else:
            nav_order = -1

        if "nav" in page.metadata and page.metadata["nav"]:
            sorted_pages.append((nav_order, "page", page))

    for d in dropdowns:
        sorted_pages.append((d["nav_order"], "dropdown", d))

    sorted_pages = sorted(sorted_pages, key=itemgetter(0))
    gen.context["nav_sorted_pages"] = sorted_pages


def get_generators(pelican_object):
    return ALFolioGenerator

def register():
    signals.get_generators.connect(get_generators)
    signals.page_generator_finalized.connect(process_content_fields)
