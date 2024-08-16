from flask import Flask, render_template, request, redirect, url_for
from forms import (ScamPreventionForm, TradePredictorForm, OperationalRiskModelForm, MarketRiskModelForm,
                   ValueAtRiskModelForm, CreditworthinessForm, LoanRepaymentProbabilityForm,
                   ExposureAtDefaultForm, CreditRiskModelForm)

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    return render_template('chat_page_final.html')

@app.route('/dashboard')
def dashboard():
    return render_template('page_dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']
        # Authentication logic goes here
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup form submission
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        # Registration logic goes here
    return render_template('login.html', action='signup')

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        message = request.form['message']
        # Logic to handle the message
        return redirect(url_for('chat'))

@app.route('/scam_prevention', methods=['GET', 'POST'])
def scam_prevention():
    form = ScamPreventionForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Scam Prevention model executed successfully'))
    return render_template('pages/forms/scam_prevention.html', form=form, title='Scam Prevention')

@app.route('/trad_predictor', methods=['GET', 'POST'])
def trade_predictor():
    form = TradePredictorForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Trade Predictor model executed successfully'))
    return render_template('pages/forms/trad_predictor.html', form=form, title='Trade Predictor')

@app.route('/operational_risk', methods=['GET', 'POST'])
def operational_risk_model():
    form = OperationalRiskModelForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Operational Risk model executed successfully'))
    return render_template('pages/forms/op.html', form=form, title='Operational Risk Model')

@app.route('/market_risk-model', methods=['GET', 'POST'])
def market_risk_model():
    form = MarketRiskModelForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Market Risk model executed successfully'))
    return render_template('pages/forms/market_risk.html', form=form, title='Market Risk Model')

@app.route('/value_at_risk-model', methods=['GET', 'POST'])
def value_at_risk_model():
    form = ValueAtRiskModelForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Value at Risk model executed successfully'))
    return render_template('pages/forms/value_at_risk.html', form=form, title='Value at Risk Model')

@app.route('/creditworthiness', methods=['GET', 'POST'])
def creditworthiness():
    form = CreditworthinessForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Creditworthiness model executed successfully'))
    return render_template('pages/forms/creditworthiness.html', form=form, title='Creditworthiness')

@app.route('/loan_repayment_probability', methods=['GET', 'POST'])
def loan_repayment_probability():
    form = LoanRepaymentProbabilityForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Loan Repayment Probability model executed successfully'))
    return render_template('pages/forms/loan_repayment_probability.html', form=form, title='Loan Repayment Probability')

@app.route('/exposure-at-default', methods=['GET', 'POST'])
def exposure_at_default():
    form = ExposureAtDefaultForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Exposure at Default model executed successfully'))
    return render_template('pages/forms/exposure_at_default.html', form=form, title='Exposure at Default')

@app.route('/credit_risk-model', methods=['GET', 'POST'])
def credit_risk_model():
    form = CreditRiskModelForm()
    if form.validate_on_submit():
        # Process the form data and generate output
        return redirect(url_for('home', alert='Credit Risk model executed successfully'))
    return render_template('pages/forms/credit_risk.html', form=form, title='Credit Risk Model')

if __name__ == '__main__':
    app.run(debug=True)
