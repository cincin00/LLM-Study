# 예제 텍스트 읽어오기
with open('/opt/homebrew/var/www/langChainGptStudy/documentTransferExample/llm_example_text.txt') as f:
    llm_example_text = f.read()

print(llm_example_text);