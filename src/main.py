import os, shutil, pathlib
from inline_markdown import extract_title, extract_markdown_links
from markdown_blocks import markdown_to_html_node
from textnode import TextNode

def main():
    
    print(extract_title("# Hello World"))
    
    def copy_static_files():
        if not os.path.exists("public"):
            print("Creating public directory...")
            os.mkdir("public")
            recursive_copy("static", "public")
            print("Done!")
        else:
            print("Deleting public directory")
            shutil.rmtree("public")
            print("Old public directory deleted.")
            print("Creating new public directory...")
            copy_static_files()
            print("Done!")
    
    def recursive_copy(source, destination):
        for item in os.listdir(source):
            source_path = os.path.join(source, item)
            destination_path = os.path.join(destination, item)
            if os.path.isdir(source_path):
                if not os.path.exists(destination_path):
                    os.mkdir(destination_path)
                    print("Created directory: " + destination_path)
                recursive_copy(source_path, destination_path)
            else:
                shutil.copy(source_path, destination_path)
                print("Copied file: " + destination_path)
                
    def generate_page(from_path, template_path, to_path):
        print(f"Generating page from {from_path} to {to_path} using {template_path}")
        from_file = open(from_path, "r").read()
        template_file = open(template_path, "r").read()
        
        convert_to_html = markdown_to_html_node(from_file)
        html_content = convert_to_html.to_html()
        title = extract_title(from_file)
        
        html = template_file.replace("{{ Title }}", title)
        html = html.replace("{{ Content }}", html_content)
        
        open(to_path, "w").write(html)
        print("Page generated!")
    
    def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
        # Crawl every entry in the content directory
        # For each markdown file found, generate a new .html file using the same template.html. The generated pages should be written to the public directory in the same directory structure.
        
        for entry in os.listdir(dir_path_content):
            if os.path.isdir(os.path.join(dir_path_content, entry)):
                os.mkdir(os.path.join(dest_dir_path, entry))
                generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry))
            else:
                if entry.endswith(".md"):
                    generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry.replace(".md", ".html")))
        
        
        

    copy_static_files()
    generate_pages_recursive("content", "template.html", "public")

main()
