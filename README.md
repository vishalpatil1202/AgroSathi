# 🌾 AgroSathi - Bridging Farmers and Government Support

_AgroSathi_ is an AI-powered farmer support tool that helps farmers discover relevant **government schemes, subsidies, and crop insurance** based on their age, land type/size, state, and crops sown.

This project is submitted as part of the [Google Gemma 3N Hackathon](https://www.kaggle.com/competitions/google-gemma-3n-hackathon).

---

## 🧠 Powered by Google Gemma 2B (Instruction-Tuned)

The tool uses the `google/gemma-1.1-2b-it` model to analyze farmer input and generate scheme recommendations in their preferred language.

---

## 🎯 Features

✅ Multilingual UI (supports 9 Indian languages)  
✅ Dynamic form for farmer details  
✅ Streamlit-based frontend  
✅ Colab notebook for reproducibility  
✅ Uses Gemma 2B LLM to recommend real-world applicable schemes  
✅ Lightweight and ready-to-deploy

---

## 🖼️ Demo

[📺 Watch the 2-minute demo video here](https://your-video-link.com)  
(*Replace with actual video link*)

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

Open the AgroSathi.ipynb notebook to try out the model interaction directly on Colab.
Make sure to install required packages and enable GPU (recommended).

---

## 📦 Model Used

- Model Name: google/gemma-1.1-2b-it
- Hugging Face Link: https://huggingface.co/google/gemma-1.1-2b-it
