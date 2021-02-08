from flask_restful import Resource, reqparse, abort
from application.models.account import Account

account_parser = reqparse.RequestParser()
account_parser.add_argument('email', type=str, required=True, help='Email is required')
account_parser.add_argument('password', type=str, required=True, help='Password is required')

class AccountControllerSignIn(Resource):
    def post(self):
        args = account_parser.parse_args()
        return Account.sign_in(self, args.email, args.password)

class AccountControllerSignUp(Resource):
    def post(self):
        args = account_parser.parse_args()
        return Account.sign_up(self, args.email, args.password)

class AccountControllerRefresh(Resource):
    def post(self):
        return Account.refresh(self)