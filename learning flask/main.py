from flask import Flask, render_template, url_for

app = Flask(__name__)
posts = [
    {
        'name' : 'test',
        'title' : 'first title',
        'content' : '1st content',
        'date_posted' : '18 Oct 2010'
    },
    {
        'name' : 'John doe',
        'title' : 'second title',
        'content' : '2nd content',
        'date_posted' : '10 Aug 2012'
    } 
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='ABout page')

if __name__ == '__main__':
    app.run(debug=True)