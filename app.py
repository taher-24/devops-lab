
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def accueil():
    date = datetime.now().strftime("%d/%m/%Y")
    return f"""
    <h1>Devops Lab</h1>
    <h2>Application Opérationelle - Version 1.0</h2>
    <p>Directed by Taher Toula</p>
    <p>Date : {date}</p>
    """
