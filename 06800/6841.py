import sys

read = sys.stdin.readline

while True:
    s = read().rstrip()
    if s == "CU":
        print("see you")
    elif s == ":-)":
        print("I'm happy")
    elif s == ":-(":
        print("I'm unhappy")
    elif s == ";-)":
        print("wink")
    elif s == ":-P":
        print("stick out of my tongue")
    elif s == "(~.~)":
        print("sleepy")
    elif s == "TA":
        print("totally awesome")
    elif s == "CCC":
        print("Canadian Computing Competition")
    elif s == "CUZ":
        print("because")
    elif s == "TY":
        print("thank-you")
    elif s == "YW":
        print("you're welcome")
    elif s == "TTYL":
        print("talk to you later")
        break
    else:
        print(s)