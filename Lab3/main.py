from funcs import *

if __name__ == "__main__":
    print(welcome_message())
    print(greet_user("Timur"))

    user = create_user()
    print(user)

    message = send_message("Alex", "Nikita", "Hi there!", urgent=True)
    print(message)

    users_list = list_users("Alex", "Nikita", "Pasha")
    print(users_list)

    info = user_info(username="Alex", age=20, role="admin")
    print(info)

    print(announce_new_user("Pasha"))

    print(execute_function(lambda: "Something"))
    print(repeat_function(lambda: "Repeat me", 3))
    print(call_with_username(greet_user, "DurkaVerder"))

    print(log_user_action("Alex", "login"))
    print(notify_admin("Pasha", "Server down"))

    print(say_hello_lambda())
    print(greet_lambda("Pasha"))
    print(call_lambda(lambda: "Calling from call_lambda"))

    greeter = make_greeter("Nikita")
    print(greeter())

    logger = make_message_logger("INFO")
    print(logger("System started"))

    counter = make_user_counter()
    print(counter())
    print(counter())
    print(counter())
