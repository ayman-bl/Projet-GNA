class XOR_NRBG:
    def __init__(self, gen_a, gen_b):
        self.gen_a = gen_a
        self.gen_b = gen_b

    def next_byte(self):
        byte_a = self.gen_a.next() % 256
        
        try:
            byte_b = next(self.gen_b) % 256
        except TypeError: 
            byte_b = self.gen_b.next() % 256
            
        return byte_a ^ byte_b