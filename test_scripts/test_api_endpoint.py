from flask import Flask, request

app = Flask(__name__)

@app.route('/nmap-results', methods=['POST'])
def receive_nmap_results():
    data = request.json
    print(data)

    return {'message': 'Data received successfully'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# packages installed for this
# Flask-2.3.2 Jinja2-3.1.2 MarkupSafe-2.1.3 Werkzeug-2.3.6 blinker-1.6.2 click-8.1.6 colorama-0.4.6 itsdangerous-2.1.2