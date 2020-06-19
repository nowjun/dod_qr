from flask import Flask, render_template
# from flask_restful import Resource, Api
# from flask_restful.reqparse import RequestParser
app = Flask(__name__)
# api = Api(app)
#
# class CreateUser(Resource):
#     def post(self):
#         try:
#             parser = RequestParser()
#             parser.add_argument('code', type=str)
#             parser.add_argument('name', type=str)
#             parser.add_argument('id', type=str)
#             args = parser.parse_args()
#
#             _code = args['code']
#             _name = args['name']
#             _id = args['id']
#
#             return {'Code': _code, 'Name': _name, 'ID': _id}
#         except Exception as e:
#             return {'error': str(e)}
#
#
# api.add_resource(CreateUser, '/user')
#
@app.route("/")
def main():
    return render_template('reimage.html')


if __name__ == '__main__':
    app.run(debug=True)
