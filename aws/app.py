from flask import Flask, render_template_string
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    region = requests.get('http://169.254.169.254/latest/meta-data/placement/region').text
    az = requests.get('http://169.254.169.254/latest/meta-data/placement/availability-zone').text

    html = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <img src="{{{{ url_for('static', filename='img/logo.png') }}}}" alt="Company Logo" width="200">
        <img src="{{{{ url_for('static', filename='img/aws.png') }}}}" alt="AWS Logo" width="100">
        <h1>Region: {region}</h1>
        <h2>Availability Zone: {az}</h2>
        <h3>Cloud Provider: AWS</h3>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
