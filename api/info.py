from flask import Blueprint

info_blueprint = Blueprint(
    name='info_blueprint',
    import_name=__name__,
)


@info_blueprint.route('/index')
def index():
    return "This is an example app"
