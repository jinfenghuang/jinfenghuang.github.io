"""views.py

"""

from flask import render_template

from app import app
from app import pages

# ------------------------------------------------
# Home
# ------------------------------------------------

@app.route('/')
def index():
	return render_template('index.html')

# ------------------------------------------------
# About
# ------------------------------------------------

@app.route('/about')
def about():
	return render_template('about.html')

# ------------------------------------------------
# Blog
# ------------------------------------------------

@app.route('/blog')
def blog():
	posts = [page for page in pages if 'date' in page.meta]
	sorted_posts = sorted(posts, reverse=True, key=lambda page: page.meta['date'])
	return render_template('blog.html', pages=sorted_posts)

@app.route('/<path:path>/')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)
