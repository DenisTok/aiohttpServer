from .views import frontend


def setup_routes(app):
    # app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('GET', '/post', frontend.post)
    app.router.add_get('/', frontend.index, name='index')
