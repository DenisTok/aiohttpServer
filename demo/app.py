import base64
from aiohttp import web
import jinja2
import aiohttp_jinja2
import asyncpgsa
import aiopg
from aiopg.sa import create_engine
# from aiohttp_session import setup, get_session, session_middleware
# from aiohttp_session.cookie_storage import EncryptedCookieStorage
from .routes import setup_routes


async def create_app(config: dict):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    setup_routes(app)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    config = app['config']
    app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])


async def on_shutdown(app):
    await app['db'].close()
