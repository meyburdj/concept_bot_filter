import asyncio
from flask import request
from flask_restx import  Resource
from src.api.filters.schemas import messages_model, filters_namespace
from src.api.utils.orchestration import orchestrate_chatbot_pipeline

from src.api.utils.nemo_guardrails.config.config import process_input_with_guardrails


class Filter(Resource):
    @filters_namespace.expect(messages_model, validate=True)
    def post(self):
        post_data = request.get_json()

        messages = post_data.get("messages")        
        print("messages :", messages)
        grade_level = post_data.get("gradeLevel")       
        academic_topic = post_data.get("academicTopic")

        try:
            updated_messages = orchestrate_chatbot_pipeline(messages=messages, grade_level=grade_level, academic_topic=academic_topic)
            print('updated_message: ', updated_messages)
            return updated_messages, 200
        except Exception as e:
            return {"error": str(e)}, 500

filters_namespace.add_resource(Filter, '')
