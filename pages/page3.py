import streamlit as st

st.set_page_config(page_title="사각형 성질 학습", page_icon="📐")
st.title("📐 사각형의 성질과 분류")

# -----------------------
st.header("📘 [문제 1] 평행사변형의 성질에 대한 복합 문제")

with st.expander("❓ 다음 중 평행사변형의 성질로 옳지 않은 것을 모두 고르세요."):
    q1_options = [
        "① 마주보는 각의 크기가 같다.",
        "② 네 각이 모두 직각이다.",
        "③ 두 쌍의 변이 각각 평행하다.",
        "④ 마주보는 변의 길이가 같다.",
        "⑤ 대각선이 서로를 이등분한다.",
    ]
    selected1 = st.multiselect("선택하세요:", q1_options, key="q1")
    if st.button("채점하기", key="q1_button"):
        wrong = ["② 네 각이 모두 직각이다."]
        if sorted(selected1) == sorted(wrong):
            st.success("정답입니다! 평행사변형은 네 각이 모두 직각일 필요는 없습니다.")
        else:
            st.error("틀렸습니다. 다시 생각해보세요!")

# -----------------------
st.header("📙 [문제 2] 평행사변형이 되기 위한 조건")

with st.expander("❓ 다음 중 사각형이 평행사변형이 되기 위한 조건으로 옳은 것을 모두 고르세요."):
    q2_options = [
        "① 마주보는 각의 크기가 같다.",
        "② 한 쌍의 변이 평행하고 길이가 같다.",
        "③ 두 대각선의 길이가 같다.",
        "④ 두 쌍의 변이 각각 평행하다.",
        "⑤ 두 쌍의 변이 각각 길이가 같다.",
    ]
    selected2 = st.multiselect("선택하세요:", q2_options, key="q2")
    correct = ["① 마주보는 각의 크기가 같다.", "② 한 쌍의 변이 평행하고 길이가 같다.", "④ 두 쌍의 변이 각각 평행하다.", "⑤ 두 쌍의 변이 각각 길이가 같다."]
    if st.button("채점하기", key="q2_button"):
        if sorted(selected2) == sorted(correct):
            st.success("정답입니다! 위 네 가지는 모두 평행사변형이 되는 조건입니다.")
        else:
            st.error("틀렸습니다. 다시 선택해보세요.")

# -----------------------
st.divider()
st.header("🧪 [1] 조건 버튼으로 도형 판별")

col1, col2 = st.columns(2)
with col1:
    a = st.checkbox("A. 네 각이 모두 90도이다.")
    b = st.checkbox("B. 대각선의 길이가 모두 같다.")
with col2:
    c = st.checkbox("C. 네 변의 길이가 모두 같다.")
    d = st.checkbox("D. 대각선이 서로 다른 것을 수직이등분한다.")

result = None
if (a or b) and (c or d):
    result = "정사각형"
elif a or b:
    result = "직사각형"
elif c or d:
    result = "마름모"

if a or b or c or d:
    st.subheader("🧠 도형 판별 결과")
    if result:
        st.success(f"👉 선택한 조건에 해당하는 도형은 **{result}**입니다.")
    else:
        st.warning("❓ 해당 조건에 맞는 도형이 없습니다.")
else:
    st.info("☝️ 위 조건 중 하나 이상을 선택해보세요.")

# -----------------------
st.divider()
st.header("🧭 [2] 대각선 중심 도형 분류 순서도")

st.markdown("🟦 다음 조건을 단계적으로 선택해보면 도형이 무엇인지 알 수 있습니다.")

step1 = st.radio("1️⃣ 대각선이 서로 이등분하나요?", ["선택 안 함", "예", "아니오"], index=0)

if step1 == "예":
    step2 = st.radio("2️⃣ 대각선이 수직인가요?", ["선택 안 함", "예", "아니오"], index=0)
    if step2 == "예":
        step3 = st.radio("3️⃣ 대각선의 길이가 같은가요?", ["선택 안 함", "예", "아니오"], index=0)
        if step3 == "예":
            st.success("➡️ 도형은 **정사각형**입니다.")
        elif step3 == "아니오":
            st.success("➡️ 도형은 **마름모**입니다.")
    elif step2 == "아니오":
        step4 = st.radio("3️⃣ 대각선의 길이가 같은가요?", ["선택 안 함", "예", "아니오"], index=0)
        if step4 == "예":
            st.success("➡️ 도형은 **직사각형**입니다.")
        elif step4 == "아니오":
            st.success("➡️ 도형은 **평행사변형**입니다.")
elif step1 == "아니오":
    step5 = st.radio("2️⃣ 대각선 중 한 쌍만 이등분하는가요?", ["선택 안 함", "예", "아니오"], index=0)
    if step5 == "예":
        st.success("➡️ 도형은 **사다리꼴**일 수 있습니다.")
    elif step5 == "아니오":
        st.success("➡️ 도형은 **일반 사각형**입니다.")

st.divider()
st.caption("© 2025 중학교 2학년 수학 도형 단원 - 복합문항 기반 웹 앱")
