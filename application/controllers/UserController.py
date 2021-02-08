import json
from flask import jsonify
from flask_restful import Resource, reqparse, abort
from application.models.user import User
from application.utils import STATUS_CODE
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

list_user = reqparse.RequestParser()
list_user.add_argument('limit', type=int)
list_user.add_argument('skip', type=int)
list_user.add_argument('typeSort', type=str)

user = reqparse.RequestParser()
user.add_argument('account_number', type=int, required=True, help='Account number is required')
user.add_argument('balance', type=int, required=True, help='Balance is required')
user.add_argument('firstname', type=str, required=True, help='Firstname is required')
user.add_argument('lastname', type=str, required=True, help='Lastname is required')
user.add_argument('age', type=int, required=True, help='Age is required')
user.add_argument('gender', type=str, required=True, help='Gender is required')
user.add_argument('address', type=str, required=True, help='Address is required')
user.add_argument('employer', type=str, required=True, help='Employer is required')
user.add_argument('email', type=str, required=True, help='Email is required')
user.add_argument('city', type=str, required=True, help='City is required')
user.add_argument('state', type=str, required=True, help='State is required')

user_delete = reqparse.RequestParser()
user_delete.add_argument('email', type=str, required=True, help='Email is required')


class UserController(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        if current_user['role'] != 'system_admin':
            return {
                'status': STATUS_CODE['AUTH'],
                'message': 'Permission denied'
            }
        args = list_user.parse_args()
        if not args.limit:
            args.limit = 50
        if not args.skip:
            args.skip = 0
        if not args.typeSort:
            args.typeSort = 'account_number'
        listUser = User.objects.filter({}).limit(args.limit).skip(args.skip).order_by(args.typeSort)
        return jsonify({
            'status': STATUS_CODE['SUCCESS'],
            'data': listUser
        })

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        if current_user['role'] != 'system_admin':
            return {
                'status': STATUS_CODE['AUTH'],
                'message': 'Permission denied'
            }
        args = user.parse_args()
        isExists = User.objects(email=args['email']).first()
        if isExists:
            return {
                'status': STATUS_CODE['ERROR'],
                'message': 'Email already exists'
            }

        isExistsAccountNumber = User.objects(account_number=args['account_number']).first()
        if isExistsAccountNumber:
            return {
                'status': STATUS_CODE['ERROR'],
                'message': 'Account number already exists'
            }
        User(
            account_number=args['account_number'],
            balance=args['balance'],
            firstname=args['firstname'],
            lastname=args['lastname'],
            age=args['age'],
            gender=args['gender'],
            address=args['address'],
            employer=args['employer'],
            email=args['email'],
            city=args['city'],
            state=args['state']
        ).save()
        return {
            'status': STATUS_CODE['SUCCESS'],
            'message': 'Successfully'
        }

    @jwt_required
    def put(self):
        current_user = get_jwt_identity()
        if current_user['role'] != 'system_admin':
            return {
                'status': STATUS_CODE['AUTH'],
                'message': 'Permission denied'
            }
        args = user.parse_args()

        User.objects.get(email=args['email']).update(
            account_number=args['account_number'],
            balance=args['balance'],
            firstname=args['firstname'],
            lastname=args['lastname'],
            age=args['age'],
            gender=args['gender'],
            address=args['address'],
            employer=args['employer'],
            city=args['city'],
            state=args['state']
        )
        return {
            'status': STATUS_CODE['SUCCESS'],
            'message': 'Successfully'
        }

    @jwt_required
    def delete(self):
        current_user = get_jwt_identity()
        if current_user['role'] != 'system_admin':
            return {
                'status': STATUS_CODE['AUTH'],
                'message': 'Permission denied'
            }
        args = user_delete.parse_args()
        User.objects.get(email=args['email']).delete()
        return {
            'status': STATUS_CODE['SUCCESS'],
            'message': 'Successfully'
        }


get_user = reqparse.RequestParser()
get_user.add_argument('field', type=str, required=True, help='Field is required')
get_user.add_argument('value', type=str, required=True, help='Value is required')
get_user.add_argument('limit', type=int)
get_user.add_argument('skip', type=int)


class UserList(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        if current_user['role'] != 'system_admin':
            return {
                'status': STATUS_CODE['AUTH'],
                'message': 'Permission denied'
            }
        args = get_user.parse_args()
        if not args.limit:
            args.limit = 20
        if not args.skip:
            args.skip = 0
        fields = ['account_number', 'balance', 'firstname', 'lastname', 'age', 'gender', 'address', 'employer', 'email',
                  'city', 'state']
        if args['field'] not in fields:
            return {
                'status': STATUS_CODE['ERROR'],
                'message': 'Field invalid'
            }
        field = args.field
        value = args.value
        if field in ['account_number', 'balance', 'age']:
            value = int(value)
        users = User.objects(__raw__={field: value}).limit(args.limit).skip(args.skip)
        if not user:
            return {
                'status': STATUS_CODE['ERROR'],
                'message': "Data not found"
            }
        return jsonify({
            'status': STATUS_CODE['SUCCESS'],
            'data': users
        })
