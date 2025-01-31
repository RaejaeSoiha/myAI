# myAI - Open Source AI Chatbot

## 🚀 Overview
myAI is a **fully open-source AI chatbot platform** designed to be **better than other than AI in future**. It includes:
- **Backend (FastAPI)** for AI inference
- **Frontend (Streamlit)** for an interactive UI
- **Fine-Tuned LLM (Mistral-7B)** for improved performance
- **Deployment (Docker & Kubernetes)** for scalability
- **CI/CD (GitHub Actions)** for automated testing & deployment

## 📂 Project Structure
```
myai/
│── backend/             # API server (FastAPI)
│── frontend/            # UI (Streamlit)
│── model_training/      # Training scripts
│── deployment/          # Deployment configs (Docker/Kubernetes)
│── .github/workflows/   # CI/CD pipeline
│── README.md
│── .gitignore
```

## 🛠️ Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/myai.git
cd myai
```

### 2️⃣ **Setup Backend (FastAPI)**
```sh
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

### 3️⃣ **Setup Frontend (Streamlit)**
```sh
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Deployment with Docker
```sh
docker build -t myai .
docker run -p 8000:8000 myai
```

## ☁️ Deploying to Kubernetes
```sh
kubectl apply -f k8s.yaml
```

## 📜 License
This project is **100% free & open-source** under the MIT License.
