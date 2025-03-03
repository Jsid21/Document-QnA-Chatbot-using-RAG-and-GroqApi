## Document QnA (Indian Railways) ChatBot - using Groq API and RAG-Powered with FAISS & LangChain

> **A smart chatbot that answers queries based on Indian Railways documents using Retrieval-Augmented Generation (RAG).**

---

## 🚀 Features

✅ Uses **Retrieval-Augmented Generation (RAG)** for accurate responses<br>
✅ **FAISS Vector Database** for efficient document retrieval.<br>
✅ **GoogleGenerativeAIEmbeddings** for text vectorization and embedding.<br>
✅ **Groq LLM** for contextfull and accurate response.<br>
✅ **Streamlit-based UI** for easy interaction.<br>
✅ Supports **PDF-based knowledge ingestion**.<br>

---

## 🛠 How It Works

1️⃣ **Loads Indian Railways PDFs** 📄 from the `/data` folder.  
2️⃣ **Splits & embeds text** into FAISS using **GoogleGenerativeAIEmbeddings**.  
3️⃣ **Retrieves relevant content** based on user queries.  
4️⃣ **Passes context to LLM** (`ChatGroq` with `gemma2-9b-it`).  
5️⃣ **Generates an accurate response** using LangChain’s **retrieval chain**.  

---

## 📂 Project Structure

```plaintext
📁 IndianRailwaysChatBot
│── 📂 data/                   # Folder containing Indian Railways PDF documents
│── 📂 .venv/                   # Virtual environment (optional)
│── 📄 app.py                   # Main chatbot application (Streamlit)
│── 📄 requirements.txt         # Required dependencies
│── 📄 .env                     # API keys for Google & Groq
│── 📄 README.md                # Project documentation
```
---

## 🔧 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Jsid21/Document-QnA-Chatbot-using-RAG-and-GroqApi.git
cd Document-QnA-Chatbot-using-RAG-and-GroqApi
```
### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up API Keys**
Create a `.env` file in the root directory and add your API keys:
```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

### **4️⃣ Add Indian Railways Documents**
Place relevant **PDF documents** inside the `/data` folder.

---

## ▶️ Run the Chatbot
```sh
streamlit run app.py
```
