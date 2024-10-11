import sys
import os
import base64
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_url(path):
    return path.startswith(('http://', 'https://'))

def get_content(path, base_dir):
    if is_url(path):
        return requests.get(path).content
    else:
        full_path = path if os.path.isabs(path) else os.path.join(base_dir, path)
        with open(full_path, 'rb') as file:
            return file.read()

def encode_image(content):
    return base64.b64encode(content).decode('utf-8')

def embed_resources(input_file, output_file):
    base_dir = os.path.dirname(input_file)

    with open(input_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Embed images
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            try:
                content = get_content(src, base_dir)
                img['src'] = f"data:image/{os.path.splitext(src)[1][1:]};base64,{encode_image(content)}"
            except Exception as e:
                print(f"Warning: Could not embed image {src}: {e}")

    # Embed CSS
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href')
        if href:
            try:
                content = get_content(href, base_url)
                style_tag = soup.new_tag('style')
                style_tag.string = content.decode('utf-8')
                link.replace_with(style_tag)
            except Exception as e:
                print(f"Warning: Could not embed CSS {href}: {e}")

    # Embed JavaScript
    for script in soup.find_all('script', src=True):
        src = script.get('src')
        if src:
            try:
                content = get_content(src, base_url)
                new_script = soup.new_tag('script')
                new_script.string = content.decode('utf-8')
                script.replace_with(new_script)
            except Exception as e:
                print(f"Warning: Could not embed JavaScript {src}: {e}")

    # Write the modified HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_html_file> <output_html_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    embed_resources(input_file, output_file)
    print(f"Self-contained HTML file created: {output_file}")

if __name__ == "__main__":
    main()
