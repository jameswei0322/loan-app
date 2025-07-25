


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
developer_return = st.sidebar.number_input("建商賣出金額（萬元）", value=2134.0)

# 計算
principal = price_per_ping * area
bullet_total = bullet_loan(principal, annual_rate, years)
annuity_total, monthly_payment = annuity_loan(principal, annual_rate, years)
bullet_monthly_payment = bullet_total / (years * 12)
bullet_monthly_interest = (bullet_total - principal) / (years * 12)

# 投資報酬分析
bullet_profit = developer_return - bullet_total
annuity_profit = developer_return - annuity_total
monthly_principal = principal / (years * 12)
monthly_interest = monthly_payment - monthly_principal

# 顯示
st.title("土地貸款試算工具")
st.markdown(f"###  本金總額：{principal:.2f} 萬元")

st.subheader(" 複利｜期末一次還本息")
st.write(f"6 年後總還款：{bullet_total:.2f} 萬元")
st.write(f"平均月攤（僅供參考）：{bullet_monthly_payment:.2f} 萬元（其中利息約 {bullet_monthly_interest:.2f} 萬元）")
st.write(f"預估淨利潤：{bullet_profit:.2f} 萬元")

st.subheader("等額本息｜每月固定還款")
st.write(f"每月應繳：{monthly_payment:.2f} 萬元（其中利息約 {monthly_interest:.2f} 萬元）")
st.write(f"總還款金額：{annuity_total:.2f} 萬元")
st.write(f"預估淨利潤：{annuity_profit:.2f} 萬元")


