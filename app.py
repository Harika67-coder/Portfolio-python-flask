from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data
projects = [
    {"title": "Authentication System", "description": "A secure authentication system using Node.js, Express, and SQLite, integrating JWT for authentication and bcrypt for password hashing.", "link": "https://authentication-system-project-using-node-7ysz.onrender.com/"},
    {"title": "Task Manager", "description": "A task management app with CRUD features.", "link": "https://task-management-system-node-express12.onrender.com/"},
    {"title": "E-Commerce Platform", "description": "An online store with user authentication.", "link": "https://authentication-system-project-using-node-7ysz.onrender.com/"}
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/api/projects')
def get_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)
