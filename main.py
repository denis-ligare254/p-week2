
from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources="abc-news-au")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('index.html', context=mylist)


@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="YOUR-API-KEY")
    topheadlines = newsapi.get_top_headlines(sources="ary-news")

    articles = topheadlines['articles']

    description = []
    news = []
    image= []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        description.append(myarticles['description'])
        image.append(myarticles['urlToImage'])

    mylist = zip(news, description, image)

    return render_template('bbc.html', context=mylist)


if __name__ == "__main__":
    app.run(debug=True)
