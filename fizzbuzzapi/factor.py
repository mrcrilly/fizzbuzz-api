# factor.py
# our simple factoring functions

def isafactorofthree(number):
    return not bool(number%3)

def isafactoroffive(number):
    return not bool(number%5)

def isafactorofboth(number):
    return isafactorofthree(number) and isafactoroffive(number)