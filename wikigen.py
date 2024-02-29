import os
import markdown2
from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader
import re

app = Flask(__name__)
template_env = Environment(loader=FileSystemLoader('templates'))

# Function to convert markdown to HTML using markdown2 library
def convert_markdown_to_html(content):
    return markdown2.markdown(content)

# Function to generate HTML using Jinja2 template
def generate_html(template, **kwargs):
    template = template_env.get_template(template)
    return template.render(**kwargs)

# Function to generate static HTML files
def generate_static_html(source_path, output_path):
    for filename in os.listdir(source_path):
        if filename.endswith(".md"):
            with open(os.path.join(source_path, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                html_content = convert_markdown_to_html(content)
                output_filename = os.path.splitext(filename)[0] + ".html"
                output_file_path = os.path.join(output_path, output_filename)
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(html_content)

# Function to build the site
def build_site(source_path, output_path):
    generate_static_html(source_path, output_path)

# Function to run the development server
def run_dev_server():
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/<filename>')
    def page(filename):
        filename = os.path.join(output_path, filename)
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                # Process links to ensure they point to the correct HTML file
                content = process_links(content)
                return render_template('page_template.html', content=content)
        else:
            return "Page not found", 404

    print("Starting the development server...")
    app.run(debug=True)

def process_links(content):
    # Modify links in the content to point to HTML files
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'[\1](\2.html)', content)

if __name__ == "__main__":
    source_path = "content"
    output_path = "output"

    # Build the site
    build_site(source_path, output_path)

    # Run the development server
    run_dev_server()
    
