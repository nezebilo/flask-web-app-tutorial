from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html', boolean=True, user="Tim")


@auth.route('/logout')
def logout():
    return "<p>You have Logged Out!</p>"


@auth.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(firstname) < 2:
            flash('Name must be longer than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords do not matchs', category='error')
        elif len(password1) < 4:
            flash('Password must be longer than 3 characters', category='error')
        else:
            flash('Account Created', category='success')
            
    return render_template('sign-up.html')
