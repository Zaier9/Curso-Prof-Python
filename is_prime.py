def is_prime(num: int) -> int:
    counter: int = 0
    for i in range(1, num + 1):
        if i == 1 or i == num:
            continue
        elif num % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

def run():
    num: int = int(input('Escribe un numero por favor:'))
    if is_prime(num) == True:
        print('Es un numero primo')
    else:
        print('No es un numero primo :(')


if __name__ == '__main__':
    run()

