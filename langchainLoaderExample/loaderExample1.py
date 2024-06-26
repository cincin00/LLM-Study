# 외부페이지 HTML 정보를 수집하는 예제
from langchain.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup

loader = WebBaseLoader("https://ko.wikipedia.org/wiki/%EB%8C%80%ED%98%95_%EC%96%B8%EC%96%B4_%EB%AA%A8%EB%8D%B8")

data = loader.load()

print(data)