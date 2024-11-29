from flask import Flask,render_template
from utils.db import db


flask_app=Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db.init_app(flask_app)

with flask_app.app_context():
    db.create_all()

@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/about')
def about():
    return render_template('about.html')

@flask_app.route('/blogs')
def blogs():
    blogs_list = [
        {
            "blog_id": 1,
            "blog_title":"blog one",
            "blog_content":"blog dummy content",
            "author":"Author 1",
            "date":"29-11-2024"
        },
        {
            "blog_id": 2,
            "blog_title": "blog two",
            "blog_content": "blog dummy content",
            "author": "Author 2",
            "date": "19-11-2024"
        },
        {
            "blog_id": 3,
            "blog_title": "blog three",
            "blog_content": "blog dummy content",
            "author": "Author 3",
            "date": "21-11-2024"
        },
        {
            "blog_id": 4,
            "blog_title": "blog three",
            "blog_content": "blog dummy content",
            "author": "Author 3",
            "date": "21-11-2024"
        },
        {
            "blog_id": 5,
            "blog_title": "blog three",
            "blog_content": "blog dummy content",
            "author": "Author 3",
            "date": "21-11-2024"
        },
        {
            "blog_id": 6,
            "blog_title": "blog three",
            "blog_content": "blog dummy content",
            "author": "Author 3",
            "date": "21-11-2024"
        }
    ]
    print(blogs_list)
    return render_template('blogs.html', blogs = blogs_list)

@flask_app.route('/add_blog')
def add_blog():
    return render_template('add_blog.html')









if __name__ == '__main__':
    flask_app.run(
    host='127.0.0.1',
    port=8005,
    debug=True
)