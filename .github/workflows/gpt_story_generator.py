import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_story_and_prompts(user_input):
    # Step 1: 스토리 생성 프롬프트
    story_prompt = f"""
내가 {user_input}가 되어 미래 어느 시점에서 깨어나는 1인칭 시점 영상을 만들 거야. 몰입감과 스토리텔링에 집중한 장면 구성을 만들어 줘.

구성:
1. 기상 장면 (다리 장면 – 항상 포함)
 • 1인칭 시점, 다리를 [설정 설명] 위에 쭉 뻗고 있음.
 • [의류/신발/맨발 설명] 착용.
 • 근처에 [객체 설명]가 있고, [조명/분위기 설명]이 연출됨.
2. 아침 루틴 장면
 • 1인칭 시점, 손으로 [무언가를 만지거나 사용하는 장면].
 • 주변에는 [환경 설명].
 • (선택) 화면 속 중요한 물체 [객체 설명].
3. 이동/전환 장면
 • 1인칭 시점, [장소 설명]을 지나 이동.
 • 손에는 [무엇을 들고 있는지 설명].
 • [분위기 묘사]로 감정이 강조됨.
4. 핵심 액션 장면
 • 1인칭 시점, [주요 작업 수행].
 • 주변에는 [환경 묘사].
 • [긴장감 또는 집중 요소]가 포함됨.
5. 중간 휴식 장면
 • 1인칭 시점, 손으로 [무언가를 들거나 만지는 모습].
 • [분위기 묘사]로 감정 전달.
 • (선택) [복선 요소] 추가 가능.
6. 두 번째 액션 장면
 • 1인칭 시점, [작업을 더 강렬하게 진행].
 • [환경 또는 상황 변화]가 생김.
7. 마무리 전환 장면
 • 1인칭 시점, [정리하거나 결말로 향하는 움직임].
 • [환경 변화 묘사] 추가.
8. 엔딩 장면
 • 1인칭 시점, [강렬하거나 감정적인 마지막 행동].
 • [의미 있는 오브젝트] 등장.
 • [마지막 감정 또는 반성]이 강조됨.
"""

    story_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": story_prompt}]
    )
    story_text = story_response.choices[0].message.content

    # Step 2: 장면 → 이미지 프롬프트 변환
    convert_prompt = f"""
다음은 1인칭 미래 시점의 8장면 이야기야.  
각 장면을 영어로 시각적으로 묘사 가능한 이미지 생성용 프롬프트로 변환해줘.  
배경, 분위기, 감정, 조명 등을 포함해 영화적 묘사 스타일로 작성해줘.

출력 형식:
장면1: cinematic, first-person view of ..., ...

입력:
{story_text}
"""

    prompt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": convert_prompt}]
    )
    prompt_text = prompt_response.choices[0].message.content

    return story_text, prompt_text
