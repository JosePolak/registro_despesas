from flask import Flask


def create_app():
    app = Flask(
        __name__,
        template_folder = 'templates',
        static_folder = 'static'
    )

    from app.db_init import init_db
    from app.routes.main import main

    app.register_blueprint(main)

    with app.app_context():
        init_db()

    return app
