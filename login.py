class LoginInterface:
    def authenticate(self, username, password):
        pass


class AdminLogin(LoginInterface):
    ADMIN_NAME = "ADMIN"
    ADMIN_PASSWORD = "1234"

    def authenticate(self, username, password):
        return username == self.ADMIN_NAME and password == self.ADMIN_PASSWORD
