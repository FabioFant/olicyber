# Not solved yet

def pair_strings(a1, a2, a3, a4):
    v4 = 0
    v5 = 0
    v6 = 0
    v7 = 0
    v10 = 0
    v11 = 0
    v12 = 0
    result = 0
    
    while True:
        if v11 >= a4:
            result = v12
            if v12 >= a4:
                break
        
        if (v10 & 1) != 0:  # If v10 is odd
            v4 = v12
            v12 += 1
            v5 = a3[v4]
        else:
            v7 = v11
            v11 += 1
            v5 = a2[v7]
        
        v6 = v10
        v10 += 1
        a1[v6] = v5

    return result

def make_serial(a1, a2):
    pair_strings(a2, a1[18:], a1[9:18], 8)
    pair_strings(a2[16:], a1[:18], a1[9:18], 8)
    pair_strings(a2[32:], a1[9:18], a1[:9], 8)

    result = a2
    a2[48] = '\0'
    return result

id = "FrE7lWcr-9BiRR0dR-5zxGcTUz"
str = [''] * 64
chiave = make_serial(id, str)
chiave = ''.join(chiave)
print(chiave)

