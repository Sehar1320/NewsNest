from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = '7a239b1b18144d7484cbe7f73511ccce'

# Using search keywords instead of exact source IDs
NEWS_QUERIES = {
    'The Economic Times': 'Economic Times',
    'Times of India': 'Times of India',
    'The Hindu': 'The Hindu',
    'Hindustan Times': 'Hindustan Times'
}

def fetch_news(query):
    url = f'https://newsapi.org/v2/everything?q="{query}"&language=en&sortBy=publishedAt&pageSize=5&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if data.get("status") == "ok":
        return data.get("articles", [])
    return []

@app.route('/')
def home():
    news_data = {}
    for paper, query in NEWS_QUERIES.items():
        articles = fetch_news(query)
        news_data[paper] = articles
    return render_template('home.html', news_data=news_data)

if __name__ == '__main__':
    app.run(debug=True)