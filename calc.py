def add(x, y):
    return x + y


def multiply(x, y):
    return x*y


def divide(x, y):
    try:
        return x / y
    except Exception as e:
        print("Error : {}".format(e))
