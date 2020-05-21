from flask import Blueprint
from flask_restplus import Api

from .helloworld import api as ns_hello
from .users import api as ns_users

from ..config import settings

blueprint = Blueprint('api',__name__,url_prefix='/api')

api = Api(blueprint, title=settings.NAME,version=settings.VERSION)
api.add_namespace(ns_hello)
api.add_namespace(ns_users)