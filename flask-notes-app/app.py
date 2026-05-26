from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "secretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(120), nullable=False)

class Note(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    content = db.Column(db.Text, nullable=False)    

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    if "user_id" in session:
        return redirect ("/dashboard")
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        existing_user = User.query.filter_by(
            username=username
        ).first()
        
        if existing_user:
            return"Username already exists!" 
        
        new_user = User(
            username=username,
            password=password
        )

        db.session.add(new_user)

        db.session.commit()

        return redirect("/login")
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:
            session["user_id"] = user.id
            return redirect("/dashboard")
        return "Invalid username or password!"
    
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    
    notes = Note.query.filter_by(user_id=session["user_id"]).all()
    return render_template("dashboard.html", notes=notes)

@app.route("/add", methods=["GET", "POST"])
def add_note():

    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        content = request.form.get("content")

        new_note = Note(
            content=content,
            user_id=session["user_id"]
        )

        db.session.add(new_note)

        db.session.commit()

        return redirect("/dashboard")

    return render_template("add_note.html")

@app.route("/delete/<int:id>")
def delete_note(id):

    note = Note.query.get(id)

    if note and note.user_id == session["user_id"]:
        db.session.delete(note)

        db.session.commit()
    return redirect("/dashboard")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")
    

if __name__ == "__main__":
    app.run(debug=True)        
