from flask import Blueprint, render_template
main = Blueprint('main', __name__)

@main.route('/')
def home():
    posts = [ 
        {
            "body" : "This is the post",
            "timestamp" : "Date and time of post"
        }
    ]
    return render_template("home.html", posts=posts)

