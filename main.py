import Encrypt

if __name__ == '__main__':
    msg = "Welcome to Codebusters!"
    print(f"Plaintext: {msg}")
    print(f"Length: {len(msg)}")
    print(f"Aristocrat: {Encrypt.aristocrat(msg)}")
    print(f"Caesar: {Encrypt.rot(msg, 13)}")
    print(f"Rail Fence: {Encrypt.railFence(msg, 2)}")
    print(f"Vigenere: {Encrypt.vigenere(msg, 'TJSCIOLY')}")
    print(f"Patristocrat: {Encrypt.patristocrat(msg)}")
    print(f"Atbash: {Encrypt.atbash(msg)}")
    print(f"Hill: {Encrypt.hill(msg, 'TJSCIOLY')}")
    print(f"Affine: {Encrypt.affine(msg, 3, 12)}")
