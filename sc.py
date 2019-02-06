def closest_mod_5(x):
    if x % 5 == 0 and x!=0:
        return x
    else:
        import math
        x = 5* (x//5) +5
    return x
print(closest_mod_5(51))