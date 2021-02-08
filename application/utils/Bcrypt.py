from manager import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#generate password
def generate_password(self, password):
    pw_hash = bcrypt.generate_password_hash(password)
    return pw_hash

#verify password
def verify_password(self, pw_hash, password):
    return bcrypt.check_password_hash(pw_hash, password)
