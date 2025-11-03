import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def carregar_dados():
    return sns.load_dataset("iris")

def tela_inicial():
    st.title("🌸 Bem-vindo à Análise de Dados!")
    st.write("Esta aplicação realiza uma análise simples do famoso conjunto de dados **Iris**.")
    st.write("Clique no botão abaixo para iniciar a análise dos dados.")
    
    if st.button("Iniciar Análise"):
        st.session_state["tela"] = "analise"
        st.rerun()