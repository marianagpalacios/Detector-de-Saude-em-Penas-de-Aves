# 🐦 Detector de Saúde em Penas de Aves  

Este projeto é um protótipo de **visão computacional aplicada à biologia**, desenvolvido em Python, que analisa imagens de aves para verificar possíveis **irregularidades nas penas**.  

O sistema utiliza técnicas básicas de **processamento de imagem (OpenCV)** para detectar variações de textura e cor, gerando uma classificação simples entre:  
- Penas saudáveis  
- Penas com pequenas irregularidades  
- Penas com sinais de problemas  

---

## 🚀 Tecnologias utilizadas
- **Python 3.x**  
- [OpenCV](https://opencv.org/) – processamento de imagens  
- [Matplotlib](https://matplotlib.org/) – visualização de imagens  
- [NumPy](https://numpy.org/) – cálculos estatísticos  

---

## 📂 Estrutura do projeto

📁 detector-penas

┣ 📄 detector.py # Script principal

┣ 📄 requirements.txt # Dependências do projeto

┣ 📄 README.md # Documentação

┗ 📂 imagens_teste # Imagens de aves para análise


---

## ⚙️ Como executar

### 1. Clone o repositório
git clone https://github.com/seu-usuario/detector-penas.git
cd detector-penas

### 2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Adicione uma imagem de ave

Coloque uma foto na pasta imagens_teste/

Renomeie para ave.jpg

### 5. Execute o analisador
python detector.py

---

📊 Exemplo de saída

Desvio padrão da textura: 18.45

Classificação: Penas parecem saudáveis

---

🌱 Próximos passos

Adicionar segmentação automática para focar apenas nas penas.

Treinar um modelo de Machine Learning (CNN) com dataset de aves.

Criar interface gráfica simples (ex.: Streamlit) para upload de imagens.

---

📌 Objetivo

Este projeto é experimental e educacional, mostrando como a bioinformática e visão computacional podem ser aplicadas de forma interdisciplinar na análise de saúde animal.
Não deve ser usado como diagnóstico real.







