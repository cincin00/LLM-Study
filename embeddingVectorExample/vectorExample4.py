from langchain_openai import OpenAIEmbeddings
import sys
sys.path.append('/opt/homebrew/var/www/')
from langChainGptStudy.langchain_const import *
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document

embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
sample_text = ['안녕!','빨간색 공','파란색 공','붉은색 공','푸른색 공']

document = []
for item in range(len(sample_text)):
    page = Document(page_content=sample_text[item])
    document.append(page)

db = Chroma.from_documents(document,embeddings_model)

print(db)