from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("main/index.html")
@app.route("/contact")
def contacts():
    return render_template("main/contact.html")
@app.route("/graphics")
def graphics():
    return render_template("main/graphics.html")
@app.route("/wd")
def wdesign():
    return render_template("main/wb.html")
@app.route("/socialmedia")
def smedia():
    return render_template("main/socialmedia.html")
@app.route("/team")
def team():
    return render_template("main/team.html")
@app.route("/policy")
def policy():
    return render_template("main/privacyPolicy.html")
if __name__=="__main__":
    app.run()
