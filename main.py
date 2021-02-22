from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index ():
   NewsKey = NewsApiKey(api_key="0e1fc7cee0e8462e92dd4bb8eb5f98c1")
   '''
   unique key to help us access news over the internet to the application
   '''





if __name__ == '__main__':
    app.run(debug = True)
