def get_prime_factors(val):
    pf = []
    prime_fact = 2
    while prime_fact <= val:
        if val % prime_fact == 0:
            pf.append(prime_fact)
            val = val // prime_fact
        else:
            prime_fact += 1
    return pf
