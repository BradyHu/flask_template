from flask import Blueprint
from flask_restplus import Api

from .v1.helloworld import api as ns_hello

from ..config import settings

blueprint = Blueprint('api',__name__,url_prefix='/api')

api = Api(blueprint, title=settings.NAME,version=settings.VERSION)

api.add_namespace(ns_hello)
