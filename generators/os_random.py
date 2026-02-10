import os

def os_random(n):
    random_bytes = os.urandom(n)
    return(random_bytes)

print(os_random(1000))