import openai
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from nltk.tokenize import sent_tokenize
from rest_framework.decorators import api_view
from rest_framework.response import Response

openai.api_key = "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"


@api_view(['GET'])
def get_data(request):
    url = request.GET.get('url')
    reviews = scraper(url)

    summary = summarize_array(reviews)
    print(summary)
    # one_line = summarize_reviews(reviews)
    return Response({'one_line': summary})


def get_html(url):
    payload = {'api_key': '10ca7ca53cc96fc775b7efc2a9c7767a', 'url': url, 'render': 'true'}
    response = requests.get('http://api.scraperapi.com/', params=payload)
    return response.content


def scrape_reviews(html):
    soup = BeautifulSoup(html, 'html.parser')
    reviews = []

    div_tags = soup.find_all("div", attrs={
        "class": "a-expander-content reviewText review-text-content a-expander-partial-collapse-content"})

    for div in div_tags:
        span = div.find("span")
        if span is not None:
            reviews.append(div.text.strip())

    return reviews


def scraper(product_url):
    product_html = get_html(product_url)
    reviews = scrape_reviews(product_html)
    return reviews


def summarize_reviews(reviews):
    text = ' '.join(reviews)

    sentences = sent_tokenize(text)

    summary = ""
    count = 0.01

    while len(summary) <= 0:
        summary = summarize(text, ratio=0.01)
        count += 0.01

    return summary


def summarize_array(array):
    prompt = "Please summarize the following texts:\n"
    for text in array:
        prompt += f"- {text}\n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        n=1,
        stop=None,
        timeout=30,
    )
    summary = response.choices[0].text.strip()
    return summary
