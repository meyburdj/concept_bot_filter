from flask import request
from flask_restx import Namespace, Resource, fields
import asyncio

from src.api.utils.nemo_guardrails.config.config import process_request

guardrails_namespace = Namespace("guardrails")

openai_post = guardrails_namespace.model(
    "Message",
    {"message": fields.String(required=True)}
)

class Guardrail(Resource):
    @guardrails_namespace.expect(openai_post, validate=True)
    async def post(self):
        post_data = request.get_json()
        message = post_data.get("message")

        if not message:
            return {"message": "No message provided"}, 400

        try:
            filtered_request_to_openai = asyncio.run(process_request(message))
            response_object = {"message": filtered_request_to_openai}
            return response_object, 200
        except Exception as e:
            return {"error": str(e)}, 500

guardrails_namespace.add_resource(Guardrail, '')