from nemoguardrails import LLMRails, RailsConfig

CONFIG_PATH = 'src/api/utils/nemo_guardrails/config/config.yml'

async def process_input_with_guardrails(input_data):
    config = RailsConfig.from_path(CONFIG_PATH)
    rails = LLMRails(config)
    response = await rails.generate_async(messages=[{"role": "user", "content": input_data}])
    info = rails.explain()
    print('info: ', info)
    return response
