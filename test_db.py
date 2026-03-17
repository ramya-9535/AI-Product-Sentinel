import requests

try:
    response = requests.get("http://localhost:8080/api/v1/index/list")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print("✅ Connection Successful!")
except Exception as e:
    print("❌ Connection Failed:", e)