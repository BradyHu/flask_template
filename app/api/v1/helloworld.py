from flask_restplus import Namespace,Resource,reqparse

api = Namespace('hello')

hello = reqparse.RequestParser()
hello.add_argument('name',default='brady')

@api.route('/hello')
class Hello(Resource):
    @api.expect(hello)
    def get(self):
        args = hello.parse_args()
        name = args.name

        return {'message':f"hello, {name}"}
