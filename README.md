
# 🖼️ Projeto de Segmentação de Imagens com Deep Learning 

Bem-vindo ao repositório do projeto de Segmentação de Imagens! 🎉 Este projeto utiliza redes neurais para segmentar imagens e identificar regiões de interesse, como lesões em exames médicos, usando um modelo de deep learning treinado em dados de alta qualidade.

---

## 🌟 Funcionalidades

- **Segmentação Precisa** 🔍: Identificação de áreas específicas em imagens usando redes neurais avançadas.
- **Probabilidades por Classe** 📊: Exibição das classes com maiores probabilidades de detecção.
- **Visualização Intuitiva** 🌈: Mostra a imagem original e a máscara segmentada lado a lado.
- **Compatível com Todos os Sistemas Operacionais** 🖥️🐧🍏: Funcionando no Windows, Linux e macOS sem problemas.

---

## 🛠️ Tecnologias e Bibliotecas

- **Python** 🐍
- **Streamlit** 🌐
- **TensorFlow/Keras** 🤖
- **PIL (Pillow)** 🖼️
- **NumPy** 📐

---

## 🚀 Como Instalar e Executar

> **Pré-requisitos**: Certifique-se de ter o Python 3.10+ instalado.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/thaleson/AI_image_segmentation
   cd nome_do_repositorio
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   - **Windows**: `venv\Scripts\activate`
   - **Linux/Mac**: `source venv/bin/activate`

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Inicie a aplicação Streamlit:**
   ```bash
   streamlit run app.py
   ```

6. **Visualize no Navegador** 🌐: Após iniciar o Streamlit, abra [http://localhost:8501](http://localhost:8501) para acessar a interface.

---

## 📁 Estrutura de Pastas

```plaintext
├── app.py               # Código principal da aplicação Streamlit
├── model/               # Contém o modelo de deep learning (.h5)
├── utils.py             # Funções auxiliares para preprocessamento e pós-processamento
├── color_map.py         # Dicionário de classes e cores
├── assets/              # Imagens e recursos adicionais
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto
```

---

## 🔮 Demonstração

1. **Faça o upload de uma imagem** 📸
2. **Veja o modelo em ação** 🧠
3. **Interprete os resultados** 📈

A aplicação exibe a máscara segmentada ao lado da imagem original, juntamente com as probabilidades de cada classe para melhor interpretação.

---

## ⚠️ Aviso de Precisão

> **Nota:** O modelo possui uma precisão de aproximadamente **71%** devido à limitação de dados de treinamento, mas será aprimorado em futuras atualizações! 🔄

---

## 🎯 Próximos Passos

- **Aprimorar o modelo** com mais dados 📈
- **Ajuste fino** para melhor segmentação em casos clínicos específicos 🩺
- **Melhorar a UI** com Streamlit para uma experiência mais interativa 🖱️

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se tiver ideias para melhorar o projeto, sinta-se à vontade para abrir um PR ou enviar sugestões. 

---

## 📜 Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

