import openai
from src.api.utils.openai.config import get_openai_key
from src.api.utils.openai.prompts import scaffold_response_prompt,initial_scaffolding_prompt, is_question_prompt, continue_conversation_prompt, construct_system_prompt

def is_question_call(initial_message, grade_level, academic_topic):
    """takes in an initial user message. sends prompt determing if the initial
    input was a question. Returns boolean depending on if question or not question """

    api_key = get_openai_key()
    openai.api_key = api_key
    is_question = is_question_prompt(initial_message=initial_message, grade_level=grade_level, 
                                     academic_topic=academic_topic)
    print(is_question)
    chat_completion = openai.chat.completions.create(
    messages=[is_question],
    model="gpt-3.5-turbo",
    # model="gpt-4-0125-preview",
)
    chat_completion_content = chat_completion.choices[-1].message.content
    print("chat_comletion", chat_completion_content)
    
    if "yes" in chat_completion_content.lower():
        return True
    else:
        return False

def initial_scaffolding_call(initial_message, grade_level, academic_topic):
    """ Takes in a question. Generates an outline scaffolding the concepts building
     to the concepet's answer and apends that to a list with a system prompt. 
     Returns the raw assistant response, updates the prompt_mesages list, and 
     returns the list"""
    
    api_key = get_openai_key()
    openai.api_key = api_key

    initial_scaffolding = initial_scaffolding_prompt(initial_message=initial_message, 
                                                     grade_level=grade_level, 
                                                     academic_topic=academic_topic)
    
    chat_completion = openai.chat.completions.create(
        messages=[initial_scaffolding],
        model="gpt-3.5-turbo",
        # model="gpt-4-0125-preview",
    )
    chat_completion_content = chat_completion.choices[-1].message.content
    print("chat_comletion", chat_completion_content)
    return chat_completion_content    

def initial_question_call(scaffolding, grade_level, academic_topic):
    """"Takes in a user question and a scaffolded response. Produces a question 
    related to the first concept within the scaffolding"""

    api_key = get_openai_key()
    openai.api_key = api_key

    initial_question = initial_question_prompt(scaffolding=scaffolding, 
                                                     grade_level=grade_level, 
                                                     academic_topic=academic_topic)
    
    return initial_question


def catch_all_initial_response_call( client_messages, grade_level, academic_topic):
    """ Takes in a question. Generates an outline scaffolding the concepts building
     to the concepet's answer and apends that to a list with a system prompt. 
     Returns the raw assistant response, updates the prompt_mesages list, and 
     returns the list"""

    api_key = get_openai_key()
    openai.api_key = api_key

    system_prompt = construct_system_prompt(grade_level=grade_level, academic_topic=academic_topic)
    new_prompt_message = scaffold_response_prompt(client_messages, grade_level, academic_topic)
    prompt_messages =  [system_prompt, new_prompt_message] 
    
    chat_completion = openai.chat.completions.create(
        messages=prompt_messages,
        model="gpt-3.5-turbo",
        # model="gpt-4-0125-preview",
    )

    chat_completion_content = chat_completion.choices[-1].message.content
    prompt_message_object = {"role": "assistant", "content": chat_completion_content}
    prompt_messages = prompt_messages + [prompt_message_object]

    return {'updated_prompt_messages': prompt_messages, 
            "client_message": chat_completion_content}

def continue_conversation_call(client_messages, prompt_messages):
    """ Continues the conversation while maintaining prompt context. Returns the 
    raw assistant response and the updated prompt messages list"""

    api_key = get_openai_key()
    openai.api_key = api_key

    new_prompt_message = continue_conversation_prompt(client_messages)
    prompt_messages = prompt_messages + [new_prompt_message]

    chat_completion = openai.chat.completions.create(
        messages=prompt_messages,
        model="gpt-3.5-turbo",
        # model="gpt-4-0125-preview",
    )

    chat_completion_content = chat_completion.choices[-1].message.content
    prompt_message_object = {"role": "assistant", "content": chat_completion_content}
    prompt_messages = prompt_messages + [prompt_message_object]

    return {'updated_prompt_messages': prompt_messages, 
            "client_message": chat_completion_content}