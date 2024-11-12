import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from utils.utils import preprocess_image, decode_segmentation_mask
from utils.color_map import color_map  # Importando o color_map com classes em português

# Carregar o modelo
@st.cache_resource
def load_segmentation_model():
    model = load_model("model/modelo_compacto.h5", compile=False)
    return model

model = load_segmentation_model()

def show_prediction(segment_image):
    st.title("Segmentação de Imagens com CamVid")
    st.write("Faça o upload de uma imagem para realizar a segmentação")

    # Carregar imagem do usuário
    uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])


    st.error("""
    **Aviso:** O modelo acerta 71% das previsões atualmente devido à quantidade limitada de dados utilizados no treinamento. Ele será melhorado com o tempo.
    """)

    if uploaded_file is not None:
        # Converter imagem para o formato necessário
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem Original", use_container_width=True)

        # Botão para gerar previsão de segmentação
        if st.button("Gerar Previsão de Segmentos"):
            with st.spinner("Realizando a previsão..."):
                # Pré-processar a imagem para entrada no modelo
                input_image = preprocess_image(np.array(image), (256, 256))

                # Prever a máscara
                predicted_mask = model.predict(np.expand_dims(input_image, axis=0))
                predicted_mask = np.argmax(predicted_mask[0], axis=-1)

                # Decodificar a máscara para cores
                predicted_colored_mask = decode_segmentation_mask(predicted_mask, color_map)

                # Exibir a máscara original e a prevista lado a lado
                st.subheader("Segmentação Resultante")
                st.image(predicted_colored_mask, caption="Máscara Prevista", use_container_width=True)

                # Exibir a probabilidade para cada classe
                st.subheader("Probabilidades por Classe")
                
                # Calcular as probabilidades para cada classe
                predicted_probabilities = predicted_mask  # Já temos as classes previstas

                class_probabilities = {}
                num_classes = predicted_mask.max() + 1  # Assumindo que a classe máxima é o número total de classes
                
                for c in range(num_classes):
                    # Criar uma máscara booleana para cada classe
                    class_mask = (predicted_mask == c)
                    
                    # Extrair a probabilidade para a classe c
                    class_probabilities_for_pixels = predicted_mask * class_mask
                    
                    # Calcular a média da probabilidade
                    class_probabilities[c] = np.mean(class_probabilities_for_pixels)

                # Ordenar classes por probabilidade
                sorted_classes = sorted(class_probabilities.items(), key=lambda x: x[1], reverse=True)
                
                for class_id, prob in sorted_classes[:3]:
                    class_name = list(color_map.keys())[class_id]  # Obter o nome da classe pelo ID
                    st.write(f"{class_name}: {prob:.2f}%")
