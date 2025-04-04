def test_login_page_title(login_page):
    login_page.go_to_login()
    assert "Login" in login_page.get_title()

def test_login_with_invalid_credentials(login_page):
    login_page.login("wronguser", "wrongpass")
    assert login_page.is_error_displayed()