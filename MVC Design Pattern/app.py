from flask import Flask, render_template  # type: ignore
from models import fetch_data 
from views import render_data 
app = Flask(__name__) 
@app.route('/') 
def home(): 
# Fetch data from the model 
    data = fetch_data() 
# Pass data to the view for rendering 
    return render_data(data) 
if __name__ == '__main__': 
    app.run(debug=True)