import streamlit as st

def show_about():
    st.title("Sobre o Projeto")
    
    st.markdown("""
    🌟 **Visão Geral do Projeto** 🌟
    
    Este projeto foi desenvolvido para **segmentação de imagens** utilizando **redes neurais profundas** (Deep Learning). 
    Nosso modelo é treinado para identificar e classificar **regiões de interesse** em imagens, como **tumores em exames médicos**, com o objetivo de fornecer uma ferramenta precisa e eficiente para análise de imagens em áreas como **saúde** e **diagnóstico médico**.

    🧠 **Tecnologia Utilizada**:
    - **Deep Learning**: Redes neurais convolucionais (CNNs)
    - **TensorFlow & Keras**: Para treinamento e implementação do modelo
    - **Streamlit**: Interface web interativa e fácil de usar
    
    ⚡ **Como Funciona**:
    O modelo segmenta automaticamente as imagens fornecidas, destacando as áreas relevantes, com alta precisão. A solução visa oferecer uma análise mais rápida e acessível para profissionais da saúde, auxiliando no diagnóstico de condições médicas.
    
    📈 **Objetivo do Projeto**:
    - Melhorar a **precisão** dos diagnósticos
    - **Automatizar** a análise de exames médicos
    - Reduzir o **tempo de espera** e **custo** dos exames
    - **Apoiar médicos** na identificação de tumores e outras anomalias
    
    🌱 **Futuro do Projeto**:
    Estamos comprometidos com o aprimoramento contínuo deste modelo, incluindo a expansão da base de dados e o aumento da acurácia para tornar a solução mais robusta e confiável.

    🎯 **Próximos Passos**:
    - Integração com mais tipos de exames médicos
    - Melhoria na interface do usuário
    - Testes e validações com dados reais
    """)

