"""News Flash - Application Factory"""
import os
from typing import Optional
from flask import Flask
from .config import config

def create_app(config_name: Optional[str] = None) -> Flask:
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "development")

    app = Flask(
        __name__,
        template_folder="presentation/templates",
        static_folder="presentation/static",
    )

    app.config.from_object(config[config_name])

    # Register blueprints
    from .presentation.routes.public import bp as public_bp
    app.register_blueprint(public_bp)

    return app

# Create app instance for flask run
app = create_app()