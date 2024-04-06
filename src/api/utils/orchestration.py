from src.api.utils.openai.calls import (catch_all_initial_response_call, 
continue_conversation_call, is_question_call, initial_scaffolding_call, initial_question_call, 
catch_all_initial_response_call)

def orchestrate_initial_response(client_messages, grade_level, academic_topic):
    """Determines if the first user messages is a question. If it is a question, then
    scaffold conceptual response, create initial multiple choice question, return assistant
    message, user prompt, and assistant prompt."""

    initial_message = client_messages[0]
    is_question=is_question_call(initial_message=initial_message, 
                                 grade_level=grade_level, academic_topic=academic_topic)


    if(is_question):
        initial_scaffolding = initial_scaffolding_call(initial_message=initial_message, 
                                                       grade_level=grade_level, 
                                                       academic_topic=academic_topic)
        return initial_scaffolding
        initial_question = initial_question_call(initial_scaffolding, grade_level, academic_topic)
        initial_message = initial_scaffolding + initial_question
        return initial_message
    else:
        catch_all_initial_response = catch_all_initial_response_call(client_messages=client_messages, 
                                                    grade_level=grade_level, 
                                                    academic_topic=academic_topic )
        return catch_all_initial_response

def orchestrate_chatbot_pipeline(client_messages, prompt_messages, grade_level, academic_topic):
    """Orchestrates flow of data across prompts and calls."""
    
    if len(client_messages) == 1 and client_messages[0]["role"] == "user":
        response = orchestrate_initial_response(client_messages=client_messages, grade_level=grade_level, academic_topic=academic_topic)
    else:
        response = continue_conversation_call(client_messages=client_messages, prompt_messages=prompt_messages)

    return response
