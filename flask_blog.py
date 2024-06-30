from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistratonForm, LoginForm

app = Flask(__name__)
# add secrete key
app.config["SECRET_KEY"] = "27b6dcd360704809fc675ebe7db64540"
# specify the uri for the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# create a database instance
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
        
        
posts = [
    {
        "author": "Torzor Hub",
        "title": "Blog post 1",
        "content": "first post content",
        "date_posted": "April 20, 2018"
    },
     {
        "author": "jane Doe",
        "title": "Blog post 2",
        "content": "second post content",
        "date_posted": "April 20, 2018"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title="About")
@app.route("/register", methods=["GET", "POST"])
# to accept a post request add allowed methods in our routes
def register():
    form = RegistratonForm() #this create an instance of the form
    # form validation
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)
    # with form=form we have access to the instance above
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm() #this create an instance of the form
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        return redirect(url_for("login"))
    return render_template("login.html", title="Login", form=form)
    # with form=form we have access to the instance above

if __name__ == "__main__":
    app.run(debug=True)
