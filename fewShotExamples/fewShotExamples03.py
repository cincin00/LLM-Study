from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings
import sys
sys.path.append('/opt/homebrew/var/www/')
from langChainGptStudy.langchain_const import *

examples = [
    {
        "question": "오늘의 날씨는 어떤가요?",
        "answer": """
여기서 추가 질문이 필요합니까: 네.
추가 질문: 이번주 평균 온도는 어때요?
중간 답변: 이번주 평균 온도는 26도입니다..
추가 질문: 이번주 평균 습도는 몇 %인가요?
중간 답변: 이번주 평균 습도는 26% 입니다..
그래서 최종 답변은: 오늘의 날씨는 26도이고 습도는 26% 정도 될것으로 예상됩니다.
""",
    },
    {
        "question": "금요일에 비가 올까요?",
        "answer": """
여기서 추가 질문이 필요합니까: 네.
추가 질문: 지난달에 평균적으로 비가 많이 왔나요?
중간 답변: 지난달에는 평균적으로 20일 동안 비가 내렸습니다..
추가 질문: 지난달에 금요일마다 비가 왔나요?
중간 답변: 지난달에 금요일은 모두 비가 왔습니다.
그래서 최종 답변은: 금요일에 비가 올 확률이 높습니다.
""",
    },
#     {
#         "question": "조지 워싱턴의 외할아버지는 누구였나요?",
#         "answer": """
# 여기서 추가 질문이 필요합니까: 네.
# 추가 질문: 조지 워싱턴의 어머니는 누구였나요?
# 중간 답변: 조지 워싱턴의 어머니는 메리 볼 워싱턴입니다.
# 추가 질문: 메리 볼 워싱턴의 아버지는 누구였나요?
# 중간 답변: 메리 볼 워싱턴의 아버지는 조셉 볼입니다.
# 그래서 최종 답변은: 조셉 볼
# """,
#     },
#     {
#         "question": "죠스와 카지노 로얄의 감독은 같은 나라 출신인가요?",
#         "answer": """
# 여기서 추가 질문이 필요합니까: 네.
# 추가 질문: 죠스의 감독은 누구인가요?
# 중간 답변: 죠스의 감독은 스티븐 스필버그입니다.
# 추가 질문: 스티븐 스필버그는 어느 나라 출신인가요?
# 중간 답변: 미국입니다.
# 추가 질문: 카지노 로얄의 감독은 누구인가요?
# 중간 답변: 카지노 로얄의 감독은 마틴 캠벨입니다.
# 추가 질문: 마틴 캠벨은 어느 나라 출신인가요?
# 중간 답변: 뉴질랜드입니다.
# 그래서 최종 답변은: 아니요
# """,
#     },
]

example_prompt = PromptTemplate(
    input_variables=["question", "answer"], template="Question: {question}\n{answer}"
)

#print(example_prompt.format(**examples[0]))

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)


example_selector = SemanticSimilarityExampleSelector.from_examples(
    # This is the list of examples available to select from.
    examples,
    # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
    OpenAIEmbeddings(openai_api_key=OPENAI_KEY),
    # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
    Chroma,
    # This is the number of examples to produce.
    k=1,
)

# Select the most similar example to the input.
question = "수요일에 비가 올까요?"
selected_examples = example_selector.select_examples({"question": question})
print(f"입력과 유사한 답변: {question}")
for example in selected_examples:
    print("\n")
    for k, v in example.items():
        print(f"{k}: {v}")