from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:blog_id>')
def blog(blog_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    post = response.json()[blog_id - 1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
