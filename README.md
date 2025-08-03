# 🌾 AgroSathi - Bridging Farmers and Government Support

_AgroSathi_ is an AI-powered farmer support tool that helps farmers discover relevant **government schemes, subsidies, and crop insurance** based on their age, land type/size, state, and crops sown.

This project is submitted as part of the [Google Gemma 3N Hackathon](https://www.kaggle.com/competitions/google-gemma-3n-hackathon).

---

## 🧠 Powered by Google Gemma

The tool uses the `google/gemma-1.1-2b-it` model to analyze farmer input and generate scheme recommendations in their preferred language.

---

## 🎯 Features

✅ Multilingual UI (supports 9 Indian languages)  
✅ Dynamic form for farmer details  
✅ Streamlit-based frontend  
✅ Colab notebook for reproducibility  
✅ Uses Gemma LLM to recommend real-world applicable schemes

---

## 🛠️ Tech Stack

- **Python 3.10**
- **Streamlit**
- **Google Colab**
- **Transformers (HuggingFace)**
- **Gemma 1.1 2B-Instruct**
- **Torch**

---

## 📂 Project Structure

```

AgroSathi/
├── streamlit_app/
│ ├── app.py # Streamlit frontend
│ ├── gemma.py # Gemma model loading and response generation
│ └── requirements.txt # Dependencies
├── AgroSathi.ipynb # Google colab notebook
├── .gitignore
└── README.md

```

---

## 🚀 Run Locally (Streamlit App)

```bash
# 1. Clone the repository
git clone https://github.com/vishalpatil1202/AgroSathi
cd agrosathi/streamlit_app

# 2. Create virtual environment and activate (optional)
python -m venv venv
.\venv\Scripts\activate  

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py

 ```

---

## 📒 Run on Google Colab

You can try the AI-powered recommendation system directly in a Colab notebook.
However, to run the full Streamlit app via Colab, follow these instructions carefully:

- Open AgroSathi.ipynb in Google Colab
- Upload the app.py and gemma.py files into the Colab runtime
- Add ngrok and Hugging Face token
- Run the notebook cells to launch the app, it will provide a public URL (via ngrok) to access the UI.

---

## 📦 Model Used

- Model Name: google/gemma-1.1-2b-it
- Hugging Face Link: https://huggingface.co/google/gemma-1.1-2b-it
