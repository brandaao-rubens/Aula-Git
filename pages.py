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

def tela_analise():
    st.title("📊 Análise de Dados - Iris Dataset")
    df = carregar_dados()
    
    st.write("### Visualização do Dataset")
    st.dataframe(df.head())
    
    st.write("### Estatísticas Descritivas")
    st.write(df.describe())
    
    st.write("### Relação entre comprimento e largura da sépala")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", ax=ax)
    st.pyplot(fig)
    
    st.write("### Distribuição do comprimento da pétala")
    fig, ax = plt.subplots()
    sns.histplot(df["petal_length"], kde=True, bins=15, ax=ax)
    st.pyplot(fig)

    if st.button("Voltar"):
        st.session_state["tela"] = "inicial"
        st.rerun()