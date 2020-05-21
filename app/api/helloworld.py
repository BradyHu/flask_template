from flask_restplus import Namespace,Resource,reqparse
from flask import jsonify

api = Namespace('hello')

hello = reqparse.RequestParser()
hello.add_argument('name',default='brady')

celecy_example = reqparse.RequestParser()
celecy_example.add_argument('text', default='blank')

@api.route('/hello')
class Hello(Resource):
    @api.expect(hello)
    def get(self):
        args = hello.parse_args()
        name = args.name

        return {'message':f"hello, {name}"}


@api.route('/celeryexample')
class CeleryExample(Resource):
    @api.expect(celecy_example)
    def get(self):
        from app.celery import celery
        args = celecy_example.parse_args()
        text = args.text

        result = celery.send_task('app.tasks.example.example', (text,))

        return jsonify({'message': 'success', 'result': result.result})

