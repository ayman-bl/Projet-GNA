def lcg_generator(seed, a=1664525, c=1013904223, m=2**32):
    state = seed #pos actuelle dans la séquence
    while True:
        state = (a * state + c) % m
        yield state #renvoie le nombre et met la fonction en pause 

