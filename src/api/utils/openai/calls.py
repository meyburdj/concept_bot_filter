from openai import OpenAI
from src.api.utils.openai.config import get_openai_key
from src.api.utils.openai.prompts import scaffold_response_response, continue_conversation_prompt


async def scaffold_response_call( messages, grade_level, academic_topic):
    """ Takes in a question. Returns an outline scaffolding the concepts building
     to the concepet's answer."""

    api_key = get_openai_key()
    client = OpenAI(api_key)

    updated_messages = scaffold_response_response(messages, grade_level, academic_topic)

    chat_completion = client.chat.completions.create(
        messages=updated_messages,
        model="gpt-3.5-turbo",
    )

    return chat_completion

async def continue_conversation_prompt(messages):
    """ Takes in a question. Returns an outline scaffolding the concepts building
     to the concepet's answer."""

    api_key = get_openai_key()
    client = OpenAI(api_key)

    updated_messages = scaffold_response_response(messages)

    chat_completion = client.chat.completions.create(
        messages=updated_messages,
        model="gpt-3.5-turbo",
    )

    return chat_completion