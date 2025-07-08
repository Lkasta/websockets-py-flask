import os
from dotenv import load_dotenv

from flask import Flask, jsonify
from repository.database import db

from models import payment

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
  return jsonify({"message", "The payment has been created!"})

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
  return jsonify({"message", "The payment has been confirmed!"})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page():
  return 'payment'

if __name__ == "__main__":
  app.run(debug=True)