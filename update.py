import json

json_file_path = 'css_properties.json'
readme_format_path = 'README-format.md'
readme_output_path = 'README.md'

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def read_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def sanitize_text(text, isText):
    """Replace '|' with '/', '\n' with ' ' to avoid issues in table formatting."""
    if isText:
        if '<' in text:
            text = text.replace('<', '&lt;')
        if '>' in text:
            text = text.replace('>', '&gt;')
        text = text.replace("\n\t", " ").replace("  ", " ")
    return text.replace('|', '\\|').replace('\n', ' ')


def generate_table(properties):
    table_header = "| Category       | Property Name | Brief Description         | Learn More Link                 |\n"
    table_header += "|----------------|---------------|---------------------------|---------------------------------|\n"

    table_rows = ""
    for letter, entries in properties.items():
        for entry in entries:
            category = sanitize_text(entry['category'], True)
            name = sanitize_text(entry['name'], False)
            brief = sanitize_text(entry['brief'], True)
            link = entry['link']
            table_rows += f"| `{category}` | `{name}` | {brief} | [Learn More]({link}) |\n"

    return table_header + table_rows

def write_readme(output_path, template, table):
    readme_content = template.replace("{table}", table)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(readme_content)

def main():
    properties = read_json(json_file_path)
    template = read_template(readme_format_path)
    table = generate_table(properties)
    write_readme(readme_output_path, template, table)
    print(f"README.md has been successfully updated!")

if __name__ == "__main__":
    main()
