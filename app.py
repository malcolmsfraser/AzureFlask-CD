from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello party people!! Isn't continuous delivery is cool!? FUCK YES IT WORKS ON BOOOOOTTTTTHHHH!!!"
    
@app.route("/sun")
def guns_out():
    return "Sun's out guns out"
    
@app.route("/rugby_scores")
def scores():
    file = '2020results.csv'
    df = pd.read_csv(file)
    return df.to_html(header="true", table_id="table")
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)