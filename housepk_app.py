from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HousePK! — Login version"


@app.route('/login')
def login():
    return "Login Page - Developed by Abdulrehman"

@app.route('/dashboard')
def dashboard():
    return "Dashboard Page"

if __name__ == '__main__':
    print("Login feature initialized...")  # added overlapping print line
    app.run(debug=True)
