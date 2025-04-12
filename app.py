#run streamlit dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data():
    data = pd.read_csv('data/dummy_data.csv')
    return data

#title display and discription

st.title("Surgiccal Site Infection (SSI) Risk Predictionin Elective C-Section Patients")
st.write("This dashboard predicts risk of SSI")

#load the data
data = load_data()

#showing th epatient data

st.subheader("Patient Data")
st.write(data)

#show distribution of risk using plotly
st.subheader("Risk Distribution")
fig = px.histogram(data, x="Combined_Risk_Score", color="Combined_Risk_Score", title= "Risk Distribution")
st.plotly_chart(fig)

#show Rag Scores using Seaborn
st.subheader("RAG Scores by Category")
plt.figure(figsize=(8, 6))
sns.countplot(x="RAG_Antenatal", data=data, palette="coolwarm")
sns.countplot(x="RAG_Intrapartum", data=data, palette="coolwarm")
st.pyplot()



