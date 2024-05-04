from flask import Flask
from resources.usuario import usuario
from models import db

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_db_user:your_db_password@your_db_host/your_db_name'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///CI_NOTICIARIO.db"
app.register_blueprint(usuario)
db.init_app(app)

with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run()