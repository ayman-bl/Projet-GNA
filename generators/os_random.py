import os

def os_random(n):
    random_bytes = os.urandom(n)
    return(random_bytes)


