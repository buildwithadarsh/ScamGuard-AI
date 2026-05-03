# 🚨 ScamGuard AI

ScamGuard AI is an intelligent system designed to detect scams, phishing attempts, and fraudulent messages using AI-powered analysis.

It helps users identify potential threats in:

* Emails
* Messages
* CSV / Excel datasets

---

## 🌐 Deployed Application

The application is deployed on Streamlit Cloud:

👉 https://scamguard-ai-buildwithadarsh.streamlit.app/

---

## 🧠 Features

* 🔍 AI-based scam detection
* 📊 Bulk analysis via CSV / Excel upload
* ⚡ Real-time text analysis
* 📈 Confidence scoring & risk classification
* 🧾 Structured output (JSON-based)
* 🎯 Multiple scam categories detection:

  * OTP Fraud
  * Phishing
  * Fake Authority
  * Loan Scams
  * Urgency / Fear Tactics
  * Reward Manipulation

---

## 🏗️ Tech Stack

* Python 3.11
* Streamlit (UI)
* LangChain (LLM orchestration)
* OpenAI (LLM)
* Pandas (data processing)
* Pydantic (structured output validation)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/buildwithadarsh/ScamGuard-AI.git
cd scamguard-ai
```

---

### 2. Create virtual environment

```bash
uv venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

---

### 4. Set environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
LANGSMITH_API_KEY=your_key
```

---

## 🖥️ Run Streamlit App

```bash
PYTHONPATH=. streamlit run app/ui/streamlit_app.py
```

---

## 📂 Project Structure

```
app/
├── services/        # Core business logic
├── utils/           # Helper functions
├── model/           # Pydantic schemas
├── ui/              # Streamlit UI
```

---

## 🧠 How It Works

1. User inputs text or uploads file
2. Data is preprocessed
3. Prompt is generated
4. LLM analyzes the content
5. Structured response is returned
6. Results displayed in UI

---

## ⚠️ Limitations

* LLM-based predictions are probabilistic
* Large files may take time (row-wise processing)
* Requires API key for OpenAI

---

## 🚀 Future Improvements

* Async / parallel processing for large datasets
* Real-time browser extension
* API endpoints for external integrations
* Multi-language support
* Improved UI dashboard

---

## 👤 Author

**Adarsh Gupta**

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!
