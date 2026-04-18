from behave import when, then
from selenium.webdriver.common.by import By

# 🔹 Task 7a: Button Click
@when('I click the "{button}" button')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, f"//button[text()='{button}']").click()


# 🔹 Task 7b: Verify text is present
@then('I should see "{text}" in the page')
def step_impl(context, text):
    assert text in context.driver.page_source


# 🔹 Task 7c: Verify text is NOT present
@then('I should not see "{text}" in the page')
def step_impl(context, text):
    assert text not in context.driver.page_source


# 🔹 Task 7d: Verify message is present
@then('I should see the message "{message}"')
def step_impl(context, message):
    body = context.driver.find_element(By.TAG_NAME, "body").text
    assert message in body
