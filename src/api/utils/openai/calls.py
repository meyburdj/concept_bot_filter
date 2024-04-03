import openai
from src.api.utils.openai.config import get_openai_key
from src.api.utils.openai.prompts import scaffold_response_prompt, continue_conversation_prompt


def scaffold_response_call( messages, grade_level, academic_topic):
    """ Takes in a question. Returns an outline scaffolding the concepts building
     to the concepet's answer."""

    api_key = get_openai_key()
    openai.api_key = api_key

    new_message = scaffold_response_prompt(messages, grade_level, academic_topic)

    chat_completion = openai.chat.completions.create(
        messages=messages + [new_message],
        model="gpt-3.5-turbo-instruct",
        # model="gpt-4-0125-preview",
    )

    return chat_completion.choices[0].message.content

def continue_conversation_call(messages):
    """ Takes in a question. Returns an outline scaffolding the concepts building
     to the concepet's answer."""

    api_key = get_openai_key()
    openai.api_key = api_key

    new_message = continue_conversation_prompt(messages)
    print("here's the new_message :", new_message)

    chat_completion = openai.chat.completions.create(
        messages=messages + [new_message],
        model="gpt-3.5-turbo-instruct",
        # model="gpt-4-0125-preview",
    )

    return chat_completion.choices[-1].message.content