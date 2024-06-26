# 외부 페이지 HTML 데이터를 수집하고 해당 데이터로 chatGPT로 답변하는 예제
from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# OpenAI Embedding 모델을 이용해서 Chunk를 Embedding 한후 Vector Store에 저장
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
import sys
sys.path.append('/opt/homebrew/var/www/')
from langChainGptStudy.langchain_const import *
from langchain.prompts import PromptTemplate
# GPT-3.5 trurbo를 이용해서 LLM 설정
#from langchain_community.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain_openai import ChatOpenAI

# url을 통해서 pdf 정보 가져오기
loader = WebBaseLoader("https://www.clickn.co.kr/customer/notice")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(data)

vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=OPENAI_KEY)) # text-embedding-ada-002
retriever = vectorstore.as_retriever()

template = """다음과 같은 맥락을 사용하여 마지막 질문에 대답하십시오.
만약 답을 모르면 모른다고만 말하고 답을 지어내려고 하지 마십시오.
답변은 최대 세 문장으로 하고 가능한 한 간결하게 유지하십시오.
항상 '다음 질문이 가능하다.'라고 답변 끝에 말하십시오.
{context}
질문: {question}
도움이 되는 답변:"""

rag_prompt_custom = PromptTemplate.from_template(template)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_KEY)

# RAG chain 설정
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | rag_prompt_custom | llm

answer = rag_chain.invoke("가장 최근 방화벽 교체 일시는?")
print(answer)