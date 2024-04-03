from src.api.utils.openai.calls import scaffold_response_call, continue_conversation_call

def orchestrate_chatbot_pipeline(messages, grade_level, academic_topic):
    """Orchestrates flow of data across prompts and calls."""
    
    print("messages[0]['role']: ", messages[0]["role"])
    if len(messages) == 1 and messages[0]["role"] == "user":
        print("scaffold_response_call")
        response = scaffold_response_call(messages=messages, grade_level=grade_level, academic_topic=academic_topic)
    else:
        print("i'm about to do continue_conversation_prompt")
        response = continue_conversation_call(messages=messages)

    return response
