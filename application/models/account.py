from manager import db
from application.models.role import Role
from application.utils.Bcrypt import generate_password, verify_password
from application.utils import STATUS_CODE
from flask_jwt_extended import (create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required)


# Defind Model
class Account(db.Document):
    email = db.EmailField()
    password = db.StringField()

    def sign_up(self, email, password):
        isExists = Account.objects(email=email).first()
        if isExists:
            return {
                'status': STATUS_CODE['ERROR'],
                'message': 'Email already exists'
            }
        password = generate_password(self, password)
        Account(email=email, password=password).save()
        return {
            'status': STATUS_CODE['SUCCESS'],
            'message': 'Successfully!'
        }

    def sign_in(self, email, password):
        isExists = Account.objects(email=email).first()

        if not isExists:
            return {
                'status': STATUS_CODE['ERROR'],
                'message': "Email hasn't register"
            }
        if not verify_password(self, isExists.password, password):
            return {
                'status': STATUS_CODE['ERROR'],
                'message': "Password invalid"
            }
        role = Role.get_role(self, isExists.email)
        # Identity can be any data that is json serializable
        access_token = create_access_token({
            'email': isExists.email,
            'role': role['role']
        })
        refresh_token = create_refresh_token({
            'email': isExists.email,
            'role': role['role']
        })
        return {
            'status': STATUS_CODE['SUCCESS'],
            'data': {
                'email': isExists.email,
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        }

    @jwt_refresh_token_required
    def refresh(selfs):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {
            'status': STATUS_CODE['SUCCESS'],
            'access_token': access_token
        }

    def to_json(self):
        return {
            'email': self.email,
            'password': self.password
        }
