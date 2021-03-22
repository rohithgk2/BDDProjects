from behave import given, then
from login import login
import logging as logger

@given('I am the first sample')
def first_sample(context):
    login.login_function()
    pass

@then('I should be the first sample')
def confirm_sample(context):
    logger.info("1 Info")
    pass

@given('I am in subdir')
def subdir_function(context):
    logger.debug('2 DEBUG')
    pass
@then('I am also running')
def subdir_final(context):
    logger.debug('ERROR')
    assert 1 ==2
