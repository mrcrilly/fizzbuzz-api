from fizzbuzzapi import app

def before_all(context):
    # http://flask.pocoo.org/docs/testing/ -- see for info on test_client()
    app.config['TESTING'] = True
    context.client = app.test_client()