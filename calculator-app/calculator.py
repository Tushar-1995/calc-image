from flask import Flask, request

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/add', methods=['GET'])
def web_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)