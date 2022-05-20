from flask import Flask,render_template

app = Flask(__name__)#set variable to flask __name__ is name of module

posts=[
    {
        'author':'Narayani H',
        'title':'Hello using flask',
        'content':'First post',
        'date_posted':'May 20,2022',
    },
    {
        'author':'Hari Bhat',
        'title':'Accounting',
        'content':'Hello to all',
        'date_posted':'May 12,2010',
    },
    {
        'author':'Kalavathi',
        'title':'Motherhood',
        'content':'Working women are great',
        'date_posted':'May 18,2022',
    },
]

@app.route("/")#home page route
@app.route("/home")

def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title="ABOUT")

# if __name__=='__main__':
#     app.run(debug=True)