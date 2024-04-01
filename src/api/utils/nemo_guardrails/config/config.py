import asyncio
from nemoguardrails import LLMRails, RailsConfig

CONFIG_PATH = 'src/api/utils/nemo_guardrails/config/config.yml'

# Async function to process input with guardrails
async def process_input_with_guardrails(input_data):
    config = RailsConfig.from_path(CONFIG_PATH)
    rails = LLMRails(config)
    
    response = await rails.generate(messages=[{
        "role": "user",
        "content": input_data
    }])

    return response['content']

# Synchronous wrapper for the async function
def process_request(input_data):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(process_input_with_guardrails(input_data))
