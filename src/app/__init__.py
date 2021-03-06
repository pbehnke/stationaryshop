from app.account import account as account_bp
from app.admin import admin as admin_bp
from app.api import api as api_bp
from app.cart import cart as cart_bp
from app.catalog import catalog as catalog_bp
from app.extensions import (
    bcrypt,
    csrf_protect,
    db,
    login,
    mail,
    migrate,
    store,
)
from app.main import main as main_bp
from app.order import order as order_bp
from flask import (
    Flask,
    current_app,
    render_template,
    request
)
from flask_babel import Babel, lazy_gettext as _l
from flask_kvsession import KVSessionExtension


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    register_extensions(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    KVSessionExtension(store, app)
    babel = Babel(app)
    mail.init_app(app)

    @babel.localeselector
    def get_locale():
        # return 'ja'
        return request.accept_languages \
            .best_match(current_app.config['LANGUAGES'])
    return None


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(account_bp, url_prefix='/account')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(catalog_bp, url_prefix='/catalog')
    app.register_blueprint(order_bp, url_prefix='/order')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    return None


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{0}.html'.format(error_code)), error_code
    for errcode in [401, 403, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
