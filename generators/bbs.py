class BlumBlumShub:

    def __init__(self, p, q, seed):
        self.M = p * q
        self.state = seed

    def next_bit(self):
        self.state = pow(self.state, 2, self.M)
        return self.state % 2