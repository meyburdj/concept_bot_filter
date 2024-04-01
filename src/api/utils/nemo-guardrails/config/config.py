from nemoguardrails import LLMRails, RailsConfig

CONFIG_PATH = 'src/api/utils/nemo-guardrails/config/config.yml'

def process_input_with_guardrails(input_data):
    config = RailsConfig.from_path(CONFIG_PATH)
    rails = LLMRails(config)

    response = rails.generate(messages=[{
        "role": "user",
        "content": input_data
    }])

    return response['content']
