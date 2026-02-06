# 🚀 DEPLOYMENT GUIDE - Make Your Portfolio Live!

This guide will walk you through deploying your portfolio website step by step.

---

## 📋 PREREQUISITES

Before deploying, make sure you have:
1. A GitHub account (free): https://github.com/signup
2. Git installed on your computer: https://git-scm.com/downloads
3. Your project files ready (which you have!)

---

## STEP 1: Upload Your Project to GitHub

### 1.1 Create a GitHub Repository

1. Go to https://github.com
2. Click the **+** icon (top right) → **New repository**
3. Fill in:
   - Repository name: `architect-portfolio` (or any name)
   - Description: "My Architecture Portfolio Website"
   - Select: **Public**
   - DON'T check "Add a README file" (we already have one)
4. Click **Create repository**

### 1.2 Upload Your Files Using Git

Open PowerShell/Terminal in your project folder (`D:\Samera portfolio`) and run these commands one by one:

```powershell
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit - Portfolio website"

# Connect to your GitHub repository (replace with YOUR GitHub username and repo name)
git remote add origin https://github.com/YOUR_USERNAME/architect-portfolio.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** If prompted, login with your GitHub credentials.

---

## STEP 2: Deploy to Render.com (RECOMMENDED - FREE)

Render is the easiest free hosting platform for Flask apps.

### 2.1 Create Render Account

1. Go to https://render.com
2. Click **Get Started for Free**
3. Sign up with your **GitHub account** (easiest option)

### 2.2 Create New Web Service

1. From Render dashboard, click **New +** → **Web Service**
2. Connect your GitHub account if not already connected
3. Find and select your `architect-portfolio` repository
4. Click **Connect**

### 2.3 Configure Your Service

Fill in the settings:

| Setting | Value |
|---------|-------|
| **Name** | `samera-portfolio` (or any name) |
| **Region** | Choose closest to you |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn main:app` |
| **Instance Type** | `Free` |

### 2.4 Deploy!

1. Click **Create Web Service**
2. Wait 2-5 minutes for deployment
3. Your site will be live at: `https://samera-portfolio.onrender.com`

**⚠️ Note:** Free tier sites sleep after 15 minutes of inactivity. First visit after sleep takes ~30 seconds.

---

## ALTERNATIVE: Deploy to PythonAnywhere (FREE)

Good option if Render doesn't work for you.

### 3.1 Create Account

1. Go to https://www.pythonanywhere.com
2. Click **Pricing & signup** → **Create a Beginner account** (FREE)
3. Choose a username (this will be in your URL)

### 3.2 Upload Your Files

**Option A: Using Git (Recommended)**

1. Go to **Consoles** → **Bash**
2. Run:
   ```bash
   git clone https://github.com/YOUR_USERNAME/architect-portfolio.git
   ```

**Option B: Manual Upload**

1. Go to **Files** tab
2. Create folder: `architect-portfolio`
3. Upload all your files manually

### 3.3 Create Virtual Environment

In the Bash console:
```bash
cd architect-portfolio
mkvirtualenv --python=/usr/bin/python3.10 portfolioenv
pip install -r requirements.txt
```

### 3.4 Configure Web App

1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Manual configuration** → **Python 3.10**
4. Set these values:

| Setting | Value |
|---------|-------|
| **Source code** | `/home/YOUR_USERNAME/architect-portfolio` |
| **Working directory** | `/home/YOUR_USERNAME/architect-portfolio` |
| **Virtualenv** | `/home/YOUR_USERNAME/.virtualenvs/portfolioenv` |

5. Edit the **WSGI configuration file** and replace contents with:

```python
import sys
path = '/home/YOUR_USERNAME/architect-portfolio'
if path not in sys.path:
    sys.path.append(path)

from main import app as application
```

6. Click **Reload** (green button)

### 3.5 Your Site is Live!

Visit: `https://YOUR_USERNAME.pythonanywhere.com`

---

## ALTERNATIVE: Deploy to Railway.app (FREE TIER)

### 4.1 Create Account

1. Go to https://railway.app
2. Sign up with GitHub

### 4.2 Deploy

1. Click **New Project**
2. Select **Deploy from GitHub repo**
3. Choose your `architect-portfolio` repository
4. Railway auto-detects Python and deploys!
5. Click **Generate Domain** to get your URL

---

## 🌐 CUSTOM DOMAIN (Optional)

Want `www.yourname.com` instead of `yourname.onrender.com`?

### Buy a Domain

- Namecheap: https://namecheap.com (~$10/year)
- Google Domains: https://domains.google (~$12/year)
- GoDaddy: https://godaddy.com

### Connect to Render

1. In Render dashboard, go to your service
2. Click **Settings** → **Custom Domains**
3. Add your domain (e.g., `www.yourportfolio.com`)
4. Copy the CNAME record provided
5. Go to your domain registrar's DNS settings
6. Add a CNAME record pointing to Render

---

## 🔄 UPDATING YOUR SITE

After making changes locally:

```powershell
# Add changes
git add .

# Commit with a message
git commit -m "Updated project content"

# Push to GitHub
git push
```

**Render/Railway:** Auto-deploys when you push!
**PythonAnywhere:** Click the **Reload** button in Web tab.

---

## ❓ TROUBLESHOOTING

### "Application Error" on Render
- Check the **Logs** tab for errors
- Make sure `requirements.txt` has all dependencies
- Verify `Procfile` exists with: `web: gunicorn main:app`

### Site Not Loading
- Wait 2-5 minutes after initial deployment
- Clear browser cache (Ctrl+Shift+R)
- Check if the build succeeded in the dashboard

### Images Not Showing
- Use full URLs for images (not local paths) for easiest setup
- Or make sure images are in `static/images/` and committed to Git

---

## 📁 YOUR PROJECT STRUCTURE

Make sure your project has these files before deploying:

```
Samera portfolio/
├── main.py              ✅ Your Flask app
├── requirements.txt     ✅ Python dependencies
├── Procfile            ✅ For Render/Railway
├── .gitignore          ✅ Ignore unnecessary files
├── README.md           ✅ Project description
├── templates/
│   └── index.html      ✅ HTML template
└── static/
    ├── css/
    │   └── style.css   ✅ Styles
    ├── js/
    │   └── main.js     ✅ JavaScript
    └── images/         ✅ Your project images
```

---

## 🎉 CONGRATULATIONS!

Your portfolio is now live on the internet! Share your URL with clients, on LinkedIn, or anywhere else.

**Quick Links:**
- Render Dashboard: https://dashboard.render.com
- PythonAnywhere Dashboard: https://www.pythonanywhere.com
- Railway Dashboard: https://railway.app/dashboard
