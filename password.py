import random

caracteres = "!#$%()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
cant = 15

res = random.sample(caracteres, cant)
password = "".join(res)
print(password)