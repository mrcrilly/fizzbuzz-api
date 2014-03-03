from fizzbuzzapi import api

from flask.ext.restful import Resource

class FizzBuzz(Resource):
    def get(self):
        return {'implemented': False}

api.add_resource(FizzBuzz, '/')