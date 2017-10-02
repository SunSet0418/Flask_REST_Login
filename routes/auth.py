from flask import Blueprint, request, render_template, redirect
import db, json
bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        dbdata = db.users.find_one({"id":request.form['id']})
        if(dbdata):
            print(dbdata)
            return json.dumps(dbdata, cls=db.Encoder)

        elif(dbdata == None):
            return 'User Not Founded', 404



@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        dbdata = db.users.find_one({"id":request.form['id']})
        if(dbdata):
            return 'Already In Database' , 404

        else:
            user = {
                "username": request.form['username'],
                "id": request.form['id'],
                "password": request.form['password']
            }
            db.users.insert(user)
            print(user, " Insert Success")
            return redirect('/auth/login')

