import asyncio
from flask import request
from flask_restx import Namespace, Resource, fields

from src.api.utils.nemo_guardrails.config.config import process_input_with_guardrails

guardrails_namespace = Namespace("guardrails")

# Define the model for a single message
message_model = guardrails_namespace.model('Message', {
    'role': fields.String(required=True, description='The role of the message sender'),
    'content': fields.String(required=True, description='The content of the message'),
})

# Define the model for the request body, which contains an array of messages
messages_post = guardrails_namespace.model('MessagesPost', {
    'messages': fields.List(fields.Nested(message_model), required=True, description='List of messages'),
})

class Guardrail(Resource):
    @guardrails_namespace.expect(messages_post, validate=True)
    def post(self):
        post_data = request.get_json()
        messages = post_data.get("messages")
        if not messages:
            return {"messages": "No messages provided"}, 400
        print("ok i got messages: ", messages)

        try:
            filtered_request_to_openai = asyncio.run(process_input_with_guardrails(messages))
            response_object = {"role": "assistant", "content": filtered_request_to_openai}
            return response_object, 200
        except Exception as e:
            return {"error": str(e)}, 500

guardrails_namespace.add_resource(Guardrail, '')
