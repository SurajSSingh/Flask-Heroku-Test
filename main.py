# New Change
from flask import Flask
import random
import cv2

app = Flask(__name__)

GREETINGS = ["Hello", "Hi", "Good Day", "Hola"]


@app.route("/greeting/<name>")
def greeting(name=""):
    return random.sample(GREETINGS, 1)[0] + " " + name


@app.route("/compare/<x>/<y>")
def compare(x, y):
    x, y = int(x), int(y)
    if x < y:
        print("X is smaller than Y")
        return "X is smaller than Y"
    elif x > y:
        print("X is bigger than Y")
        return "X is bigger than Y"
    else:
        print("X is the same as Y")
        return "X is the same as Y"


def super_compare(min_x, max_x, y):
    for x in range(min_x, max_x+1):
        compare(x, y)


@app.route("/check/<num>")
def check_num(num):
    try:
        num = int(num)
        if num % 2 == 0:
            return "Even Number"
        else:
            return "Odd Number"
    except:
        return "Invalid Number Type: " + str(num) + " is a " + str(type(num)) + ", not an integer"


@app.route("/sum/<n>")
def get_sum(n):
    total = 0
    n = int(n)
    for i in range(1, n+1):
        total += i

    return str(total)


@app.route("/")
def index():
    return "WORKING"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
