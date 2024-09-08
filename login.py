class LoginInterface:
    def authenticate(self, username, password):
        pass


class AdminLogin(LoginInterface):
    ADMIN_NAME = "admin"
    ADMIN_PASSWORD = "admin"

    def authenticate(self, username, password):
        return username == self.ADMIN_NAME and password == self.ADMIN_PASSWORD
