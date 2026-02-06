from lcg import lcg_generator
## test de LCG
gen = lcg_generator(seed=42)
print([next(gen) for _ in range(5)])
