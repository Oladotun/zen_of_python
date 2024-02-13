'''
In flat is better than nested, the principle is that creating nested logic statements or loops
may complete a code quality, instead having a function call that is more direct is preferred
'''

def get_user_login(user= {'is_logged_in': False }, amount= 0):
    if user:
        if user['is_logged_in']:
            if amount > 0:
                print("bill paid")
            else:
                raise Exception("Invalid Amout")
        else:
            raise Exception("User not logged in")
    else:
        raise Exception("User doesnt exist")

print("the below code will run, but the code was written with",
       " multiple nested statement that is not needed")
user_login = {}
user_login["is_logged_in"] = True
amount = 10 
get_user_login(user_login, amount)

def get_user_login_flat(user= {'is_logged_in': False }, amount= 0):
    if not user:
        raise Exception("User doesnt exist")
    if not user['is_logged_in']:
        raise Exception("User not logged in")
    if amount <= 0:
        raise Exception("Invalid amount")
    
    print("bill said")
print("the below code was created with a flat approach",
      " the idea is put the negate logic first to check")
get_user_login_flat(user_login, amount)