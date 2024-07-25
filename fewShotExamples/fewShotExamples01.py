from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate

examples = [
    {
        "question": "무하마드 알리와 앨런 튜링 중 누가 더 오래 살았나요?",
        "answer": """
여기서 추가 질문이 필요합니까: 네.
추가 질문: 무하마드 알리가 죽었을 때 몇 살이었나요?
중간 답변: 무하마드 알리는 죽었을 때 74세였습니다.
추가 질문: 앨런 튜링이 죽었을 때 몇 살이었나요?
중간 답변: 앨런 튜링은 죽었을 때 41세였습니다.
그래서 최종 답변은: 무하마드 알리
""",
    },
    {
        "question": "크레이그리스트의 창립자는 언제 태어났나요?",
        "answer": """
여기서 추가 질문이 필요합니까: 네.
추가 질문: 크레이그리스트의 창립자는 누구인가요?
중간 답변: 크레이그리스트는 크레이그 뉴마크에 의해 창립되었습니다.
추가 질문: 크레이그 뉴마크는 언제 태어났나요?
중간 답변: 크레이그 뉴마크는 1952년 12월 6일에 태어났습니다.
그래서 최종 답변은: 1952년 12월 6일
""",
    },
    {
        "question": "조지 워싱턴의 외할아버지는 누구였나요?",
        "answer": """
여기서 추가 질문이 필요합니까: 네.
추가 질문: 조지 워싱턴의 어머니는 누구였나요?
중간 답변: 조지 워싱턴의 어머니는 메리 볼 워싱턴입니다.
추가 질문: 메리 볼 워싱턴의 아버지는 누구였나요?
중간 답변: 메리 볼 워싱턴의 아버지는 조셉 볼입니다.
그래서 최종 답변은: 조셉 볼
""",
    },
    {
        "question": "죠스와 카지노 로얄의 감독은 같은 나라 출신인가요?",
        "answer": """
여기서 추가 질문이 필요합니까: 네.
추가 질문: 죠스의 감독은 누구인가요?
중간 답변: 죠스의 감독은 스티븐 스필버그입니다.
추가 질문: 스티븐 스필버그는 어느 나라 출신인가요?
중간 답변: 미국입니다.
추가 질문: 카지노 로얄의 감독은 누구인가요?
중간 답변: 카지노 로얄의 감독은 마틴 캠벨입니다.
추가 질문: 마틴 캠벨은 어느 나라 출신인가요?
중간 답변: 뉴질랜드입니다.
그래서 최종 답변은: 아니요
""",
    },
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

print(prompt.format(input=" 메리 볼 워싱턴 아버지는 누구였나요?"))