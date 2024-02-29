t# Function to run the development server
def run_dev_server():
    app.run(debug=True)

if __name__ == "__main__":
    source_path = "content"
    output_path = "output"

    # Build the site
    build_site(source_path, output_path)

    # Run the development server
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
                return render_template('page_template.html', content=content)
        else:
            return "Page not found", 404

    print("Starting the development server...")
    app.run(debug=True)

if __name__ == "__main__":
    source_path = "content"
    output_path = "output"

    # Build the site
    build_site(source_path, output_path)

    # Run the development server
    run_dev_server()
