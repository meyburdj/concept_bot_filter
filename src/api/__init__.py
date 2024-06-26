from flask_restx import Api

from src.api.ping import ping_namespace
from src.api.filters.views import filters_namespace

api = Api(version="1.0", title="Users API", doc="/doc")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(filters_namespace, path="/filter")
