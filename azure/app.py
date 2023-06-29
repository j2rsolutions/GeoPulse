from flask import Flask, render_template_string
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    r = requests.get('http://169.254.169.254/metadata/instance?api-version=2020-09-01')
    data = json.loads(r.text)
    location = data['compute']['location']
    az = data['compute']['azEnvironment']

    html = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <img src="{{{{ url_for('static', filename='img/logo.png') }}}}" alt="Company Logo" width="200">
        <img src="{{{{ url_for('static', filename='img/azure.png') }}}}" alt="Azure Logo" width="100">
        <h1>Region: {location}</h1>
        <h2>Availability Zone: {az}</h2>
        <h3>Cloud Provider: Azure</h3>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
