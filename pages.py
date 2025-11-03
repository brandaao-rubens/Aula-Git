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