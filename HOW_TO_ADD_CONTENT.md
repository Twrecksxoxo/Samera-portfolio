# 📖 HOW TO ADD YOUR CONTENT - Complete Guide

## 🏗️ ADDING/EDITING PROJECTS

All your projects are stored in `main.py`. Open this file and look for the `projects` list (starting at line 6).

---

### 📋 PROJECT STRUCTURE EXPLAINED

Each project is a dictionary with these fields:

```python
{
    "id": 1,                                    # REQUIRED - Unique number (1, 2, 3, etc.)
    "title": "Project Name",                    # REQUIRED - Name of your project
    "category": "Residential",                  # REQUIRED - Must be: "Residential", "Commercial", or "Interior"
    "year": "2025",                             # REQUIRED - Year completed
    "location": "City, Country",                # REQUIRED - Where the project is located
    "image": "path/to/image",                   # REQUIRED - Image URL or local path
    "description": "Brief project description"  # REQUIRED - 1-2 sentences about the project
}
```

---

### ✏️ HOW TO EDIT AN EXISTING PROJECT

**Example:** Change "Sunset Residence" to your own project:

**BEFORE:**
```python
{
    "id": 1,
    "title": "Sunset Residence",
    "category": "Residential",
    "year": "2025",
    "location": "Malibu, California",
    "image": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200",
    "description": "A modern coastal home that seamlessly blends indoor and outdoor living spaces."
}
```

**AFTER (Your Project):**
```python
{
    "id": 1,
    "title": "Villa Marina",
    "category": "Residential",
    "year": "2024",
    "location": "Dubai Marina, UAE",
    "image": "/static/images/villa-marina.jpg",
    "description": "A luxurious waterfront villa featuring panoramic sea views and contemporary Arabic design elements."
}
```

---

### ➕ HOW TO ADD A NEW PROJECT

Add a new project by copying this template and adding it to the `projects` list:

```python
{
    "id": 7,                                    # Use the next number in sequence
    "title": "Your New Project Name",
    "category": "Commercial",                   # Choose: Residential, Commercial, or Interior
    "year": "2026",
    "location": "Your City, Country",
    "image": "/static/images/your-image.jpg",   # See image section below
    "description": "Describe your project in 1-2 sentences."
},  # DON'T FORGET THE COMMA!
```

**Place it inside the `projects = [...]` list, like this:**

```python
projects = [
    {
        "id": 1,
        "title": "Project 1",
        ...
    },
    {
        "id": 2,
        "title": "Project 2",
        ...
    },
    {
        "id": 7,                    # <-- YOUR NEW PROJECT HERE
        "title": "Your New Project",
        "category": "Residential",
        "year": "2026",
        "location": "Your City",
        "image": "/static/images/new-project.jpg",
        "description": "Your description."
    }   # <-- Last item doesn't need a comma
]
```

---

### ❌ HOW TO REMOVE A PROJECT

Simply delete the entire block (including the curly braces `{ }`) for that project.

**Example - Remove "The Cube" project:**
Delete these lines from main.py:
```python
    {
        "id": 5,
        "title": "The Cube",
        "category": "Commercial",
        "year": "2023",
        "location": "Dubai, UAE",
        "image": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200",
        "description": "A bold geometric office building redefining the Dubai skyline."
    },
```

---

## 🖼️ IMAGES - Two Options

### Option 1: Use Online Images (Easiest)
Use any image URL from the web:
```python
"image": "https://example.com/your-image.jpg"
```

**Free architecture images:**
- https://unsplash.com (search "architecture", "interior design", etc.)
- https://pexels.com
- Your own cloud storage (Google Drive, Dropbox public links)

### Option 2: Use Local Images (Recommended for Production)

1. **Save your image** to: `static/images/` folder
   
   Example: `D:\Samera portfolio\static\images\my-project.jpg`

2. **Reference it like this:**
   ```python
   "image": "/static/images/my-project.jpg"
   ```

**Image Tips:**
- Use high-quality images (at least 1200px wide)
- Recommended aspect ratio: 4:5 (portrait) works best with the grid
- Supported formats: JPG, PNG, WebP
- Keep file sizes under 500KB for fast loading

---

## 📂 CATEGORY OPTIONS

The website has three filter buttons. Use these exact category names:

| Category | Use For |
|----------|---------|
| `"Residential"` | Houses, apartments, villas, private homes |
| `"Commercial"` | Offices, hotels, retail, public buildings |
| `"Interior"` | Interior design projects, renovations |

---

## 🔄 COMPLETE EXAMPLE - Replace All Projects

Here's how your `main.py` would look with your own projects:

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# YOUR Portfolio Projects
projects = [
    {
        "id": 1,
        "title": "Al Wasl Tower",
        "category": "Commercial",
        "year": "2024",
        "location": "Dubai, UAE",
        "image": "/static/images/al-wasl-tower.jpg",
        "description": "A 45-story mixed-use tower featuring sustainable design and smart building technology."
    },
    {
        "id": 2,
        "title": "Palm Villa",
        "category": "Residential",
        "year": "2024",
        "location": "Palm Jumeirah, Dubai",
        "image": "/static/images/palm-villa.jpg",
        "description": "Ultra-luxury beachfront villa with infinity pool and private marina."
    },
    {
        "id": 3,
        "title": "Minimalist Penthouse",
        "category": "Interior",
        "year": "2023",
        "location": "Downtown Dubai",
        "image": "/static/images/penthouse.jpg",
        "description": "Contemporary interior design for a 5,000 sq ft penthouse with panoramic city views."
    },
    {
        "id": 4,
        "title": "Desert Spa Resort",
        "category": "Commercial",
        "year": "2023",
        "location": "Al Ain, UAE",
        "image": "/static/images/spa-resort.jpg",
        "description": "An eco-friendly wellness retreat inspired by traditional Arabian architecture."
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
```

---

## ⚠️ COMMON MISTAKES TO AVOID

1. **Missing comma between projects:**
   ```python
   }    # ❌ WRONG - missing comma
   {
   ```
   ```python
   },   # ✅ CORRECT - comma after each project (except the last one)
   {
   ```

2. **Wrong category spelling:**
   ```python
   "category": "residential"     # ❌ WRONG - lowercase
   "category": "Residential"     # ✅ CORRECT - capitalized
   ```

3. **Wrong image path:**
   ```python
   "image": "images/photo.jpg"           # ❌ WRONG
   "image": "/static/images/photo.jpg"   # ✅ CORRECT
   ```

4. **Missing quotes around text:**
   ```python
   "title": My Project           # ❌ WRONG
   "title": "My Project"         # ✅ CORRECT
   ```

---

## 🚀 AFTER MAKING CHANGES

1. **Save the file** (Ctrl+S)

2. **Restart the server:**
   - Stop the running server (Ctrl+C in terminal)
   - Run again: `python main.py`

3. **Refresh your browser** (Ctrl+F5 for hard refresh)

4. **View at:** http://localhost:5000

---

## 📧 NEED MORE HELP?

If you want to change other content (About section, Contact info, etc.), 
see the `templates/index.html` file.
