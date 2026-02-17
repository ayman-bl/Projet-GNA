def shannon_entropy(data):
    counts = Counter(data)
    entropy = 0
    for count in counts.values():
        p = count / len(data)
        entropy -= p * math.log2(p)
    return entropy

def chi_square_test(data):
    counts = Counter(data)
    expected = len(data) / 256
    chi2 = 0
    for i in range(256):
        observed = counts.get(i, 0)
        chi2 += (observed - expected) ** 2 / expected
    return chi2


def autocorrelation(data, lag=1):
    n = len(data)
    mean = sum(data) / n

    num = 0
    den = 0

    for i in range(n - lag):
        num += (data[i] - mean) * (data[i + lag] - mean)

    for i in range(n):
        den += (data[i] - mean) ** 2

    return num / den

def ks_test(data):
    normalized = [x / 255 for x in data]
    return stats.kstest(normalized, 'uniform')

def shannon_entropy(data):
    counts = Counter(data)
    entropy = 0
    for count in counts.values():
        p = count / len(data)
        entropy -= p * math.log2(p)
    return entropy

def chi_square_test(data):
    counts = Counter(data)
    expected = len(data) / 256
    chi2 = 0
    for i in range(256):
        observed = counts.get(i, 0)
        chi2 += (observed - expected) ** 2 / expected
    return chi2


def autocorrelation(data, lag=1):
    n = len(data)
    mean = sum(data) / n

    num = 0
    den = 0

    for i in range(n - lag):
        num += (data[i] - mean) * (data[i + lag] - mean)

    for i in range(n):
        den += (data[i] - mean) ** 2

    return num / den

def ks_test(data):
    normalized = [x / 255 for x in data]
    return stats.kstest(normalized, 'uniform')

from mt19937.py import mt19937
from os_random.py import os_random

N = 1_000_000  # 1 million d’octets

print("=== MT19937 ===")
mt_data = generate_mt_bytes(N)

print("Entropie:", shannon_entropy(mt_data))
print("Chi²:", chi_square_test(mt_data))
print("Autocorr:", autocorrelation(mt_data))
print("KS:", ks_test(mt_data))


print("\n=== os.urandom ===")
os_data = generate_os_bytes(N)

print("Entropie:", shannon_entropy(os_data))
print("Chi²:", chi_square_test(os_data))
print("Autocorr:", autocorrelation(os_data))
print("KS:", ks_test(os_data))
