import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def replace_inside_html(to_replace_with: str) -> str:
    """ Placeholder function for future use """
    newdata = ""
    with open('animals_template.html', 'r') as file:
        newdata = file.read().replace('__REPLACE_ANIMALS_INFO__', to_replace_with)

    return newdata

def create_new_html_file(file_name: str, content: str):
    """ Creates a new HTML file with the given content """
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File {file_name} created successfully.")

def populate_html_from_animal_data(animals):
    """ Populates animal data with default values if not present """
    output = ''  # define an empty string
    for animal in animals:
        # append information to each string
        output += '<li class="cards__item">'
        output += f"Name: {animal['name']}<br/>\n"
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        output += f"Location: {animal['locations']}<br/>\n"
        output += f"Type: {animal['characteristics'].get('type', "")}<br/>\n"
        output += '</li>'

    new_html = replace_inside_html(output)
    create_new_html_file('animals.html', new_html)


if __name__ == "__main__":
    """ Main function to run the script """
    print("Loading animal data...")
    animals_data = load_data('animals_data.json')
    populate_html_from_animal_data(animals_data)
    print("Animal data loaded successfully.")