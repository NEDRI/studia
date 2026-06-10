from decimal import Decimal, getcontext

def print_998001_sequence(limit=1000):
    getcontext().prec = limit * 3 + 10
    
    result = Decimal(1) / Decimal(998001)
    full_str = format(result, 'f').split('.')[1]
    
    for i in range(0, limit * 3, 3):
        chunk = full_str[i:i+3]
        print(chunk)

print_998001_sequence(1000)