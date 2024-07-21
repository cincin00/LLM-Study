# 로컬 임베딩 저장 후 임베딩 처리한 데이터를 호출하는 예제
#https://colab.research.google.com/drive/1HP9Gf-YTKMZPGZQoIPurObZd8he-QMtu?usp=sharing

#from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma

#model_name = "sentence-transformers/all-mpnet-base-v2"
#model_name = "BAAI/bge-large-en-v1.5"  # (2023.11.16 기준 공개모델 중 LeaderBoard 1위 모델)
model_name = "jhgan/ko-sroberta-multitask" # (KorNLU 데이터셋에 학습시킨 한국어 임베딩 모델)
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

sample_texts = [
        "의자",
        "식탁",
        "침대",
        "세탁기",
        "냉장고"
]

documents =  []
for item in range(len(sample_texts)):
    page = Document(page_content=sample_texts[item])
    documents.append(page)

#print(documents)

# #db.delete_collection()  # Collection 삭제
db = Chroma.from_documents(documents, hf)

#print(db)

query = "잠자기"
docs = db.similarity_search_with_score(query)
print(docs[0])