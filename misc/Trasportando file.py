import os
import re
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_files():
    # Collect all .enc files in the current directory
    enc_files = [f for f in os.listdir() if f.endswith('.enc')]
    
    # Regex to extract base filename and chunk index
    pattern = re.compile(r'^(.*?)_([0-9]{2})\.enc$')
    
    # Group files by their original filename
    groups = {}
    for filename in enc_files:
        match = pattern.match(filename)
        if not match:
            continue
        base = match.group(1)
        index = int(match.group(2))
        if base not in groups:
            groups[base] = []
        groups[base].append((index, filename))
    
    # Process each group to decrypt and combine chunks
    for base in groups:
        # Sort chunks by index
        chunks = sorted(groups[base], key=lambda x: x[0])
        
        # Decrypt each chunk and write to the output file
        with open(base, 'wb') as outfile:
            for index, filename in chunks:
                with open(filename, 'rb') as infile:
                    enc_data = infile.read()
                
                # Derive key from the original filename
                key = sha256(base.encode()).digest()
                iv = b'\x00' * 16
                cipher = AES.new(key, AES.MODE_CBC, iv)
                
                # Decrypt and unpad the chunk
                decrypted_data = cipher.decrypt(enc_data)
                try:
                    unpadded_data = unpad(decrypted_data, AES.block_size)
                except ValueError as e:
                    print(f"Error unpadding {filename}: {e}")
                    continue
                
                outfile.write(unpadded_data)
        
        print(f"Decrypted '{base}' successfully.")

if __name__ == "__main__":
    decrypt_files()