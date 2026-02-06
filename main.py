from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Portfolio Projects Data
projects = [
    {
        "id": 1,
        "title": "Sunset Residence",
        "category": "Residential",
        "year": "2025",
        "location": "Malibu, California",
        "image": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200",
        "description": "A modern coastal home that seamlessly blends indoor and outdoor living spaces."
    },
    {
        "id": 2,
        "title": "Urban Loft",
        "category": "Interior",
        "year": "2024",
        "location": "New York City",
        "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200",
        "description": "Industrial meets contemporary in this Manhattan penthouse renovation."
    },
    {
        "id": 3,
        "title": "Glass Pavilion",
        "category": "Commercial",
        "year": "2024",
        "location": "Tokyo, Japan",
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200",
        "description": "A floating glass structure designed for art exhibitions and cultural events."
    },
    {
        "id": 4,
        "title": "Desert Oasis",
        "category": "Residential",
        "year": "2023",
        "location": "Scottsdale, Arizona",
        "image": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200",
        "description": "Sustainable desert living with panoramic mountain views."
    },
    {
        "id": 5,
        "title": "The Cube",
        "category": "Commercial",
        "year": "2023",
        "location": "Dubai, UAE",
        "image": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200",
        "description": "A bold geometric office building redefining the Dubai skyline."
    },
    {
        "id": 6,
        "title": "Forest Retreat",
        "category": "Residential",
        "year": "2022",
        "location": "Vancouver, Canada",
        "image": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200",
        "description": "A timber-clad sanctuary nestled among ancient cedars."
    }
]


@app.route('/')
def home():
    return render_template('index.html', projects=projects)


@app.route('/api/projects')
def get_projects():
    return jsonify(projects)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
