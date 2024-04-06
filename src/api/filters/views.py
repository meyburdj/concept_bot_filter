import asyncio
from flask import request
from flask_restx import  Resource
from src.api.filters.schemas import messages_model, filters_namespace
from src.api.utils.orchestration import orchestrate_chatbot_pipeline

from src.api.utils.nemo_guardrails.config.config import process_input_with_guardrails


class Filter(Resource):
    @filters_namespace.expect(messages_model, validate=True)
    def post(self):
        """
        Receives list of client messages, prompt messages, and 
        context (grade level, academic topic). Client messages are strictly for client
        display. prompt messages are to maintain conversational context. 
        Orchestrates processing of chat conversation, returning the resulting
        message and the list of prompt messages with a new user and a new assistant
        dictionary appended. 
        """
        post_data = request.get_json()

        client_messages = post_data.get("clientMessages")
        prompt_messages = post_data.get("promptMessages")        
        grade_level = post_data.get("gradeLevel")       
        academic_topic = post_data.get("academicTopic")

        try:
            updated_messages = orchestrate_chatbot_pipeline(client_messages=client_messages, prompt_messages=prompt_messages, grade_level=grade_level, academic_topic=academic_topic)
            print('updated_messages', updated_messages)
            return updated_messages
            client_message = updated_messages['client_message']
            updated_prompt_messages = updated_messages['updated_prompt_messages']
            return {"clientMessage": client_message, "promptMessages": updated_prompt_messages}, 200
        except Exception as e:
            return {"error": str(e)}, 500

filters_namespace.add_resource(Filter, '')
