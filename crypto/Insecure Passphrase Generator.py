words = [
    "casa", "albero", "notte", "sole", "montagna", "fiume", "mare", "vento", "nuvola", 
    "pioggia", "strada", "amico", "sorriso", "viaggio", "tempo", "cuore", "stella", 
    "sogno", "giorno", "libro", "porta", "luce", "ombra", "silenzio", "fiore", "luna"
]

passphrase_str = "fiume-amico-casa-mare-{-amico-tempo-viaggio-mare-_-sole-tempo-montagna-giorno-viaggio-libro-_-sorriso-montagna-casa-viaggio-_-giorno-montagna-notte-porta-sogno-montagna-_-vento-notte-fiume-luna-nuvola-strada-luna-luce-}"

decoded_chars = []
for part in passphrase_str.split('-'):
    if part in words:
        index = words.index(part)
        decoded_char = chr(ord('a') + index)
        decoded_chars.append(decoded_char)
    else:
        decoded_chars.append(part)

decoded_flag = ''.join(decoded_chars)
print(decoded_flag) # Ultima parte non corretta, è 'password'.