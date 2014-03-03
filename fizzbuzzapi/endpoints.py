from fizzbuzzapi import api, factor
from flask.ext.restful import Resource

import re

class FizzBuzz(Resource):

    def get(self, low=False, high=False):
        number_re = re.compile('^\d+$')

        # if not number_re.match(str(low)) or not number_re.match(str(high)):
        #     return False, 400

        if low and not number_re.match(low):
            return False, 400

        if high and not number_re.match(high):
            return False, 400

        low, high = int(low), high and int(high)

        if low:
            if high:
                if high > 1001: high = 1001

                results = []
                for x in range(low,high): results.append("Fizz"[x%3*4:]+"Buzz"[x%5*4:] or x)
                return results
            else:
                if factor.isafactorofthree(low):
                    if factor.isafactoroffive(low):
                        return "FizzBuzz"
                    else:
                        return "Fizz"
                elif factor.isafactoroffive(low):
                    return "Buzz"
                else:
                    return low
        else:
            return False

api.add_resource(FizzBuzz, '/<low>', '/<low>/<high>')