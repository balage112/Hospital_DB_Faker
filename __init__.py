from A_app_operations_04 import *


def app(user_action):
    app_functions.get(user_action)()

end= False
while not end:
    action = input(opening_phrase)
    if action.lower() == "e":
        end = True
    if action in app_functions:
        app(action)
    else:
        print("Invalid option. Please try it again")