from behave import given,then

@given('I will "{}" Ammu today')
def parameter_testing(context,action):
    print("The item is : {}".format(action))
    # action = 'call'
    if action.lower() == "text":
        print('Yesss')
    else:
        print('Nooooo')

@then('Will i be hurrying things')
def step_impl(context):
    pass
