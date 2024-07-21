#https://colab.research.google.com/drive/1HP9Gf-YTKMZPGZQoIPurObZd8he-QMtu?usp=sharing

#from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

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

#print(hf)

embedded_query = hf.embed_query("안녕!")
print(len(embedded_query))
print(embedded_query[:5])