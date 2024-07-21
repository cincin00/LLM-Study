#from langchain_openai import OpenAIEmbeddings
#import sys
#sys.path.append('/opt/homebrew/var/www/')
# from langChainGptStudy.langchain_const import *

# embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
# embeddings = embeddings_model.embed_documents(['안녕!','빨간색 공','파란색 공','붉은색 공','푸른색 공'])
# print(embeddings)
from langchain.docstore.document import Document
sample_text = ['안녕!','빨간색 공','파란색 공','붉은색 공','푸른색 공']

document = []
for item in range(len(sample_text)):
    page = Document(page_content=sample_text[item])
    document.append(page)

    print(document);
