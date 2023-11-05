from jinja2 import Environment, FileSystemLoader

def render_main_scss(SITE):
    env = Environment(loader=FileSystemLoader(searchpath='al_folio_theme/templated_assets/'))

    # Load the template
    template = env.get_template('main.scss')

    # Define the data you want to use in the template
    data = {
        'SITE': SITE 
    }

    # Render the template with the data
    output = template.render(data)

    # Print or save the compiled output
    output_file_path = 'al_folio_theme/static/css/main.scss'
    with open(output_file_path, 'w') as output_file:
        output_file.write(output) 

