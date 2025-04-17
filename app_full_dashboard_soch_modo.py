
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("nisoplus_full_integrated.csv")

st.set_page_config(page_title="НИСО+: Полный дэшборд", layout="wide")
st.title("📊 НИСО+: Интеграция СОЧ и МОДО по Целям Обучения")

st.markdown("### 🔍 Многоуровневая фильтрация")

year = st.selectbox("Учебный год", sorted(df["Учебный год"].unique()))
df = df[df["Учебный год"] == year]

region = st.selectbox("Область", sorted(df["Область"].unique()))
df = df[df["Область"] == region]

district = st.selectbox("Район", sorted(df["Район"].unique()))
df = df[df["Район"] == district]

school = st.selectbox("Школа", sorted(df["Школа"].unique()))
df = df[df["Школа"] == school]

grade = st.selectbox("Класс", sorted(df["Класс"].unique()))
df = df[df["Класс"] == grade]

subject = st.selectbox("Предмет", sorted(df["Предмет"].unique()))
df = df[df["Предмет"] == subject]

goal = st.selectbox("Цель обучения", sorted(df["Цель обучения"].unique()))
df_goal = df[df["Цель обучения"] == goal]

st.markdown("### 📈 Сравнение результатов СОЧ и МОДО")
fig = px.bar(df_goal, x="Ученик", y=["СОЧ (%)", "МОДО (%)"],
             barmode="group", text_auto=True,
             title=f"Цель: {goal}")
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 📋 Таблица по дескрипторам и аналитике")
columns_to_show = [
    "Ученик", "Раздел", "Подраздел", "Критерий оценивания", "Дескриптор",
    "СОЧ (%)", "МОДО (%)", "Отклонение", "Аналитика", "Обратная связь"
]

for col in columns_to_show:
    if col not in df_goal.columns:
        st.error(f"Отсутствует столбец: {col}")

styled = df_goal[columns_to_show].sort_values("СОЧ (%)", ascending=False)
styled = df_goal[columns_to_show].sort_values("СОЧ (%)", ascending=False)
st.dataframe(styled, use_container_width=True)
