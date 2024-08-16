from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ScamPreventionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = FloatField('Age', validators=[DataRequired(), NumberRange(min=18, max=100)])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TradePredictorForm(FlaskForm):
    stock_symbol = StringField('Stock Symbol', validators=[DataRequired()])
    investment_amount = FloatField('Investment Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

class OperationalRiskModelForm(FlaskForm):
    department = StringField('Department', validators=[DataRequired()])
    risk_score = FloatField('Risk Score', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MarketRiskModelForm(FlaskForm):
    market_index = StringField('Market Index', validators=[DataRequired()])
    volatility = FloatField('Volatility', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ValueAtRiskModelForm(FlaskForm):
    portfolio_value = FloatField('Portfolio Value', validators=[DataRequired()])
    confidence_level = FloatField('Confidence Level', validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Submit')

class CreditworthinessForm(FlaskForm):
    credit_score = FloatField('Credit Score', validators=[DataRequired()])
    annual_income = FloatField('Annual Income', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoanRepaymentProbabilityForm(FlaskForm):
    loan_amount = FloatField('Loan Amount', validators=[DataRequired()])
    term_length = FloatField('Term Length (years)', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ExposureAtDefaultForm(FlaskForm):
    exposure_value = FloatField('Exposure Value', validators=[DataRequired()])
    default_probability = FloatField('Default Probability', validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Submit')

class CreditRiskModelForm(FlaskForm):
    borrower_name = StringField('Borrower Name', validators=[DataRequired()])
    credit_risk_score = FloatField('Credit Risk Score', validators=[DataRequired()])
    submit = SubmitField('Submit')
