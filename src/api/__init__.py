from flask_restx import Api

from src.api.ping import ping_namespace
from src.api.guardrails.views import guardrails_namespace

api = Api(version="1.0", title="Users API", doc="/doc")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(guardrails_namespace, path="/filter")
