from behave import given, when, then
import behave

@given('I have entered {num:d} into the calculator')
def enter_number(context, num):
    context.calculator = Calculator()
    context.calculator.enter(num)

@when('I press add')
def press_add(context):
    context.calculator.add()

@then('the result should be {expected_result:d} on the screen')
def verify_result(context, expected_result):
    assert context.calculator.result == expected_result
