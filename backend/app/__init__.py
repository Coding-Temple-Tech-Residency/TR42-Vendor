from flask import Flask
from .extensions import db, ma
from .config import Config
from .logging_config import setup_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging()

    db.init_app(app)
    ma.init_app(app)

    from .routes import main
    from . import models
    app.register_blueprint(main)

    try:
        from .blueprints.vendor_user import vendor_user_bp
        app.register_blueprint(vendor_user_bp, url_prefix="/vendor_user")
    except ImportError:
        pass

    try:
        from .blueprints.vendor import vendor_bp
        app.register_blueprint(vendor_bp, url_prefix="/vendor")
    except ImportError:
        pass

    with app.app_context():
        db.create_all()

    return app