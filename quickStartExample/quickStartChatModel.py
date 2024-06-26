from langchain_openai import ChatOpenAI

OPENAI_KEY = ""

chat_model = ChatOpenAI(openai_api_key=OPENAI_KEY) # 기본모델 : text-davinci-003

# Deprecated Method
# llm.predict("hello?")
response = chat_model.invoke("How are you today?")
print(response)
# content="I'm just a computer program, so I don't have feelings, but I'm here and ready to help you with anything you need. How can I assist you today?" response_metadata={'token_usage': {'completion_tokens': 35, 'prompt_tokens': 12, 'total_tokens': 47}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-782aee8b-79f5-4746-a76f-78032d7af7c9-0' usage_metadata={'input_tokens': 12, 'output_tokens': 35, 'total_tokens': 47}