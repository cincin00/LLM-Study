from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "{input}을 만드는 회사의 좋은 이름은 무엇일까요?"),
    ("user", "{input}")
])