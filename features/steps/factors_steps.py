# factors_steps.py
# All our factoring BDD tests

from fizzbuzzapi.factor import isafactorofthree, isafactoroffive, isafactorofboth

@given(u'i pass the number "{number}"')
def step_impl(context, number):
    context.number = int(number)
    assert context.number

@when(u'i divide it by 3')
def step_impl(context):
    context.result = isafactorofthree(context.number)

@then(u'i will get true')
def step_impl(context):
    assert context.result

@then(u'i will get false')
def step_impl(context):
    assert not context.result

@when(u'i divide it by 5')
def step_impl(context):
    context.result = isafactoroffive(context.number)

@when(u'i divide it by 3 and 5')
def step_impl(context):
    context.result = isafactorofboth(context.number)