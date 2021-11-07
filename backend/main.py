from src import app, db
from src.config import PORT


if __name__ == '__main__':
    db.create_all()
    app.run(debug=False, port=PORT)
