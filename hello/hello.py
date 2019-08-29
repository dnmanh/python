import sys

import requests

print(sys.version)
print(sys.executable)

name = input("Your name?")
print("Hello {}".format(name))


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Manh"))
r = requests.get("http://justforlearning.xyz:9090")
print(r.status_code)
