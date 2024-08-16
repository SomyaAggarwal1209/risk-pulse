from flask import Blueprint, render_template, request, redirect, url_for

home_bp = Blueprint('home', __name__)


@home_bp.route('/chat')
def chat():
    return render_template('chat_page_final.html')

@home_bp.route('/dashboard')
def dashboard():
    return render_template('page_dashboard.html')

@home_bp.route('/about')
def about():
    return render_template('about.html')

@home_bp.route('/contact')
def contact():
    return render_template('contact.html')

@home_bp.route('/profile')
def profile():
    return render_template('profile.html')

@home_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']
        # Authentication logic goes here
    return render_template('login.html')

@home_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == ['POST']:
        # Handle signup form submission
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        # Registration logic goes here
    return render_template('login.html', action='signup')

@home_bp.route('/send_message', methods=['POST'])
def send_message():
    if request.method == ['POST']:
        message = request.form['message']
        # Logic to handle the message
        return redirect(url_for('home.chat'))  # Correctly specify the blueprint name
