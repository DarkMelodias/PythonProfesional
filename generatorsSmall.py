from time import sleep
from typing import Generator

def fibonacci_gen(max:int = 0) -> Generator:
    a, b , counter= 0, 1, 0
    while counter < max:
        yield a
        a, b = b, a+b
        counter += 1

def run():
    num: int = int(input("Digite cuantos numeros quiere ver: "))
    fibonacci = fibonacci_gen(num)
    for element in fibonacci:
        print(element)
        sleep(0.5)


if __name__ == "__main__":
    run()