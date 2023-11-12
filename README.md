# al-folio-pelican

Build an academic website with the stylish look of the popular [al-folio](https://github.com/alshedivat/al-folio) 
template, but using Python, not Ruby. This is a port of the al-folio template for the Pelican static site generator and the
Jinja templating engine. All credit to the original authors of this fantastic template!

Want to see what the result looks like? It's almost identical to al-folio, and you can see an active version on
[my personal website](https://vivek-bharadwaj.com).

Building this template has been tested (at a cursory level) on Mac OSX, Windows, and Linux.

### Getting started locally
1. Click "Use this template" at the top of the Github page to create a repository with
   a fresh copy of the template and a blank history.
2. Clone the new repository to your computer and `cd` into it.
```
git clone <repo_name>
cd <repo_name>
```
3. Install dependencies via `pip`. For interactive local development, also install `invoke`:
```
pip install -r requirements.txt
pip install invoke
```
4. Build the website:
```
python -m invoke livereload
```
This command will compile the site and open a browser window that dynamically updates as you edit
the content of your website.
5. Edit the content of your website. You can change `config.yml`, the contents of each page in the `pages` 
directory, blog posts in the `articles` directory, and add your list of publications in
`pages/publications.bib`.

#### Debugging
Got a cryptic error message? Try running
```
python -m pelican --debug
```
which will build the website and prints log messages and a detailed stack trace for errors.

### Deploying to Github Pages
Coming soon...





