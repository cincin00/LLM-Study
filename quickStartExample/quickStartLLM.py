from langchain_openai import OpenAI

OPENAI_KEY = ""

llm = OpenAI(openai_api_key=OPENAI_KEY) # 기본모델 : text-davinci-003

# llm.predict("hello?")
response = llm.invoke("How are you today?")
print(response)
# I am a virtual assistant and do not have the capability to feel emotions. However, thank you for asking. How may I assist you?