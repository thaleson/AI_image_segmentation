import numpy as np
import cv2

def preprocess_image(image, target_size):
    """
    Redimensiona a imagem e a normaliza para o modelo.
    """
    image = cv2.resize(image, target_size)
    image = image / 255.0  # Normalizar
    return image

def decode_segmentation_mask(mask, color_map):
    """
    Converte a máscara de classes predita em uma máscara colorida.
    """
    height, width = mask.shape
    color_mask = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Para cada classe, atribuímos a cor correspondente
    for class_index, class_name in enumerate(color_map.keys()):
        color = color_map[class_name]
        color_mask[mask == class_index] = color
    
    return color_mask
