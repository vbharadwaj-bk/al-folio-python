import pybtex
import pybtex.database
from markdown import Markdown

def parse_bibliography(filename, output_key, SITE):
    data = pybtex.database.parse_file(filename)
    entries = []

    non_link_fields = [ 
        "abbr",
        "abstract",
        "journal",
        "booktitle",
        "school",
        "month",
        "year",
        "note",
        "bibtex_show",
        "eprint",
        "doi",
        "altmetric",
        "pmid",
        "isbn",
        "dimensions"
    ]

    button_fields = [
        "arxiv",
        "html",
        "pdf",
        "supp",
        "blog",
        "code",
        "poster",
        "slides",
        "website",
    ]

    # Fields to remove from final bibtex representation
    fields_to_remove = ["abbr", "bibtex_show", "arxiv", "preview", "selected"] + button_fields

    for key in data.entries:
        d = data.entries[key]

        entry = {}
        entry["key"] = key
        entry["title"] = d.fields['title']
        entry["type"] = d.type
        entry["author_array"] = []

        if "preview" in d.fields:
            link = d.fields["preview"]
            entry["preview"] = {"link": link}
            entry["preview"]["relative"] = "://" not in link

        for author in d.persons['author']:
            entry_author = {}
            entry_author["first"] = ' '.join(author.first_names)
            entry_author["last"] = ' '.join(author.last_names)
            entry["author_array"].append(entry_author)

            if entry_author["first"] in SITE["first_name"] and \
                entry_author["last"] in SITE["last_name"]:
                entry_author["is_self"] = True

        for field in non_link_fields:
            if field in d.fields:
                entry[field] = d.fields[field]

        entry["selected"] = False
        if "selected" in d.fields and d.fields["selected"] == "true":
            entry["selected"] = True

        entry["button_fields"] = {}

        for field in button_fields: 
            if field in d.fields:
                link = d.fields[field]
                entry["button_fields"][field] = {"link": link}
                entry["button_fields"][field]["relative"] = "://" not in link

        for field in fields_to_remove:
            if field in d.fields:
                d.fields.pop(field)

        md = Markdown(extensions=['extra', 'codehilite'])
        md_code = "```\n:::bibtex\n" + d.to_string("bibtex") + "\n```"
        entry["bibtex"] = md.convert(md_code)
        entries.append(entry)

    SITE[output_key] = entries 