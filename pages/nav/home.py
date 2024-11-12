import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_animation(file_path):
    """Carregar a animação Lottie a partir do arquivo JSON"""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {file_path}")
        return None
    except json.JSONDecodeError:
        st.error(f"Erro ao decodificar o arquivo JSON: {file_path}")
        return None

def show_home():
    # Configurar o título da página
    st.title("Bem-vindo ao Sistema de Segmentação de Imagens! 🖼️")

    # Adicionar subtítulo
    st.subheader("Exploração interativa para segmentação de imagens com IA 🔍")

    # Carregar animações
    animation_1 = load_lottie_animation("animaçoes/pagina_inicial1.json")  # Substitua pelo caminho correto do seu arquivo de animação
    animation_2 = load_lottie_animation("animaçoes/animation1.json")  # Substitua pelo caminho correto do seu arquivo de animação

    if animation_1 and animation_2:
        # Configurar layout em colunas
        col1, col2 = st.columns(2)

        # Conteúdo da coluna 1
        with col1:
            st_lottie(animation_1, height=350, width=350, key="animation1")
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Este projeto utiliza técnicas avançadas de aprendizado de máquina para segmentação de imagens, focando em separar áreas de interesse específicas de maneira precisa e eficiente.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Conteúdo da coluna 2
        with col2:
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Com o modelo de segmentação treinado, podemos identificar padrões e destacar áreas específicas em imagens. A segmentação é útil em vários campos, como diagnóstico médico, análise de imagens de satélite e muito mais.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )
            st_lottie(animation_2, height=350, width=350, key="animation2")

        # Adicionar um aviso
        st.markdown(
            """
            <div style='background-color: #d4edda; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #155724;'>Aviso:</h4>
                <p style='color: #155724;'>Este projeto demonstra as capacidades de segmentação de imagens, podendo ser aplicado em várias áreas. A precisão do modelo pode variar conforme os dados de entrada e deve ser utilizado como ferramenta complementar.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Não foi possível carregar as animações.")

if __name__ == "__main__":
    show_home()
