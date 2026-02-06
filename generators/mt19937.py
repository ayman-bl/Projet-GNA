def mt19937(seed):
    MT = [0]*624
    index = 0

    # initialisation
    MT[0] = seed
    for i in range(1, 624):
        MT[i] = (1812433253 * (MT[i-1] ^ (MT[i-1] >> 30)) + i) & 0xFFFFFFFF

    while True:
        if index == 0:
            # twist
            for i in range(624):
                y = (MT[i] & 0x80000000) + (MT[(i+1) % 624] & 0x7FFFFFFF)
                MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
                if y % 2 != 0:
                    MT[i] ^= 0x9908B0DF

        y = MT[index]

        # tempering (version minimale)
        y ^= (y >> 11)
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= (y >> 18)

        index = (index + 1) % 624
        yield y & 0xFFFFFFFF
