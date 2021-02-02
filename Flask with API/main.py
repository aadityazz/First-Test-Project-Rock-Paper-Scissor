from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homeEnter():
    return 'Hello! Would you like to enter your name in URL.'


@app.route('/<naming>')
def home(naming):
    name = naming
    url_gender = f"https://api.genderize.io/?name={naming}"
    r = requests.get(url_gender)
    data = r.json()
    value = data['gender']
    return render_template('index.html', name = name, value= value)


if __name__ == "__main__":
    app.run(debug=True)