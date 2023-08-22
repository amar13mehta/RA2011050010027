from flask import Flask, request, jsonify
import requests

app = Flask(name)

def fetch_numbers(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "numbers" in data:
                return data["numbers"]
    except Exception as e:
        print(f"Error fetching numbers from {url}: {e}")
    return []

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    all_numbers = []
    for url in urls:
        numbers = fetch_numbers(url)
        all_numbers.extend(numbers)

    response_data = {"numbers": all_numbers}
    return jsonify(response_data)

if name == 'main':
    app.run(port=8008)