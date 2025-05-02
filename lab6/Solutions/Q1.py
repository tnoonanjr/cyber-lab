from flask import Flask, make_response


app = Flask(__name__)

@app.route("/")
def main():
    response = make_response("set cookie")
    response.set_cookie('Q1B1', 'thn23001')
    return response

@app.route('/Q1B2/')
def Q1B2():
    response = make_response("set cookie 2")
    response.set_cookie('Q1B2', 'Noonan', path="/Q1B2")
    return response

@app.route('/Q1B3/')
def Q1B3():
    response = make_response("set cookie 3")
    response.set_cookie('Q1B3', '10.13.6.151', httponly=True, secure=True)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
