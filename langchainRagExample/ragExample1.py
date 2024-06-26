# 외부에 존재하는 PDF를 가지고 내용을 분리하여 출력해보는 예제
# @deprecated
#from langchain.document_loaders import PyPDFLoader
# @see https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf/
from langchain_community.document_loaders import PyPDFLoader

# url을 통해서 pdf 정보 가져오기
loader = PyPDFLoader("https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")
pages = loader.load_and_split()
print(pages[0])