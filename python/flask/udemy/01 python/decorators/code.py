# simple decorator
user = {"username": "jose", "access_level":"admin"}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())

# @ syntax for decorators
import functools

def make_secure2(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    
    return secure_function

@make_secure2
def get_admin_password2():
    return "1234"

print(get_admin_password2())
print(get_admin_password2.__name__)