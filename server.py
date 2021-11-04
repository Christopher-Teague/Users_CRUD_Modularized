from flask import Flask, render_template
from mysqlconnection import connectToMySQL
# import the class from user.py
from user import Users

app = Flask(__name__)

@app.route('/')
def index():
    users = Users.get_all()
    print(users)
    return render_template("read_all.html", all_users = users)

@app.route('/create')
def create(cls, data):
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
    return connectToMySQL(DATABASE).query_db(query, data)

            
if __name__ == "__main__":
    app.run(debug=True)

