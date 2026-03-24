# 🛡️ AI Product Sentinel

AI Product Sentinel is an AI-powered product comparison system that finds similar products across different marketplaces using semantic similarity instead of basic keyword matching.

This project demonstrates how modern recommendation systems work using embeddings + vector databases (Endee.io).

---

## 🚀 What this project does

This application allows users to paste any product URL and automatically:

Extract the product name
Fetch similar products from multiple marketplaces
Compare them using AI
Display the most relevant matches with a confidence score

---

## 📸 Screenshots

### 🔹 Before Running Analysis

This is the initial interface where the user inputs the product URL.
![Before Analysis](images/ai1.png)
 
### 🔹 After Running Analysis

After clicking **Run Analysis**, the system displays the top 8 most similar products along with similarity scores.
![After Analysis](images/ai2.png)
![After Analysis](images/ai3.png)
  
---
## 🧠 How it works

The workflow is simple and efficient:
1. User enters a product URL  
2. Product name is extracted from the URL  
3. Products are fetched from:
   - Snapdeal  
   - Google Shopping (via SerpAPI)  
4. Product titles are converted into vector embeddings using Sentence Transformers  
5. The system performs similarity search using:
   - Endee.io vector database (if available)  
   - Local cosine similarity (fallback mechanism)  
6. Results are ranked and top 8 products are displayed  

---
## ⚙️ System Architecture
User Input (Product URL)
↓
Product Name Extraction
↓
Scraping Layer
(Snapdeal + Google Shopping)
↓
Embedding Layer
(Sentence Transformers)
↓
Similarity Engine
(Endee Vector DB OR Local Fallback)
↓
Ranking (Top 8 Matches)
↓
Streamlit UI Display

## ✨ Features

-  Works with any product URL  
-  Multi-platform comparison  
-  AI-based semantic similarity  
- Real-time product analysis  
-  Match confidence scoring  
- Displays top 8 most relevant products  
- Clean and interactive Streamlit UI  
- Fault-tolerant system (works even if Endee is down)  

---
## 🏗️ Tech Stack

* Frontend: Streamlit
* Backend: Python
* Web Scraping: BeautifulSoup, Requests
* AI Model: Sentence Transformers (all-MiniLM-L6-v2)
* Vector Database: Endee.io
* External API: SerpAPI (Google Shopping)

---

## 💡 Why Endee.io?

Traditional systems rely on keyword matching, which often gives inaccurate results.

This project uses Endee.io vector database to:

- Understand product meaning (semantic search)  
- Match products even if wording is different  
- Enable efficient similarity search at scale  

Additionally, the system is designed with a fallback mechanism, so it continues to work even if the Endee service is temporarily unavailable.

---

## 📦 Setup Instructions

Clone the repository:
<<<<<<< HEAD
git clone https://github.com/your-username/AI-Product-Sentinel.git
cd AI-Product-Sentinel
=======

```
git clone https://github.com/your-username/ai-product-sentinel.git  
cd ai-product-sentinel  
```

Install dependencies:

```
pip install streamlit requests beautifulsoup4 sentence-transformers google-search-results  
```

Make sure Endee.io is running locally at:

```
http://localhost:8080/api/v1  
```

Add your SerpAPI key in the code:

```
SERP_API_KEY = "YOUR_SERPAPI_KEY"  
```

---

## ▶️ Run the application

```
streamlit run app.py  
```

---

## 🧪 Example Usage

Paste any product link (like shoes, electronics, etc.), click **Run Analysis**, and the app will display the top 8 most similar products along with their match scores.

---

## 🔮 Future Improvements

* Add Amazon and Flipkart integration
* Highlight best deal (lowest price)
* Add direct purchase links
* Improve UI design further
* Deploy the application online

---
## 🎥 Demo

Watch the demo video below:

[Click to watch demo](Demovideo/Demo.mp4)

## 👩‍💻 Author

Ramya

---

## ⭐ Final Note

This project demonstrates how AI combined with vector databases like Endee.io can be used to build intelligent and scalable product recommendation systems.
