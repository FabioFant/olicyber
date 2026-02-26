def decrypt(data):
    blen = len(data) // 4
    cols = [data[i:i+blen] for i in range(0, len(data), blen)]
    dec = ""
    for i in range(0, blen):
        for c in cols:
            dec += c[i]

    return dec

enc = "f{anuiraaso_lfltnfi_sin_aime_rotpze_gne_ca_roi}_"
print(decrypt(enc))