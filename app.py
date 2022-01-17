
# This is basically the heart of my flask

from flask import Flask, render_template, request
import pickle
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)  # intitialize the flaks app  # common

# Default Home page
@app.route('/')
def home():
    return  render_template('home.html')

# Recommendation Page
@app.route('/recommendation', methods=['POST'])
def recommendation():
    """Recommendation System"""
    user_id = request.form['userId']
    # user_id = '00dog3'
    recommend_data = pickle.load(open('pickle/recommend_data.pkl', 'rb'))
    try:
        recommendProduct = recommend_data.loc[user_id]
        recommend20 = list(recommendProduct.sort_values(ascending=False)[0:5].index)
        # Sentiment based filtering
        # @Todo sentiment
        # Output
        if(len(recommend20) > 0):
            return  render_template('recommend.html',productTable=recommend20)
        else:
            return render_template('recommend.html',error='No Product Found')
    except:
        errorMsg: 'No Recommendation for this user!'
        return render_template('recommend.html',error=errorMsg)

if __name__ == '__main__' :
    app.run(debug=True )  # this command will enable the run of your flask app or api
    #,host="0.0.0.0")
