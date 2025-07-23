import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import re

# --- Streamlit 초기 설정 ---
st.set_page_config(page_title="Linear Equation Plotter", layout="centered")
st.title("🌞 Linear Equation Visualizer")

st.markdown("📌 예시 식: `2*x + 3*y = 6` 또는 `y = 2*x + 1`")
user_input = st.text_input("💬 방정식을 입력하세요:", "2*x + 3*y = 6")

# --- 수식 자동 보정: 2x → 2*x, -3xy → -3*x*y 등 ---
def insert_multiplication(expr: str) -> str:
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)  # 2x → 2*x
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)  # x2 → x*2
    expr = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', expr)  # xy → x*y
    return expr

processed_input = insert_multiplication(user_input)

# --- 변수 정의 ---
x, y = sp.symbols('x y')

try:
    # 등호로 나누기
    if "=" not in processed_input:
        raise ValueError("❗ 등호(=)가 포함된 식을 입력해주세요.")
    
    lhs_str, rhs_str = processed_input.split('=')
    lhs = sp.sympify(lhs_str)
    rhs = sp.sympify(rhs_str)
    eq = sp.Eq(lhs, rhs)

    # y에 대해 풀기
    result = sp.solve(eq, y)

    if not result:
        st.error("❌ y에 대해 풀 수 없는 식입니다.")
    else:
        y_expr = result[0]
        st.success("✅ y에 대해 푼 결과:")
        st.latex(f"y = {sp.latex(y_expr)}")

        # --- 그래프 그리기 ---
        x_vals = np.linspace(-10, 10, 400)
        y_vals = []

        for val in x_vals:
            try:
                y_val = y_expr.subs(x, val)
                y_vals.append(float(sp.N(y_val)))
            except:
                y_vals.append(np.nan)  # 계산 불가한 경우 공백

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"${sp.latex(eq)}$")
        ax.axhline(0, color='gray', linestyle='--')
        ax.axvline(0, color='gray', linestyle='--')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

except Exception as e:
    st.error(f"⚠️ 에러 발생: {e}")
