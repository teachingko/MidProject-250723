import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Page Setup ---
st.set_page_config(page_title="1차 함수 학습기", layout="centered")
st.title("📚 1차 함수 그래프와 개념 학습기")
st.markdown("1차 함수는 다음과 같은 형태입니다:  \n**$y = ax + b$**")

# --- Sliders ---
a = st.slider("🔁 기울기 a 값을 조절하세요", -10.0, 10.0, 1.0, 0.1)
b = st.slider("🔁 y절편 b 값을 조절하세요", -10.0, 10.0, 0.0, 0.1)

# --- Show Function ---
st.latex(f"y = {a}x + {b}")

# --- Graph Drawing ---
x_vals = np.linspace(-10, 10, 400)
y_vals = a * x_vals + b

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label=f"$y = {a}x + {b}$", color="blue")
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlim(-10, 10)
ax.set_ylim(-20, 20)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# --- Concept Prompt ---
st.subheader("✏️ 개념 확인: 기울기 절댓값 변화에 따른 그래프의 성질")

st.markdown("""
기울기의 **절댓값이 커질수록** → **Y축에 가까워지고 더 가팔라집니다.**  
기울기의 **절댓값이 작아질수록** → **X축에 가까워지고 더 완만해집니다.**
""")

# --- User Answer Input ---
user_answer = st.text_input(
    "📥 위 내용을 자신만의 문장으로 설명해 보세요:",
    placeholder="예: 기울기 절댓값이 커지면 더 가팔라진다."
)

# --- Define logic conditions ---
wrong_phrases = [
    "절댓값이커질수록x축", "절댓값커지면x축", "기울기커지면x축",  # 잘못된 가팔라짐 개념
    "절댓값이작아질수록y축", "절댓값작아지면y축", "기울기작아지면y축"  # 잘못된 완만함 개념
]

correct_phrases = [
    "절댓값이커질수록y축", "절댓값커지면y축", "가팔라", "기울기크면가팔라", "세로에가까움",
    "절댓값이작아질수록x축", "절댓값작아지면x축", "완만", "기울기작으면완만", "수평에가까움"
]

# --- Logic Evaluation ---
if user_answer and user_answer.strip() != "":
    cleaned = user_answer.lower().replace(" ", "")
    
    if any(w in cleaned for w in wrong_phrases):
        st.error("❌ Think again.")
    elif any(c in cleaned for c in correct_phrases):
        st.success("✅ Yes.")
    else:
        st.warning("🤔 Think a little more.")
