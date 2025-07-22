


import streamlit as st

def bullet_loan(principal, annual_rate, years):
    return principal * (1 + annual_rate) ** years

def annuity_loan(principal, annual_rate, years):
    r = annual_rate / 12
    n = years * 12
    A = principal * (r * (1 + r)**n) / ((1 + r)**n - 1)
    total = A * n
    return total, A

# Sidebar inputs
st.sidebar.title("貸款參數設定")
price_per_ping = st.sidebar.number_input("每坪價格（萬元）", value=60.0)
area = st.sidebar.number_input("購買坪數", value=13)
years = st.sidebar.slider("貸款年數", 1, 30, 6)
annual_rate = st.sidebar.number_input("年利率（%）", value=3.0) / 100
developer_return = st.sidebar.number_input("建商回收金額（萬元）", value=2134.0)

# 計算
principal = price_per_ping * area
bullet_total = bullet_loan(principal, annual_rate, years)
annuity_total, monthly_payment = annuity_loan(principal, annual_rate, years)

# 投資報酬分析
bullet_profit = developer_return - bullet_total
annuity_profit = developer_return - annuity_total
annuity_break_even_months = principal / monthly_payment

# 顯示
st.title("土地貸款試算工具")
st.markdown(f"###  cc本金總額：{principal:.2f} 萬元")

st.subheader(" 複利｜期末一次還本息")
st.write(f"6 年後總還款：{bullet_total:.2f} 萬元")
st.write(f"平均月負擔（僅供參考）：{bullet_total / (years * 12):.2f} 萬元")
st.write(f"預估淨利潤：{bullet_profit:.2f} 萬元")

st.subheader("等額本息｜每月固定還款")
st.write(f"每月應繳：{monthly_payment:.2f} 萬元")
st.write(f"總還款金額：{annuity_total:.2f} 萬元")
st.write(f"預估淨利潤：{annuity_profit:.2f} 萬元")
st.write(f"回本時間：約 {annuity_break_even_months:.1f} 月（{annuity_break_even_months/12:.2f} 年）")

