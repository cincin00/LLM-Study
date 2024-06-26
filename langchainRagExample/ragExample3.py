# 외부에 존재하는 PDF를 가지고 내용을 크게 분리하고 더 작게 분리하여 백터 스토어로 저장하는 예제
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

# url을 통해서 pdf 정보 가져오기
loader = PyPDFLoader("https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")
pages = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(pages)

vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=OPENAI_KEY)) # text-embedding-ada-002
retriever = vectorstore.as_retriever()

print(retriever)