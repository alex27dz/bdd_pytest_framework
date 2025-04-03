from behave import given, when, then
from pages.login_page import LoginPage

@given("the user is on the login page")
def step_impl(context):
    context.page = LoginPage(context.driver)
    context.page.open_login_page()

@when("the user enters valid credentials")
def step_impl(context):
    context.page.login("alex27dz@gmail.com", "NV27vnmc")

@then("the user should be redirected to the dashboard")
def step_impl(context):
    assert context.page.is_dashboard_displayed()
