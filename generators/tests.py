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

