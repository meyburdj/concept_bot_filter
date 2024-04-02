from flask_restx import Namespace, fields

guardrails_namespace = Namespace("guardrails")

message_model = guardrails_namespace.model('Message', {
    'role': fields.String(required=True, description='The role of the message sender will be assistant or user'),
    'content': fields.String(required=True, description='The content of the message'),
})

messages_model = guardrails_namespace.model('MessagesPost', {
    'messages': fields.List(fields.Nested(message_model), required=True, description='List of messages'),
})