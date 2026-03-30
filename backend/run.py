from app import create_app
from app.extensions import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        print("Project started")

    app.run(host="0.0.0.0", port=5001, debug=True)
