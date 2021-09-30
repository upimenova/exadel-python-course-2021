import time
import functools


def measure_elapsed_time(func):
    @functools.wraps(func)
    def calculate(*args, **kwargs):
        start = time.perf_counter()
        print(f'calling {func.__name__!r}')
        value = func(*args, **kwargs)
        end = time.perf_counter()
        complete = format(float(end - start), '.1f')
        print(f'{func.__name__!r} call took {complete} seconds')
        return value
    return calculate


@measure_elapsed_time
def my_fn1(arg1, arg2):
    time.sleep(0.5)
    return arg1 + arg2


@measure_elapsed_time
def my_fn2():
    time.sleep(0.8)
    print("I do nothing! What a life")


@measure_elapsed_time
def my_fn3(arg1, **kwargs):
    time.sleep(0.3)
    print(f"I also do nothing, but I have arg1 = {arg1} and kwargs = {kwargs}")


print("my_fn1 result:", my_fn1(1, 2))
my_fn2()
my_fn3(12, kwarg1='lol', kwarg2='kek')
