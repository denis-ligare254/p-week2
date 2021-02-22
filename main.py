from flask import Flask, render_template
from newsapi import NewsApiClient 

app = Flask(__name__)
@app.route('/')
def index ():
   newsapi =NewsApiClient(api_key="0e1fc7cee0e8462e92dd4bb8eb5f98c1")
   NewsKey = NewsApiKey(api_key="0e1fc7cee0e8462e92dd4bb8eb5f98c1")
   '''
   unique key to help us access news over the internet to the application
   '''
  bulletingMain =  newsapi.get_bulleting_Main(sources="abc-news-au")




if __name__ == '__main__':
    app.run(debug = True)
