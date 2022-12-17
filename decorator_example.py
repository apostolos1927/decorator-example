import random
from functools import wraps
from time import sleep


def check(number):
    num = random.randint(0, 10)
    print("Random Number is ", num)
    if num == number:
        return True
    else:
        raise Exception


def retry(num_retry, sleep_sec):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """A wrapper function"""
            for retry_num in range(1, num_retry):
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    print("Number of retry ", retry_num)
                    sleep(sleep_sec)

        return wrapper

    return decorator


@retry(20, 2)
def check_number(number):
    """This is docstring for check_number function"""
    if check(number):
        print("Lucky number is ", number)


if __name__ == "__main__":
    number = 4
    check_number(number)
    print(check_number.__name__)
    print(check_number.__doc__)
