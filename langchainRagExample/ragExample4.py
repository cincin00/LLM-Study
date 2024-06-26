# 외부에 존재하는 PDF를 가지고 내용을 크게 분리하고 더 작게 분리하여 백터 스토어로 저장한뒤 chatGPT에 참고하여 답변하게 하는 예제
# @deprecated
#from langchain.document_loaders import PyPDFLoader
# @see https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf/
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
loader = PyPDFLoader("https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")
pages = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(pages)

vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=OPENAI_KEY)) # text-embedding-ada-002
retriever = vectorstore.as_retriever()

template = """다음과 같은 맥락을 사용하여 마지막 질문에 대답하십시오.
만약 답을 모르면 모른다고만 말하고 답을 지어내려고 하지 마십시오.
답변은 최대 세 문장으로 하고 가능한 한 간결하게 유지하십시오.
항상 '질문해주셔서 감사합니다!'라고 답변 끝에 말하십시오.
{context}
질문: {question}
도움이 되는 답변:"""

rag_prompt_custom = PromptTemplate.from_template(template)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_KEY)

# RAG chain 설정
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | rag_prompt_custom | llm

answer = rag_chain.invoke("한국 저출산의 원인이 무엇이야?")
print(answer)

answer1 = rag_chain.invoke("저출산을 극복한 나라들은 어디가 있어?")
print(answer1)