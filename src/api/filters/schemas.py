from flask_restx import Namespace, fields

filters_namespace = Namespace("filters")

message_model = filters_namespace.model('Message', {
    'role': fields.String(required=True, description='The role of the message sender will be assistant or user'),
    'content': fields.String(required=True, description='The content of the message'),
})

messages_model = filters_namespace.model('MessagesPost', {
    'gradeLevel': fields.String(required=True, description='The role of the message sender will be assistant or user'),
    'academicTopic': fields.String(required=True, description='The role of the message sender will be assistant or user'),
    'messages': fields.List(fields.Nested(message_model), required=True, description='List of messages'),
})
