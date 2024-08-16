from flask import Flask, render_template
from g_api import g_api_bp
from home import home_bp

app = Flask(__name__)

app.register_blueprint(g_api_bp)
app.register_blueprint(home_bp)

@app.route('/')
def home():
    return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True)
