from flask_app.controllers import users_controller
from flask_app import app ### MVC
# ...server.py

# import the class from user.py
from flask_app.models.user import Users

if __name__ == "__main__":
    app.run(debug=True)


