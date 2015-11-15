from generator.random import random_name

def test_signup_new_account(app):
    username = random_name('user_', 10)
    email = username + "@loalhost"
    password = "test"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)