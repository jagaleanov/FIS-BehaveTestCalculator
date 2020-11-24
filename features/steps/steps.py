from behave import *
from calculadora import Calculadora

#sum
@given('two numbers {values} to sum')
def step_imp(context, values):
    context.calc= Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc sum the values')
def step_imp(context):
    context.total = context.calc.sumar(context.values[0],context.values[1])

@then('the sum is {total:d}')
def step_imp(context, total):
    assert (context.total == total)

#res
@given('two numbers {values} to substract')
def step_imp(context, values):
    context.calc= Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc substract the values')
def step_imp(context):
    context.total = context.calc.restar(context.values[0],context.values[1])

@then('the substract is {total:d}')
def step_imp(context, total):
    assert (context.total == total)

#product
@given('two numbers {values} to product')
def step_imp(context, values):
    context.calc= Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc product the values')
def step_imp(context):
    context.total = context.calc.multiplicar(context.values[0],context.values[1])

@then('the product is {total:d}')
def step_imp(context, total):
    assert (context.total == total)

#divide
@given('two numbers {values} to divide')
def step_imp(context, values):
    context.calc= Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc divide the values')
def step_imp(context):
    context.total = context.calc.dividir(context.values[0],context.values[1])

@then('the divide is {total}')
def step_imp(context, total):
    if total == "operationError":
        assert (context.total == "operationError")
    else:
        assert (context.total == float(total))

#power
@given('two numbers {values} to power')
def step_imp(context, values):
    context.calc= Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc power the values')
def step_imp(context):
    context.total = context.calc.potenciar(context.values[0],context.values[1])

@then('the power is {total}')
def step_imp(context, total):
    assert (context.total == float(total))

#factorial
@given('one number {values} to factorial')
def step_imp(context, values):
    context.calc= Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc factorial the value')
def step_imp(context):
    context.total = context.calc.fatorial(context.values[0])

@then('the factorial is {total}')
def step_imp(context, total):
    if total == "operationError":
        assert (context.total == "operationError")
    else:
        assert (context.total == int(total))