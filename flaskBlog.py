import email
from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
mydatabase = client.flaskData
mycollection = mydatabase.userdata

app = Flask(__name__)#set variable to flask __name__ is name of module

app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'

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

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!','success')
        return redirect(url_for('home'))#name of the function not file
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        

        email=form.email.data
        user_password=form.password.data
        print(email,user_password)
        user_data = mycollection.find_one({'email': email})
        print(user_data)
        if user_data:
                flash('You hava been logged in!','success')
                return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password','danger')


    # if form.validate_on_submit():
    #     if form.email.data=='admin@blog.com'and form.password.data=='password':
    #         flash('You hava been logged in!','success')
    #         return redirect(url_for('home'))
    #     else:
    #         flash('Login unsuccessful. Please check username and password','danger')

    # if request.method == 'POST':
        # if valid_login(request.form['username'],request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    return render_template('login.html',title='Login',form=form)

# if __name__=='__main__':
#     app.run(debug=True)