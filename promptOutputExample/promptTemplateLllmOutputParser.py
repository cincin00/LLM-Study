from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# ChatModel Def
OPENAI_KEY = ""
chat_model = ChatOpenAI(openai_api_key=OPENAI_KEY) # 기본모델 : text-davinci-003

# Template Def
template = """당신은 쉼표로 구분된 목록을 생성하는 유용한 조수입니다. \
사용자가 카테고리를 전달하면 해당 카테고리에 속하는 5개의 객체를 쉼표로 구분된 목록으로 생성합니다. \
오직 쉼표로 구분된 목록만 반환하고 그 이상은 반환하지 마세요."""
human_template = "{text}"
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("user", human_template)
])

chain = chat_prompt | chat_model
## TODO 나중에 입력하는 방식으로 바꿔보기.
response = chain.invoke({"text": "색깔"})

print(response)