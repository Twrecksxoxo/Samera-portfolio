from flask import Flask, render_template, jsonify
import os
import re

app = Flask(__name__)

def get_portfolio_pages():
    """
    Automatically get all portfolio page images from the static/images folder.
    Returns them sorted by page number.
    """
    images_folder = os.path.join(app.static_folder, 'images')
    pages = []

    # Pattern to match portfolio_pgXX.jpg files
    pattern = re.compile(r'portfolio_pg(\d+)\.jpg', re.IGNORECASE)

    if os.path.exists(images_folder):
        for filename in os.listdir(images_folder):
            match = pattern.match(filename)
            if match:
                page_number = int(match.group(1))
                pages.append({
                    'number': page_number,
                    'image': f'/static/images/{filename}'
                })

    # Sort by page number
    pages.sort(key=lambda x: x['number'])
    return pages


@app.route('/')
def home():
    pages = get_portfolio_pages()
    return render_template('flipbook_3d.html', pages=pages)


@app.route('/classic')
def classic():
    pages = get_portfolio_pages()
    return render_template('index.html', pages=pages)


@app.route('/flipbook-old')
def flipbook_old():
    pages = get_portfolio_pages()
    return render_template('flipbook.html', pages=pages)


@app.route('/flipbook-v2')
def flipbook_v2():
    pages = get_portfolio_pages()
    return render_template('flipbook_new.html', pages=pages)


@app.route('/api/pages')
def get_all_pages():
    pages = get_portfolio_pages()
    return jsonify(pages)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
