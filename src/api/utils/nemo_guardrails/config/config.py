from nemoguardrails import LLMRails, RailsConfig

CONFIG_PATH = 'src/api/utils/nemo_guardrails/config'

async def process_input_with_guardrails(input_data):
    config = RailsConfig.from_path(CONFIG_PATH)
    print("Config loaded:", config)

    rails = LLMRails(config)

    messages = [
        {"role": "user", "content": "Hi there. Can you help me with some questions I have about my ABC mobile plan?"},
        {"role": "assistant",
        "content": "Hi! How are you? Is there anything I can help with?"},
        {"role": "user", "content": "yes i'd love some help!"}
    ]
    response = await rails.generate_async(messages=input_data)
    print('response: ', response)
    info = rails.explain()
    print("info: ", info)
    info.print_llm_calls_summary()

    for i, v in enumerate(info.llm_calls):
        print(f"===== The {i} prompt ======")
        print(v.prompt)
        print(v.completion)
        print()
    return response
