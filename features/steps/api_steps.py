from behave import *
from fizzbuzzapi import app

import json

@given(u'i provide the number "{number}"')
def step_impl(context, number):
    context.number = number
    assert context.number

@when(u'i check this against the api')
def step_impl(context):
    context.result = context.client.get('/{0}'.format(context.number))

@then(u'i will get "{text}" back')
def step_impl(context, text):
    assert json.loads(context.result.data) == text and context.result.status_code == 200

@given(u'i provide the numbers "{low}" and "{high}"')
def step_impl(context, low, high):
    context.low = low
    context.high = high

@when(u'i check these against the api')
def step_impl(context):
    context.result = context.client.get('/{0}/{1}'.format(context.low, context.high))

@then(u'i will get a list back "{count}" in length')
def step_impl(context, count):
    assert len(json.loads(context.result.data)) == int(count) and context.result.status_code == 200

@then(u'i will get the correct http error code')
def step_impl(context):
    assert context.result.status_code == 400