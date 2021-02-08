from manager import app
from flask_restful import Api, Resource
from application.controllers.UserController import UserController, UserList
from application.controllers.AccountController import AccountControllerSignIn, AccountControllerSignUp, AccountControllerRefresh

api = Api(app)
class ManagerStart(Resource):
    def get(self):
        return {'status': 200}

#register url
api.add_resource(ManagerStart, '/')
api.add_resource(UserController, '/api/v1/users')
api.add_resource(UserList, '/api/v1/get-user')
api.add_resource(AccountControllerSignIn, '/api/v1/account/sign-in')
api.add_resource(AccountControllerSignUp, '/api/v1/account/sign-up')
api.add_resource(AccountControllerRefresh, '/api/v1/account/refresh')


