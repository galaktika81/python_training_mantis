
import time
def test_login(app):
    time.sleep(3)
    app.session.login("administrator", "root")
    time.sleep(10)
    assert app.session.is_logged_in_as("administrator")