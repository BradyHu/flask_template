from flask_restplus import Namespace,Resource,reqparse
from app.models.users import UserModel

api = Namespace('user')

register = reqparse.RequestParser()
register.add_argument('name',required=True)
register.add_argument('password',required=True)

@api.route('register')
class Register(Resource):
    @api.expect(register)
    def post(self):
        args = register.parse_args()
        name = args.name
        password = args.password

        UserModel(username=name,password=password).save()
        return {'success':True}