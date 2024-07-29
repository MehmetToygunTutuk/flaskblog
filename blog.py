from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, TextAreaField, validators
from passlib.hash import sha256_crypt
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Please log in to see this page", "danger")
            return redirect(url_for("login"))
    return decorated_function

class RegisterForm(Form):
    name = StringField("Name Surname", validators=[validators.length(min=4, max=100)])
    username = StringField("Username", validators=[validators.length(min=5, max=50)])
    email = StringField("Email", validators=[validators.Email("Please enter a valid email")])
    password = PasswordField("Password", validators=[
        validators.DataRequired(message= "You must assign a password"),
        validators.EqualTo(fieldname= "confirm", message="Password does not match")
    ])
    confirm = PasswordField("Confirm Password")

class LoginForm(Form):
    username = StringField("Username")
    password = PasswordField("Password")

app = Flask(__name__)
app.secret_key = "blog"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "blog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    cursor = mysql.connection.cursor()
    query = "Select * From articles"
    result = cursor.execute(query)
    if result > 0:
        articles = cursor.fetchall()
        return render_template("articles.html", articles = articles)
    else:
        return render_template("articles.html")

@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    query = "Select * From articles where AUTHOR = %s"
    result = cursor.execute(query, (session["username"], ))
    if result > 0:
        articles = cursor.fetchall()
        return render_template("dashboard.html", articles = articles)
    else:
        return render_template("dashboard.html")

@app.route("/article/<string:id>")
@login_required
def article(id):
    cursor = mysql.connection.cursor()
    query = "Select * From articles where ID = %s"
    result = cursor.execute(query, (id, ))
    if result > 0:
        article = cursor.fetchone()
        return render_template("article.html", article = article)
    else:
        return render_template("article.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():

        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        query = "Insert into users(NAME, EMAIL, USERNAME, PASSWORD) Values(%s, %s, %s, %s)"
        cursor.execute(query, (name, email, username, password))
        mysql.connection.commit()
        cursor.close()
        flash("You have successfully registered.","success")
        return redirect(url_for("login"))
    else:
        return render_template("register.html", form = form)
    
@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST":
        username = form.username.data
        entered_password = form.password.data
        cursor = mysql.connection.cursor()
        query = "Select * From users where username = %s"
        result = cursor.execute(query, (username, ))
        if result > 0:
            data = cursor.fetchone()
            real_password = data["PASSWORD"]
            if sha256_crypt.verify(entered_password, real_password):
                flash("You have logged in successfully", "success")
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("index"))
            else:
                flash("Wrong Password...", "danger")
                return redirect(url_for("login"))

        else:
            flash("There is no user such like that", "danger")
            return redirect(url_for("login"))

    return render_template("login.html", form = form)

@app.route("/exit")
def exit_blog():
    session.clear()
    return redirect(url_for("login"))

@app.route("/addarticle", methods = ["GET", "POST"])
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data

        cursor = mysql.connection.cursor()
        query = "Insert Into articles (TITLE, AUTHOR, CONTENT) Values (%s, %s, %s)"
        cursor.execute(query, (title, session["username"], content))
        mysql.connection.commit()
        cursor.close()
        flash("Article added successfully", "success")
        return redirect(url_for("dashboard"))
    return render_template("addarticle.html", form = form)

@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    query = "Select * From articles where AUTHOR = %s and ID = %s"
    result = cursor.execute(query, (session["username"], id))
    if result > 0:
        query2 = "Delete From articles where id = %s"
        cursor.execute(query2, (id, ))
        mysql.connection.commit()
        return redirect(url_for("dashboard"))
    else:
        flash("There is no article like that or you dont have the authority", "danger")
        return redirect(url_for("index"))
    
@app.route("/update/<string:id>", methods = ["GET", "POST"])
@login_required
def update(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        query = "Select * From articles where ID = %s and AUTHOR = %s"
        result = cursor.execute(query, (id, session["username"]))
        if result == 0:
            flash("There is no article like that or you dont have the authority", "danger")
            return redirect(url_for("index"))
        else:
            article = cursor.fetchone()
            form = ArticleForm()
            form.title.data = article["TITLE"]
            form.content.data = article["CONTENT"]
            return render_template("update.html", form = form)
    else:
        form = ArticleForm(request.form)
        new_title = form.title.data
        new_content = form.content.data

        query2 = "Update articles Set TITLE = %s, CONTENT = %s where ID = %s"
        cursor = mysql.connection.cursor()
        cursor.execute(query2, (new_title, new_content, id))
        mysql.connection.commit()
        flash("Article has updated successfully", "success")
        return redirect(url_for("dashboard"))

class ArticleForm(Form):
    title = StringField("Article Title", validators=[validators.Length(min= 5, max = 100)])
    content = TextAreaField("Content", validators=[validators.Length(min = 10)])

@app.route("/search", methods = ["GET", "POST"])
def search():
    if request.method == "GET":
        flash("You dont have permission for that", "warning")
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        query = "Select * From articles where TITLE like '%" + keyword + "%'"
        result = cursor.execute(query)
        if result == 0:
            flash("There is no articles like that", "danger")
            return redirect(url_for("articles"))
        else:
            articles = cursor.fetchall()
            return render_template("articles.html", articles = articles)

if __name__ == "__main__":
    app.run(debug= True)