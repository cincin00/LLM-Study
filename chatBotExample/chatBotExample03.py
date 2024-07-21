# openAI를 활용한 챗봇 예제
# - 메모리 기반으로 응답 받기
# - TODO 기능 오류 다시 확인해보기
#https://colab.research.google.com/drive/1YrmsVYrzcvPaWht-yXPbqthiJvHf78qB?usp=sharing
import sys
sys.path.append('/opt/homebrew/var/www/')
from langChainGptStudy.langchain_const import *
from langchain_core.messages import HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from langchain_community import chat_message_histories
from langchain.memory import ChatMessageHistory

chat = ChatOpenAI(openai_api_key=OPENAI_KEY)   # 기본모델 : gpt-3.5-turbo

chatbotResponse = chat.invoke(
    [
        HumanMessage(
            content="이 문장을 영어에서 한국어로 번역하세요 : I love programming."
        ),
        AIMessage(
            content='나는 프로그래밍을 사랑합니다.₩'
        ),

        HumanMessage(
            content="내가 뭐라고 말했지?"
        )
    ]
)
demo_ephemeral_chat_history = ChatMessageHistory()

demo_ephemeral_chat_history.add_user_message("hi!")

demo_ephemeral_chat_history.add_ai_message("whats up?")

demo_ephemeral_chat_history.messages
print(chatbotResponse)
# conversation = chat_message_histories(llm=chat)
# conversation.run("나의 이름은 무엇이니?")

# print(chatbotResponse.content)