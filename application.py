import  os
import  json
import  requests
from    flask       import Flask, render_template
from    get_data    import get_news, get_tweets


API_KEY_1   = os.environ.get("API_KEY_1")
API_NAME_1  = os.environ.get("API_NAME_1")

API_KEY_2   = os.environ.get("API_KEY_2")
API_NAME_2  = os.environ.get("API_NAME_2")


app = Flask(__name__)

@app.route('/')
def get_index():
    
    articles  = get_news(API_NAME_2, API_KEY_2)
    tweets    = get_tweets(API_NAME_1, API_KEY_1) 
    
    return render_template('index.html', tweets = tweets, articles = articles)
    # return render_template('index.html', tweets = tweets)
    
@app.route('/major_breachs')
def display_data():
    # breachs data displayed with dc/crossfilter/d3
    return render_template('index.html')
    
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

# ------------------------------------------------------------------------------