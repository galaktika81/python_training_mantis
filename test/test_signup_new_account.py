from generator.random import random_name

def test_signup_new_account(app):
    username = random_name('user_', 10)
    email = username + "@loalhost"
    password = "test"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()