import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

database = 'blog_db.db'


def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('blog.html', posts=posts)


def get_post(post_id):
    conn = get_db()
    blog_post = conn.execute('SELECT * FROM posts WHERE id = ?', post_id).fetchone()
    conn.close()
    return post


@app.route('/<int:post_id>')
def post(post_id):
    post_to = get_post(post_id)
    return render_template('post.html', post_to=post_to)


if __name__ == '__main__':
    app.run(debug=True)
