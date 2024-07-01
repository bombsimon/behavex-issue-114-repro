import sys

from behave import given, then, when


@given("we have behave installed")
def is_installed(_):
    pass


@when("we run a test")
def run_a_test(context):
    context.test_is_completed = True


@then("the test is completed")
def test_is_completed(context):
    assert context.failed is False
    assert context.test_is_completed is True


@given("we run a test that exits")
def run_hanging_test(_):
    # This might just as well be a segfault or crash making the process die, it
    # simply represents the process no longer living.
    sys.exit(0)


@then("we never reach here")
def never_reached(_):
    assert True
