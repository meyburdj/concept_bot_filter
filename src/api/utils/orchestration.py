from src.api.utils.openai.calls import scaffold_response_call, continue_conversation_prompt

async def orchestrate_chatbot_pipeline(messages, grade_level, academic_topic):
    """Orchestrates flow of data across prompts and calls."""
    
    if len(messages) == 1 and messages[0]["role"] == "user":
        response = await scaffold_response_call(messages=messages, grade_level=grade_level, academic_topic=academic_topic)
    else:
        response = await continue_conversation_prompt(messages=messages)

    return response
