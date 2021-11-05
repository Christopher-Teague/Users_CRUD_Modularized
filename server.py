from flask import Flask, render_template, request ,redirect
from flask.wrappers import Request
from mysqlconnection import connectToMySQL
# import the class from user.py
from user import Users

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = Users.get_all()
    print(users)
    return render_template("read_all.html", all_users = users)

@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    Users.save(request.form)
    return redirect('/users')
    # query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
    # return connectToMySQL(DATABASE).query_db(query, data)


@app.route('/user/<int:id>/edit')
def user_edit(id):
    context = {
    'user': Users.get_one({'id':id})
    }
    return render_template('edit_user.html', **context)

@app.route('/user/<int:id>/update', methods=['POST'])
def update(id):
    data = {
        **request.form,
        'id' : id
    }
    Users.update(data)
    return redirect(f'/user/{id}')

@app.route('/user/<int:id>')
def get_one(id):
    context = {
    'user': Users.get_one({'id': id})
    }
    return render_template('user_info.html', **context)



            
if __name__ == "__main__":
    app.run(debug=True)

