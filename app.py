import os
import logging
from flask import Flask, render_template, send_from_directory, request

# Configure logging - use INFO for production
logging.basicConfig(level=logging.INFO)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "multi-tools-secret-key")

# Add cache control headers
@app.after_request
def add_header(response):
    # Cache static assets for 1 week
    if 'static/' in request.path:
        response.cache_control.max_age = 60 * 60 * 24 * 7  # 1 week
    return response

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# Route for serving tool pages
@app.route('/tools/<tool_name>')
def tool_page(tool_name):
    try:
        template_path = f'tools/{tool_name}.html'
        logging.debug(f"Attempting to render template: {template_path}")
        return render_template(template_path)
    except Exception as e:
        logging.error(f"Error serving tool {tool_name}: {str(e)}")
        # Check if template exists before redirecting
        if app.template_folder:
            template_file = os.path.join(app.template_folder, 'tools', f'{tool_name}.html')
            if os.path.exists(template_file):
                logging.error(f"Template exists at {template_file} but failed to render")
            else:
                logging.error(f"Template does not exist at {template_file}")
        return render_template('index.html', error=f"Tool '{tool_name}' not found")

# Handle favicon.ico
@app.route('/favicon.ico')
def favicon():
    static_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(static_dir,
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Serve tool categories
@app.route('/category/<category_name>')
def category(category_name):
    return render_template('index.html', category=category_name)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', error="Page not found"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('index.html', error="Internal server error"), 500
