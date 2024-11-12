import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
from PIL import Image
import numpy as np
import tensorflow as tf
import os

# Configuração da página principal
st.set_page_config(page_title="Segmentação de Imagens", page_icon="🖼️")



st.markdown(
    f"""
    <style>
    {open("static/styles.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar animações
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

# Carregar animação


# Função para carregar e aplicar o modelo de segmentação
def segment_image(image):
    """Função que aplica o modelo de segmentação de imagem"""
    # Carregar o modelo
    model = tf.keras.models.load_model(os.path.join('model', 'modelo_compacto.h5'))


    # Pré-processar a imagem
    img_array = np.array(image.resize((256, 256))) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Ajustar formato para (1, 256, 256, 3)

    # Realizar a segmentação
    prediction = model.predict(img_array)

    # Redimensionar a previsão de volta ao tamanho original
    pred_mask = prediction[0] > 0.5  # Se a probabilidade for maior que 0.5, considera como 1

    return pred_mask.astype(np.uint8) * 255  # Retorna a máscara binária

# Menu de navegação
with st.sidebar:
    # Exibir animação
   

    selected = option_menu(
        "Menu", 
        ["Home", "Previsão", "Sobre o Projeto",],
        icons=['house', 'bar-chart', 'info-circle'],
        menu_icon="cast", 
        default_index=0
    )

    # Badges
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between;">
            <div>
                <a href="https://github.com/thaleson" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="mailto:thaleson177@gmail.com" target="_blank">
                    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" width="80" />
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Navegação para as páginas
if selected == "Home":
    from pages.nav import home
    home.show_home()
elif selected == "Previsão":
    from pages.nav import predict
    predict.show_prediction(segment_image)
elif selected == "Sobre o Projeto":
    from pages.nav import about
    about.show_about()
