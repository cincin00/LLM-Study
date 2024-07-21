from langchain.text_splitter import RecursiveCharacterTextSplitter

# 예제 텍스트 읽어오기
with open('/opt/homebrew/var/www/langChainGptStudy/documentTransferExample/llm_example_text.txt') as f:
    llm_example_text = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap  = 20,
    length_function = len,
    add_start_index = True,
)

texts = text_splitter.create_documents([llm_example_text])
print(texts[0])