from flask import Flask, render_template, jsonify, send_from_directory
import os
import re

app = Flask(__name__)

# Enable caching for static files (1 week for images)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 604800  # 7 days in seconds

# Hardcoded fallback list for serverless environments (Vercel)
# This ensures pages load even if os.listdir doesn't work
FALLBACK_PAGES = [
    {'number': 3, 'image': '/static/images/portfolio_pg3.jpg'},
    {'number': 4, 'image': '/static/images/portfolio_pg4.jpg'},
    {'number': 5, 'image': '/static/images/portfolio_pg5.jpg'},
    {'number': 6, 'image': '/static/images/portfolio_pg6.jpg'},
    {'number': 7, 'image': '/static/images/portfolio_pg7.jpg'},
    {'number': 8, 'image': '/static/images/portfolio_pg8.jpg'},
    {'number': 9, 'image': '/static/images/portfolio_pg9.jpg'},
    {'number': 10, 'image': '/static/images/portfolio_pg10.jpg'},
    {'number': 11, 'image': '/static/images/portfolio_pg11.jpg'},
    {'number': 12, 'image': '/static/images/portfolio_pg12.jpg'},
    {'number': 13, 'image': '/static/images/portfolio_pg13.jpg'},
    {'number': 14, 'image': '/static/images/portfolio_pg14.jpg'},
    {'number': 15, 'image': '/static/images/portfolio_pg15.jpg'},
    {'number': 16, 'image': '/static/images/portfolio_pg16.jpg'},
    {'number': 17, 'image': '/static/images/portfolio_pg17.jpg'},
    {'number': 18, 'image': '/static/images/portfolio_pg18.jpg'},
    {'number': 19, 'image': '/static/images/portfolio_pg19.jpg'},
    {'number': 20, 'image': '/static/images/portfolio_pg20.jpg'},
    {'number': 21, 'image': '/static/images/portfolio_pg21.jpg'},
    {'number': 22, 'image': '/static/images/portfolio_pg22.jpg'},
    {'number': 23, 'image': '/static/images/portfolio_pg23.jpg'},
    {'number': 24, 'image': '/static/images/portfolio_pg24.jpg'},
    {'number': 25, 'image': '/static/images/portfolio_pg25.jpg'},
    {'number': 26, 'image': '/static/images/portfolio_pg26.jpg'},
    {'number': 27, 'image': '/static/images/portfolio_pg27.jpg'},
    {'number': 28, 'image': '/static/images/portfolio_pg28.jpg'},
    {'number': 29, 'image': '/static/images/portfolio_pg29.jpg'},
]

def get_portfolio_pages():
    """
    Automatically get all portfolio page images from the static/images folder.
    Returns them sorted by page number.
    Falls back to hardcoded list for serverless environments.
    """
    images_folder = os.path.join(app.static_folder, 'images')
    pages = []

    # Pages to exclude (e.g., page 30 contains "THE PAUSE..." text)
    excluded_pages = [30]

    # Pattern to match portfolio_pgXX.jpg files
    pattern = re.compile(r'portfolio_pg(\d+)\.jpg', re.IGNORECASE)

    try:
        if os.path.exists(images_folder):
            for filename in os.listdir(images_folder):
                match = pattern.match(filename)
                if match:
                    page_number = int(match.group(1))
                    # Skip excluded pages
                    if page_number not in excluded_pages:
                        pages.append({
                            'number': page_number,
                            'image': f'/static/images/{filename}'
                        })
    except Exception as e:
        # If file system scanning fails, use fallback
        print(f"File system error: {e}, using fallback pages")
        pass

    # If no pages found (serverless environment), use fallback
    if not pages:
        pages = FALLBACK_PAGES.copy()

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
