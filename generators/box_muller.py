import math
import random

def box_muller():
    u1, u2 = random.random(), random.random()    
    if u1 == 0: u1 = 1e-10 
    
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    z1 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)
    
    return z0, z1