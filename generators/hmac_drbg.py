import hmac
import hashlib

class HMAC_DRBG:
    def __init__(self, entropy, nonce=b"", personalization_string=b""):
        self.K = b"\x00" * 32
        self.V = b"\x01" * 32
        seed_material = entropy + nonce + personalization_string
        self._update(seed_material)
        self.reseed_counter = 1

    def _update(self, data=None):
        self.K = hmac.new(self.K, self.V + b"\x00" + (data if data else b""), hashlib.sha256).digest()
        self.V = hmac.new(self.K, self.V, hashlib.sha256).digest()
        if data:
            self.K = hmac.new(self.K, self.V + b"\x01" + data, hashlib.sha256).digest()
            self.V = hmac.new(self.K, self.V, hashlib.sha256).digest()

    def generate(self, num_bytes):
        temp = b""
        while len(temp) < num_bytes:
            self.V = hmac.new(self.K, self.V, hashlib.sha256).digest()
            temp += self.V
        
        output = temp[:num_bytes]
        self._update(None)
        self.reseed_counter += 1
        return output