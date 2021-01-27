from flask import Flask
import pandas as pd

application = Flask(__name__)

@application.route("/")
def home():
    return "Hello party people!"
    
@application.route("/sun")
def guns_out():
    return "Sun's out guns out"
    
@application.route("/rugby_scores")
def scores():
    file = '2020results.csv'
    df = pd.read_csv(file)
    return df.to_html(header="true", table_id="table")
    

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)