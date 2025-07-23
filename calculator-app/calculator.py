from flask import Flask, request, render_template

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/add', methods=['GET'])
def web_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        result = add(a, b)
        print(f"Test result: {result}")
    else:
        app.run(host='0.0.0.0', port=5000, debug=True)