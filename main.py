import random, sys, os, rabinMiller, cryptomath
import math
import rsa.randnum
aes_key = rsa.randnum.read_random_bits(128)# Создаем случайный ключ 128 бит
def binary_gcd(num1, num2):
    shift = 0
    # Если одно из чисел равно нулю, делитель - другое число
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    # Если num1 = 1010, а num2 = 0100, то num1 | num2 = 1110
    # 1110 & 0001 == 0, тогда происходит сдвиг, который фиксируется в shift
    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1
    #Если True, значит num1 - четное, иначе - нечетное
    while num1 & 1 == 0:
        # если нечетное, сдвигаем на один бит
        num1 >>= 1
    while num2 != 0:
        # пока число нечётное, сдвигаем на один бит
        while num2 & 1 == 0:
            num2 >>= 1
        # если первое число больше второго
        if num1 > num2:
            # меняем их местами
            num1, num2 = num2, num1
        #теперь первое число меньше второго, вычитаем
        num2 -= num1
    # возвращаем число, перед этим сдвинув его биты на shift
    return num1 << shift

def encrypt(Message, e, n):
    arr = []
    for word in Message:
        arr.append(pow(int(word), e, n))
    return arr

def decrypt(Message, n, d):
    C = []
    for word in Message:
        C.append(pow(int(word), d,  n))
    return C

def Euclid(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

def encode_ASCII(str):
    ascii = []
    for char in str:
        ascii.append(ord(char))
    return ascii

def decode_ASCII(str):
    ascii = []
    for ask in str:
        ascii.append(chr(ask))
    return ascii

def are_relatively_prime(a, b):
    """Return ``True`` if ``a`` and ``b`` are two relatively prime numbers.

    Two numbers are relatively prime if they share no common factors,
    i.e. there is no integer (except 1) that divides both.
    """
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True


def get_d(i, F):

    return cryptomath.findModInverse(i, F)
def get_e(F):
    e = 0
    i = 2
    while i < F:
        # e = Euclid(F, i)
        e = math.gcd(F, i)
        if e == 1:
            e = i
            break
        i += 1
    return e

def generateKey(message, KeySize=62):
    p = rabinMiller.generateLargePrime(KeySize)
    q = rabinMiller.generateLargePrime(KeySize)
    n = p * q
    print(f'len N = {len(str(n))}')
    F = (p - 1) * (q - 1)
    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    e = get_e(F)
    d = get_d(e, F)
    publicKey = (n, e)
    privateKey = (n, d)
    print(f'publicKey: {publicKey}')
    print(f'privateKey: {privateKey}')
    ASKII = encode_ASCII(message)
    encode_massage = encrypt(ASKII, e, n)
    print("Зашифрованное сообщение: " + str(encode_massage))
    word = decrypt(encode_massage, n, d)
    ASKII = decode_ASCII(word)
    print("Расшифрованное сообщение: " + str(ASKII))
    return (publicKey, privateKey)




print("Введите сообщение: ")
message = str(input())
(n, e), (k, d) = generateKey(message)







