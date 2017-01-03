import server
from flask import Flask, render_template

app = Flask(__name__)

db = server.get_db()

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/login")
def login():
    render_template('login.html')

if __name__ == "__main__":
    app.run()