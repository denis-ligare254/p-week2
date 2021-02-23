# from flask import Flask, render_template
# from newsapi import NewsApiClient 

# app = Flask(__name__)
# @app.route('/')
# def index ():
#    newsapi =NewsApiClient(api_key="0e1fc7cee0e8462e92dd4bb8eb5f98c1")
#    NewsKey = NewsApiKey(api_key="0e1fc7cee0e8462e92dd4bb8eb5f98c1")
#    '''
#    unique key to help us access news over the internet to the application
#    '''
#    bulletingMain =  newsapi.get_bulleting_Main(sources="abc-news-au")

#    articles = bulletingMain("articles")
 
#    description =[]
#    news =[]
#    images =[]

# for i in range(len(articles)):
#     myarticles
#     news.append(myarticles['title'])
#     description.append(myarticles['description'])
#     images.append(myarticles['urlToImage'])


# mylist =zip(description ,news, images)

# return render_template('index.html' context = mylist)

# if __name__ == '__main__':
#     app.run(debug = True)
from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

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
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

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

    return render_template('bbc.html', context=mylist)


if __name__ == "__main__":
    app.run(debug=True)
