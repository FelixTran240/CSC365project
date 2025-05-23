from flask import Flask
from services.database import init_db
from routes import buy, sell
from routes.price import bp as price_bp

app = Flask(__name__)

# Initialize the database
init_db(app)

# Register routes
app.register_blueprint(buy.bp)
app.register_blueprint(sell.bp)
app.register_blueprint(price_bp)

if __name__ == '__main__':
    app.run(debug=True)