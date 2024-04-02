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
        print("post_data", post_data)
        messages = post_data.get("messages")
        if not messages:
            return {"messages": "No messages provided"}, 400
        
        grade_level = post_data.get("grade_level")
        if not grade_level:
            return {"grade_level": "No grade_level provided"}, 400
        
        academic_topic = post_data.get("academic_topic")
        if not academic_topic:
            return {"academic_topic": "No academic_topic provided"}, 400

        try:
            updated_messages = asyncio.run(orchestrate_chatbot_pipeline(messages=messages, grade_level=grade_level, academic_topic=academic_topic))
            return updated_messages, 200
        except Exception as e:
            return {"error": str(e)}, 500

filters_namespace.add_resource(Filter, '')
