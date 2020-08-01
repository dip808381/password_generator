from flask import Flask, request, render_template
from password import pwrd
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def classifierA():
    if request.method == "POST":
        val = request.form.get("nm")
        out = pwrd(val)
        return render_template("login.html",out="The Predicted Salary Is:"+ out)

    return render_template("login.html",out="")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port = 8080)

if __name__ == "__main__":
    app.run(debug=True)