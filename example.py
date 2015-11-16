import time

from victor import debug


@debug
def greet(first, last):
    time.sleep(0.02)
    return "Hello, {} {}!".format(first, last)


if __name__ == '__main__':
    greet("Jonathan", "Como")
