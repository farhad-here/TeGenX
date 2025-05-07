# 🧠 TeGenX: Lightweight Text Generation Web App
### TeGenX is a lightweight, browser-based text generation application built with Streamlit. It enables users to generate English and Persian text using various pre-trained language models from Hugging Face. The app is designed for simplicity, speed, and flexibility, making it suitable for both experimentation and quick content generation.
---
# 🚀 Features
### Multilingual Support: Generate text in English and Persian.

### Model Selection: Choose from various pre-trained models based on your requirements.

### Interactive Interface: User-friendly Streamlit interface for seamless interaction.

### Customizable Parameters: Adjust generation parameters like temperature, top-k, and top-p.
- Interactive web interface using Streamlit

- Support for multiple language models:

- English: EleutherAI/gpt-neo-125m, distilgpt2, gpt2-medium

- Persian: HooshvareLab/gpt2-fa

- Customizable generation parameters
---
# 🧠 Available Models

| Model | Size | Description | Usage |
|-------|------|-------------|--------|
| **EleutherAI/gpt-neo-125m** | ~500MB | Lightweight GPT-Neo model | Fast inference |
| **distilgpt2** | ~300MB | Distilled GPT-2 | Low-resource systems |
| **gpt2-medium** | ~1.5GB | Medium GPT-2 | High quality generation |
| **HooshvareLab/gpt2-fa** | ~485MB | Persian GPT-2 model | Persian text generation |


### English Models


  
#### 1. EleutherAI/gpt-neo-125m

**Size**: ~500MB

**Description**: A lightweight GPT-Neo model suitable for general English text generation.

**Usage**: Ideal for applications requiring faster inference with reasonable performance.

#### 2. distilgpt2

**Size**: ~300MB

**Description**: A distilled version of GPT-2, offering a balance between speed and performance.

**Usage**: Suitable for applications where computational resources are limited.

#### 3.gpt2-medium

**Size**: ~1.5GB

**Description**: A medium-sized GPT-2 model providing improved performance over smaller variants.

**Usage**: Recommended for applications requiring higher quality text generation.





### Persian Model


  
#### HooshvareLab/gpt2-fa

Size: ~485MB

Description: A GPT-2 model fine-tuned for Persian language text generation.

Usage: Best suited for generating coherent Persian text.

Download: <a href="https://huggingface.co/HooshvareLab/gpt2-fa">Available on Hugging Face</a>

---

# 🛠 Installation
1.**Clone the Repository**

```bash

git clone https://github.com/yourusername/tegenx.git
cd tegenx

```
2.**Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
3.**Install Dependencies**

```bash
pip install -r requirements.txt

```

---

#🎮 Usage
#### *Run the Application*

```bash
streamlit run app.py

```
#### *2.Interact with the Interface*

- Enter your prompt in the input box.

- Select the desired model for text generation.

- View the generated text displayed below.

---

# 📁 Model Management
#### All models are automatically downloaded and cached by Hugging Face's Transformers library upon first use. Ensure you have a stable internet connection during the initial download.

---

# 📝 Notes

- Performance: Larger models like gpt2-medium may require more memory and computational power.
  
- Customization: You can modify generation parameters in the code to better suit your application's needs.

- Extensibility: The application is designed to be easily extendable with additional models or features.

