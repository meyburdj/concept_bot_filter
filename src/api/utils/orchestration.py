from src.api.utils.openai.calls import scaffold_response_call, continue_conversation_call

def orchestrate_chatbot_pipeline(client_messages, prompt_messages, grade_level, academic_topic):
    """Orchestrates flow of data across prompts and calls."""
    
    if len(client_messages) == 1 and client_messages[0]["role"] == "user":
        response = scaffold_response_call(client_messages=client_messages, prompt_messages=prompt_messages, grade_level=grade_level, academic_topic=academic_topic)
    else:
        response = continue_conversation_call(client_messages=client_messages, prompt_messages=prompt_messages)

    return response
