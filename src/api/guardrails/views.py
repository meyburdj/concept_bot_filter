import asyncio
from flask import request
from flask_restx import  Resource
from src.api.guardrails.schemas import messages_model, guardrails_namespace

from src.api.utils.nemo_guardrails.config.config import process_input_with_guardrails


class Guardrail(Resource):
    @guardrails_namespace.expect(messages_model, validate=True)
    def post(self):
        post_data = request.get_json()
        print("post_data", post_data)
        messages = post_data.get("messages")
        if not messages:
            return {"messages": "No messages provided"}, 400
        print("ok i got messages: ", messages)

        try:
            filtered_request_to_openai = asyncio.run(process_input_with_guardrails(messages))
            print("filtered_request_to_openai", filtered_request_to_openai)
            response_object = filtered_request_to_openai
            return response_object, 200
        except Exception as e:
            return {"error": str(e)}, 500

guardrails_namespace.add_resource(Guardrail, '')
