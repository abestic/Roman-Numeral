from behave import *
from roman import *

#  Note: there is a weird python quirk with ranges - the stop point is NOT included in the range

@given(u'{input} is a valid integer')
def step_impl(context, input):
  assert(int(input) in range(1, 4000))            # Confirm the input is an integer in the accepted range.

@given(u'{input} is not a valid integer')
def step_impl(context, input):
  assert(int(input) not in range(1, 4000))        # Confirm the input is an integer outside the accepted range.

@given(u'{input} is not an integer')
def step_impl(context, input):
    try:
      int(input)                                  # Attempt to convert the input string to an integer.
    except:                                       # If the attempt fails, confirm the input's type
      assert(type(input) != "<class 'int>")       # is still something other than an integer.



@when(u'I enter {input}')
def step_impl(context, input):
  context.number = None                               # Note: 'None' is a non-type object.
  try:
    context.number = int(input)                       # Identify integer inputs and assign them
    assert(type(context.number) == "<class 'int'>")   # to the 'number' variable to be converted.
  except:                                             
    assert(type(context.number) != "<class 'int'>")   # Identify non-integer intputs but do not assign them
                                                      # to the 'number' variable (they cannot be converted).



@then(u'I should see {numeral}')
def step_impl(context, numeral):
  context.numeral = convert(context.number)           # Convert the integer number into a Roman numeral
  assert(context.numeral == numeral)                  # and confirm it matches the intended result

@then(u'I should receive an error')
def step_impl(context):
  try:
    convert(context.number)
  except:
    assert(True)                                       # Confirm an error is raised when trying to convert
                                                       # a non-integer or invalid integer value