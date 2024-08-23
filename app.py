from flask import Flask,render_template,request,url_for,redirect
from adminValidation import adminValidation

app = Flask(__name__,template_folder="template")

@app.route('/',methods=['POST','GET'])
def index():
    error = None
    if request.method == "POST":
        if request.form.get("username") and request.form.get("password"):
            adminValidator = adminValidation(request.form.get("username"),request.form.get("password"))
            if adminValidator.usernameChecker() and adminValidator.passwordChecker():
                return redirect(url_for("library"))
            else:
                error="Check Your Username and password"
    return render_template("login.html",error=error)

@app.route('/library')
def library():
    return render_template("library.html")

@app.route("/add_book")
def add_book():
    return render_template("add_book.html")

@app.route("/remove_book")
def remove_book():
    return render_template("remove_book.html")

@app.route("/show_books")
def show_books():
    return render_template("show_books.html")

@app.route("/update_book")
def update_book():
    return render_template("update_book.html")



if __name__=="__main__":
    app.run(debug=True)
