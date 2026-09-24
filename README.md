# 🤖 AI Health Assistant
a
### 🏋️ AI-Powered Health & Nutrition Recommendation System

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green)](https://www.langchain.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-orange)](https://github.com/facebookresearch/faiss)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-LLM-yellow?logo=huggingface\&logoColor=black)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

> **AI Health Assistant** is a beginner-friendly AI-powered health and nutrition application built with **Python and Streamlit**. It combines health calculations, nutrition knowledge, **Retrieval-Augmented Generation (RAG)**, FAISS vector search, and a Hugging Face language model to provide personalized wellness and diet-related information.

---

## 🌟 Overview

AI Health Assistant allows users to enter basic health information and receive useful nutrition and wellness recommendations.

The application calculates:

* ⚖️ BMI
* 🔥 BMR
* ⚡ TDEE
* 🎯 Daily Calorie Target

It also provides:

* 🥗 Personalized diet recommendations
* 🤖 AI-powered health assistance
* 🔎 Nutrition knowledge search
* 📚 RAG-based responses
* 🧠 FAISS vector database
* 🤗 Hugging Face LLM integration

---

## ✨ Features

### 🧮 Health Calculations

The application calculates important health and energy metrics:

| Feature           | Description                                   |
| ----------------- | --------------------------------------------- |
| ⚖️ BMI            | Estimates Body Mass Index                     |
| 🔥 BMR            | Estimates Basal Metabolic Rate                |
| ⚡ TDEE            | Estimates Total Daily Energy Expenditure      |
| 🎯 Calorie Target | Estimates calories based on the selected goal |

### 🥗 Diet Recommendation

Users can provide:

* Age
* Gender
* Weight
* Height
* Activity level
* Fitness goal
* Diet type
* Food allergies

The AI then creates a simple daily meal recommendation.

### 🤖 AI Health Assistance

Users can ask nutrition-related questions such as:

```text
What foods are good sources of fiber?
```

The application searches the nutrition knowledge base and uses the retrieved information to generate an AI response.

### 🔎 RAG System

Instead of relying only on the language model, the application retrieves relevant information from a nutrition knowledge base before generating the response.

---

# 🧠 How RAG Works

The application follows this workflow:

```text
             Nutrition PDF
                   │
                   ▼
          Document Loading
                   │
                   ▼
             Text Splitting
                   │
                   ▼
              Embeddings
                   │
                   ▼
          FAISS Vector Database
                   │
                   ▼
            Similarity Search
                   │
                   ▼
          Relevant Information
                   │
                   ▼
          Hugging Face LLM
                   │
                   ▼
             AI Response
```

This approach is called **Retrieval-Augmented Generation (RAG)**.

---

# 🏗️ Application Architecture

```text
┌──────────────────────────────┐
│        Streamlit UI          │
│                              │
│  User Health Information     │
│  Health Questions            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Python Application      │
│                              │
│ BMI │ BMR │ TDEE │ Calories │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          RAG System          │
│                              │
│ LangChain + FAISS + PDF      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Hugging Face LLM       │
│                              │
│     AI Response Generation   │
└──────────────────────────────┘
```

---

# 🛠️ Tech Stack

| Technology               | Purpose                          |
| ------------------------ | -------------------------------- |
| 🐍 Python                | Core programming language        |
| 🎈 Streamlit             | Web application interface        |
| 🦜 LangChain             | RAG application framework        |
| 🧠 FAISS                 | Vector similarity search         |
| 🤗 Hugging Face          | Language model                   |
| 🔤 Sentence Transformers | Text embeddings                  |
| 📄 PyPDF                 | PDF document processing          |
| 🔑 python-dotenv         | Environment variable management  |
| 💬 OpenAI SDK            | Communication with the model API |

---

# 📂 Project Structure

```text
ai-health-assistant/
│
├── app.py
├── diet.py
├── rag.py
├── create_database.py
├── README.md
├── LICENSE
├── .gitignore
│
└── data/
    └── nutrition.pdf
```

### File Description

| File                 | Purpose                                                  |
| -------------------- | -------------------------------------------------------- |
| `app.py`             | Main Streamlit application                               |
| `diet.py`            | BMI, BMR, TDEE and calorie calculations                  |
| `rag.py`             | RAG and FAISS functionality                              |
| `create_database.py` | Creates the vector database                              |
| `nutrition.pdf`      | Nutrition knowledge source                               |
| `.env`               | Stores API credentials locally                           |
| `.gitignore`         | Prevents sensitive/unnecessary files from being uploaded |
| `LICENSE`            | MIT License                                              |

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-health-assistant.git
```

## 2️⃣ Open the Project

```bash
cd ai-health-assistant
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv env
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
env\Scripts\activate
```

### macOS / Linux

```bash
source env/bin/activate
```

---

# 📦 Install Dependencies

Install the required Python packages:

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-huggingface
pip install faiss-cpu
pip install sentence-transformers
pip install pypdf
pip install openai
pip install python-dotenv
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token
```

### ⚠️ Security

**Never upload `.env` to GitHub.**

The `.gitignore` file should contain:

```gitignore
.env
env/
__pycache__/
*.pyc
```

Never expose your Hugging Face API token publicly.

---

# 🗃️ Create the Vector Database

After adding the nutrition PDF, run:

```bash
python create_database.py
```

This processes the nutrition document and creates the FAISS vector database used by the RAG system.

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 💡 Example Questions

You can ask questions such as:

```text
What foods are good sources of fiber?
```

```text
What are some vegetarian sources of protein?
```

```text
What are healthy whole grain foods?
```

```text
What foods contain healthy fats?
```

---

# 📊 Example Workflow

```text
Enter Personal Information
          ↓
Select Activity Level
          ↓
Select Health Goal
          ↓
Select Diet Type
          ↓
Add Food Allergies
          ↓
Calculate BMI / BMR / TDEE
          ↓
Generate Diet Recommendation
          ↓
Ask Nutrition Questions
          ↓
Receive AI Response
```

---

# 🔒 Security

This project uses environment variables for API authentication.

Sensitive files should remain local:

```text
.env
env/
```

These files should **never** be committed to the public repository.



# 🚀 Future Improvements

Some planned improvements include:

* 👤 User authentication
* 📈 Health progress tracking
* 🍱 Larger food database
* 🧮 More nutrition calculations
* 📱 Mobile-friendly interface
* 🗄️ Database integration
* 💬 Improved AI conversations
* 📊 Nutrition charts
* 🥘 Personalized meal plans
* ☁️ Cloud deployment
* 🔔 Health and meal reminders

---

# 🎯 Learning Outcomes

This project helped explore:

* Python programming
* Streamlit application development
* Functions and modules
* API integration
* Environment variables
* Large Language Models
* Prompt engineering
* LangChain
* Retrieval-Augmented Generation
* Vector databases
* FAISS similarity search
* Embeddings
* PDF document processing
* Git and GitHub

---

# 👨‍💻 Author

## Aryan Gill

Python Developer | AI & ML Learner

🐙 GitHub:
https://github.com/pythonwitharyan

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

# 💖 Made With

**Python 🐍 + Streamlit 🎈 + AI 🤖**

### Built for learning, experimentation and exploring AI-powered applications.
# 🤖 AI Health Assistant

### 🏋️ AI-Powered Health & Nutrition Recommendation System

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green)](https://www.langchain.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-orange)](https://github.com/facebookresearch/faiss)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-LLM-yellow?logo=huggingface\&logoColor=black)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

> **AI Health Assistant** is a beginner-friendly AI-powered health and nutrition application built with **Python and Streamlit**. It combines health calculations, nutrition knowledge, **Retrieval-Augmented Generation (RAG)**, FAISS vector search, and a Hugging Face language model to provide personalized wellness and diet-related information.

---

## 🌟 Overview

AI Health Assistant allows users to enter basic health information and receive useful nutrition and wellness recommendations.

The application calculates:

* ⚖️ BMI
* 🔥 BMR
* ⚡ TDEE
* 🎯 Daily Calorie Target

It also provides:

* 🥗 Personalized diet recommendations
* 🤖 AI-powered health assistance
* 🔎 Nutrition knowledge search
* 📚 RAG-based responses
* 🧠 FAISS vector database
* 🤗 Hugging Face LLM integration

---

## ✨ Features

### 🧮 Health Calculations

The application calculates important health and energy metrics:

| Feature           | Description                                   |
| ----------------- | --------------------------------------------- |
| ⚖️ BMI            | Estimates Body Mass Index                     |
| 🔥 BMR            | Estimates Basal Metabolic Rate                |
| ⚡ TDEE            | Estimates Total Daily Energy Expenditure      |
| 🎯 Calorie Target | Estimates calories based on the selected goal |

### 🥗 Diet Recommendation

Users can provide:

* Age
* Gender
* Weight
* Height
* Activity level
* Fitness goal
* Diet type
* Food allergies

The AI then creates a simple daily meal recommendation.

### 🤖 AI Health Assistance

Users can ask nutrition-related questions such as:

```text
What foods are good sources of fiber?
```

The application searches the nutrition knowledge base and uses the retrieved information to generate an AI response.

### 🔎 RAG System

Instead of relying only on the language model, the application retrieves relevant information from a nutrition knowledge base before generating the response.

---

# 🧠 How RAG Works

The application follows this workflow:

```text
             Nutrition PDF
                   │
                   ▼
          Document Loading
                   │
                   ▼
             Text Splitting
                   │
                   ▼
              Embeddings
                   │
                   ▼
          FAISS Vector Database
                   │
                   ▼
            Similarity Search
                   │
                   ▼
          Relevant Information
                   │
                   ▼
          Hugging Face LLM
                   │
                   ▼
             AI Response
```

This approach is called **Retrieval-Augmented Generation (RAG)**.

---

# 🏗️ Application Architecture

```text
┌──────────────────────────────┐
│        Streamlit UI          │
│                              │
│  User Health Information     │
│  Health Questions            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Python Application      │
│                              │
│ BMI │ BMR │ TDEE │ Calories │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          RAG System          │
│                              │
│ LangChain + FAISS + PDF      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Hugging Face LLM       │
│                              │
│     AI Response Generation   │
└──────────────────────────────┘
```

---

# 🛠️ Tech Stack

| Technology               | Purpose                          |
| ------------------------ | -------------------------------- |
| 🐍 Python                | Core programming language        |
| 🎈 Streamlit             | Web application interface        |
| 🦜 LangChain             | RAG application framework        |
| 🧠 FAISS                 | Vector similarity search         |
| 🤗 Hugging Face          | Language model                   |
| 🔤 Sentence Transformers | Text embeddings                  |
| 📄 PyPDF                 | PDF document processing          |
| 🔑 python-dotenv         | Environment variable management  |
| 💬 OpenAI SDK            | Communication with the model API |

---

# 📂 Project Structure

```text
ai-health-assistant/
│
├── app.py
├── diet.py
├── rag.py
├── create_database.py
├── README.md
├── LICENSE
├── .gitignore
│
└── data/
    └── nutrition.pdf
```

### File Description

| File                 | Purpose                                                  |
| -------------------- | -------------------------------------------------------- |
| `app.py`             | Main Streamlit application                               |
| `diet.py`            | BMI, BMR, TDEE and calorie calculations                  |
| `rag.py`             | RAG and FAISS functionality                              |
| `create_database.py` | Creates the vector database                              |
| `nutrition.pdf`      | Nutrition knowledge source                               |
| `.env`               | Stores API credentials locally                           |
| `.gitignore`         | Prevents sensitive/unnecessary files from being uploaded |
| `LICENSE`            | MIT License                                              |

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-health-assistant.git
```

## 2️⃣ Open the Project

```bash
cd ai-health-assistant
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv env
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
env\Scripts\activate
```

### macOS / Linux

```bash
source env/bin/activate
```

---

# 📦 Install Dependencies

Install the required Python packages:

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-huggingface
pip install faiss-cpu
pip install sentence-transformers
pip install pypdf
pip install openai
pip install python-dotenv
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token
```

### ⚠️ Security

**Never upload `.env` to GitHub.**

The `.gitignore` file should contain:

```gitignore
.env
env/
__pycache__/
*.pyc
```

Never expose your Hugging Face API token publicly.

---

# 🗃️ Create the Vector Database

After adding the nutrition PDF, run:

```bash
python create_database.py
```

This processes the nutrition document and creates the FAISS vector database used by the RAG system.

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 💡 Example Questions

You can ask questions such as:

```text
What foods are good sources of fiber?
```

```text
What are some vegetarian sources of protein?
```

```text
What are healthy whole grain foods?
```

```text
What foods contain healthy fats?
```

---

# 📊 Example Workflow

```text
Enter Personal Information
          ↓
Select Activity Level
          ↓
Select Health Goal
          ↓
Select Diet Type
          ↓
Add Food Allergies
          ↓
Calculate BMI / BMR / TDEE
          ↓
Generate Diet Recommendation
          ↓
Ask Nutrition Questions
          ↓
Receive AI Response
```

---

# 🔒 Security

This project uses environment variables for API authentication.

Sensitive files should remain local:

```text
.env
env/
```

These files should **never** be committed to the public repository.

---

# ⚠️ Disclaimer

This application is designed for **educational and general wellness purposes only**.

The calculations and AI-generated recommendations should not be considered medical diagnosis, treatment, or professional medical advice.

For medical conditions, serious symptoms, allergies, or personalized medical guidance, consult a qualified healthcare professional.

---

# 🚀 Future Improvements

Some planned improvements include:

* 👤 User authentication
* 📈 Health progress tracking
* 🍱 Larger food database
* 🧮 More nutrition calculations
* 📱 Mobile-friendly interface
* 🗄️ Database integration
* 💬 Improved AI conversations
* 📊 Nutrition charts
* 🥘 Personalized meal plans
* ☁️ Cloud deployment
* 🔔 Health and meal reminders

---

# 🎯 Learning Outcomes

This project helped explore:

* Python programming
* Streamlit application development
* Functions and modules
* API integration
* Environment variables
* Large Language Models
* Prompt engineering
* LangChain
* Retrieval-Augmented Generation
* Vector databases
* FAISS similarity search
* Embeddings
* PDF document processing
* Git and GitHub

---

# 👨‍💻 Author

## Aryan Gill

Python Developer | AI & ML Learner

🐙 GitHub:
https://github.com/pythonwitharyan

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

# 💖 Made With

**Python 🐍 + Streamlit 🎈 + AI 🤖**

### Built for learning, experimentation and exploring AI-powered applications.
# 🤖 AI Health Assistant

### 🏋️ AI-Powered Health & Nutrition Recommendation System

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green)](https://www.langchain.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-orange)](https://github.com/facebookresearch/faiss)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-LLM-yellow?logo=huggingface\&logoColor=black)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

> **AI Health Assistant** is a beginner-friendly AI-powered health and nutrition application built with **Python and Streamlit**. It combines health calculations, nutrition knowledge, **Retrieval-Augmented Generation (RAG)**, FAISS vector search, and a Hugging Face language model to provide personalized wellness and diet-related information.

---

## 🌟 Overview

AI Health Assistant allows users to enter basic health information and receive useful nutrition and wellness recommendations.

The application calculates:

* ⚖️ BMI
* 🔥 BMR
* ⚡ TDEE
* 🎯 Daily Calorie Target

It also provides:

* 🥗 Personalized diet recommendations
* 🤖 AI-powered health assistance
* 🔎 Nutrition knowledge search
* 📚 RAG-based responses
* 🧠 FAISS vector database
* 🤗 Hugging Face LLM integration

---

## ✨ Features

### 🧮 Health Calculations

The application calculates important health and energy metrics:

| Feature           | Description                                   |
| ----------------- | --------------------------------------------- |
| ⚖️ BMI            | Estimates Body Mass Index                     |
| 🔥 BMR            | Estimates Basal Metabolic Rate                |
| ⚡ TDEE            | Estimates Total Daily Energy Expenditure      |
| 🎯 Calorie Target | Estimates calories based on the selected goal |

### 🥗 Diet Recommendation

Users can provide:

* Age
* Gender
* Weight
* Height
* Activity level
* Fitness goal
* Diet type
* Food allergies

The AI then creates a simple daily meal recommendation.

### 🤖 AI Health Assistance

Users can ask nutrition-related questions such as:

```text
What foods are good sources of fiber?
```

The application searches the nutrition knowledge base and uses the retrieved information to generate an AI response.

### 🔎 RAG System

Instead of relying only on the language model, the application retrieves relevant information from a nutrition knowledge base before generating the response.

---

# 🧠 How RAG Works

The application follows this workflow:

```text
             Nutrition PDF
                   │
                   ▼
          Document Loading
                   │
                   ▼
             Text Splitting
                   │
                   ▼
              Embeddings
                   │
                   ▼
          FAISS Vector Database
                   │
                   ▼
            Similarity Search
                   │
                   ▼
          Relevant Information
                   │
                   ▼
          Hugging Face LLM
                   │
                   ▼
             AI Response
```

This approach is called **Retrieval-Augmented Generation (RAG)**.

---

# 🏗️ Application Architecture

```text
┌──────────────────────────────┐
│        Streamlit UI          │
│                              │
│  User Health Information     │
│  Health Questions            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Python Application      │
│                              │
│ BMI │ BMR │ TDEE │ Calories │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          RAG System          │
│                              │
│ LangChain + FAISS + PDF      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Hugging Face LLM       │
│                              │
│     AI Response Generation   │
└──────────────────────────────┘
```

---

# 🛠️ Tech Stack

| Technology               | Purpose                          |
| ------------------------ | -------------------------------- |
| 🐍 Python                | Core programming language        |
| 🎈 Streamlit             | Web application interface        |
| 🦜 LangChain             | RAG application framework        |
| 🧠 FAISS                 | Vector similarity search         |
| 🤗 Hugging Face          | Language model                   |
| 🔤 Sentence Transformers | Text embeddings                  |
| 📄 PyPDF                 | PDF document processing          |
| 🔑 python-dotenv         | Environment variable management  |
| 💬 OpenAI SDK            | Communication with the model API |

---

# 📂 Project Structure

```text
ai-health-assistant/
│
├── app.py
├── diet.py
├── rag.py
├── create_database.py
├── README.md
├── LICENSE
├── .gitignore
│
└── data/
    └── nutrition.pdf
```

### File Description

| File                 | Purpose                                                  |
| -------------------- | -------------------------------------------------------- |
| `app.py`             | Main Streamlit application                               |
| `diet.py`            | BMI, BMR, TDEE and calorie calculations                  |
| `rag.py`             | RAG and FAISS functionality                              |
| `create_database.py` | Creates the vector database                              |
| `nutrition.pdf`      | Nutrition knowledge source                               |
| `.env`               | Stores API credentials locally                           |
| `.gitignore`         | Prevents sensitive/unnecessary files from being uploaded |
| `LICENSE`            | MIT License                                              |

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-health-assistant.git
```

## 2️⃣ Open the Project

```bash
cd ai-health-assistant
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv env
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
env\Scripts\activate
```

### macOS / Linux

```bash
source env/bin/activate
```

---

# 📦 Install Dependencies

Install the required Python packages:

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-huggingface
pip install faiss-cpu
pip install sentence-transformers
pip install pypdf
pip install openai
pip install python-dotenv
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token
```

### ⚠️ Security

**Never upload `.env` to GitHub.**

The `.gitignore` file should contain:

```gitignore
.env
env/
__pycache__/
*.pyc
```

Never expose your Hugging Face API token publicly.

---

# 🗃️ Create the Vector Database

After adding the nutrition PDF, run:

```bash
python create_database.py
```

This processes the nutrition document and creates the FAISS vector database used by the RAG system.

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 💡 Example Questions

You can ask questions such as:

```text
What foods are good sources of fiber?
```

```text
What are some vegetarian sources of protein?
```

```text
What are healthy whole grain foods?
```

```text
What foods contain healthy fats?
```

---

# 📊 Example Workflow

```text
Enter Personal Information
          ↓
Select Activity Level
          ↓
Select Health Goal
          ↓
Select Diet Type
          ↓
Add Food Allergies
          ↓
Calculate BMI / BMR / TDEE
          ↓
Generate Diet Recommendation
          ↓
Ask Nutrition Questions
          ↓
Receive AI Response
```

---

# 🔒 Security

This project uses environment variables for API authentication.

Sensitive files should remain local:

```text
.env
env/
```

These files should **never** be committed to the public repository.


# 🚀 Future Improvements

Some planned improvements include:

* 👤 User authentication
* 📈 Health progress tracking
* 🍱 Larger food database
* 🧮 More nutrition calculations
* 📱 Mobile-friendly interface
* 🗄️ Database integration
* 💬 Improved AI conversations
* 📊 Nutrition charts
* 🥘 Personalized meal plans
* ☁️ Cloud deployment
* 🔔 Health and meal reminders

---

# 🎯 Learning Outcomes

This project helped explore:

* Python programming
* Streamlit application development
* Functions and modules
* API integration
* Environment variables
* Large Language Models
* Prompt engineering
* LangChain
* Retrieval-Augmented Generation
* Vector databases
* FAISS similarity search
* Embeddings
* PDF document processing
* Git and GitHub

---

# 👨‍💻 Author

## Aryan Gill

Python Developer | AI & ML Learner

🐙 GitHub:
https://github.com/pythonwitharyan

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

# 💖 Made With

**Python 🐍 + Streamlit 🎈 + AI 🤖**

### Built for learning, experimentation and exploring AI-powered applications.
# ai-health-assistant
AI-powered health and nutrition assistant built with Python, Streamlit, RAG, FAISS and Hugging Face.
