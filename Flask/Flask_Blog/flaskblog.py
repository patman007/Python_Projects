#Required Template for Flask Starting out
# from flask import Flask,
# app = Flask(__name__)

# #Root Route
# @app.route('/')
# @app.route('/home')
# def home():
#     return '<h1>Home Page</h1>'

##################################

#Required Template for Flask
from flask import Flask, render_template, url_for
app = Flask(__name__)

#List of Dictionaries
posts = [
    {
        'author': 'Patrick Mason',
        'title': 'Blog Post 1',
        'content': "First post content",
        'date_posted': 'December 12, 2020'
    },
    {
        'author': 'Corey Schauffer',
        'title': 'Blog Post 2',
        'content': "Second post content",
        'date_posted': 'January 12, 2021'
    },
    {
        'author': 'James Jim',
        'title': 'Blog Post 3',
        'content': "Third post content",
        'date_posted': 'February 12, 2021'
    },
]

#Root Route
@app.route('/')
@app.route('/home.html')
def home():
    return render_template('home.html', posts=posts)

#About Route
@app.route('/about')
def about():
    return render_template('about.html', title='About')

###############################

#Run your own environment
if __name__ == '__main__':
    app.run(debug=True)

###############################

