# openAI를 활용한 챗봇 예제
#https://colab.research.google.com/drive/1YrmsVYrzcvPaWht-yXPbqthiJvHf78qB?usp=sharing
import sys
sys.path.append('/opt/homebrew/var/www/')
from langChainGptStudy.langchain_const import *
from langchain_core.messages import HumanMessage
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(openai_api_key=OPENAI_KEY)   # 기본모델 : gpt-3.5-turbo
chatbotResponse = chat.invoke(
    [
        HumanMessage(
            content="이 문장을 영어에서 한국어로 번역하세요 : I love programming."
        )
    ]
)
print(chatbotResponse.content)