import streamlit as st
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
from serpapi import GoogleSearch

# --- 1. CONFIGURATION ---
ENDEE_URL = "http://localhost:8080/api/v1"
INDEX_NAME = "realtime_analysis_cache"
SERP_API_KEY = "03151000259d07957eeb04412352a26eddcbba69902dbaccaf231727bf312c9f" 

@st.cache_resource
def load_resources():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    try:
        requests.post(f"{ENDEE_URL}/index/create",
                      json={"name": INDEX_NAME, "dimension": 384})
    except:
        pass
    return model

MODEL = load_resources()

# --- 2. SCRAPING ENGINE ---
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_snapdeal(query):
    results = []
    try:
        url = f"https://www.snapdeal.com/search?keyword={query.replace(' ', '+')}"
        res = requests.get(url, headers=HEADERS, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')

        cards = soup.select('.product-tuple-listing')[:5]

        for card in cards:
            results.append({
                "title": card.select_one('.product-title').text.strip(),
                "price": card.select_one('.product-price').text.strip(),
                "img": card.select_one('img')['src'] if card.select_one('img') else "https://placehold.co/200",
                "source": "Snapdeal"
            })
    except:
        pass

    return results


def scrape_google_shopping(query):
    results = []
    try:
        params = {
    "engine": "google_shopping",
    "q": query,
    "api_key": SERP_API_KEY,
    "num": 10   
}

        search = GoogleSearch(params)
        data = search.get_dict()

        for item in data.get("shopping_results", [])[:5]:
            results.append({
                "title": item.get("title"),
                "price": item.get("price"),
                "img": item.get("thumbnail"),
                "source": "Google Shopping"
            })
    except Exception as e:
        print(e)

    return results


# --- 3. UI ---
st.set_page_config(page_title="AI Product Sentinel", layout="wide")

st.markdown("""
<h1 style='text-align: center;'>AI Product Sentinel</h1>
<p style='text-align: center; color: gray;'>Compare products across marketplaces using AI similarity</p>
""", unsafe_allow_html=True)


target_url = st.text_input("🔗 Enter Product URL")

if st.button("🚀 Run Analysis"):

    # Extract name
    try:
        name_part = target_url.split('/')[-3].replace('-', ' ').title()
    except:
        name_part = "Men Shoes"

    with st.spinner("🔍 Searching across marketplaces..."):

       
        snapdeal = scrape_snapdeal(name_part)
        google = scrape_google_shopping(name_part)

        candidates = snapdeal + google

        # --- Embedding ---
        target_vec = MODEL.encode(name_part)

        final_results = []
        for item in candidates:
            if not item.get('title'):
                continue

            candidate_vec = MODEL.encode(item['title'])
            similarity = float(util.cos_sim(target_vec, candidate_vec).item())
            item['score'] = similarity
            final_results.append(item)

        
        final_results = sorted(final_results, key=lambda x: x['score'], reverse=True)[:8]

    # --- RESULTS UI ---
    st.subheader(f"🔎 Results for: {name_part}")

    cols = st.columns(4)

    for idx, item in enumerate(final_results):
        with cols[idx % 4]:
            st.markdown(
                f"""
               <div style="
            border-radius:15px;
             padding:10px;
             background-color:#f9f9f9;
             box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align:center;
            height:320px;
            display:flex;
            flex-direction:column;
            justify-content:space-between;
            ">
                    <img src="{item['img']}" width="150"/>
                    <h5>{item['title'][:60]}...</h5>
                    <p><b>{item['price']}</b></p>
                    <p style="color:gray;">{item['source']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(item['score'])
            st.caption(f"Match Score: {item['score']:.4f}")