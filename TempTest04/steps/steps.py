from behave import given,when,then

@given('I have a email created')
def email_creation(context):
    print("Creating a email id")
    context.email_id = 'test@test.com'
    print('The mail id created is {}'.format(context.email_id))

@when('I login using the email')
def login_usingemail(context):
    print("The email id used is {}".format(context.email_id))

@then('I should see the email')
def display_email(context):
    print('The email seen while logging in is {}'.format(context.email_id))