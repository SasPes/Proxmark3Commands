# MIFARE DESFire

String to Hex → https://dencode.com/en/string/hex   
Hex to String → https://dencode.com/en/string

## MIFARE DESFire EV3 4K
<img src="img/MIFARE-DESFire-EV3" width="350">

### Change master key on a new card
```sh
# Set new card master key (AES)
hf mfdes changekey -t des --newalgo aes --newkey 11223344556677889900112233445566

# List all apps with the new key
hf mfdes lsapp -t aes -k 11223344556677889900112233445566

# Change card master key
hf mfdes changekey -t aes -k 11223344556677889900112233445566 --newkey 54686973206973206120746573742121

# List all apps with the new changed key
hf mfdes lsapp -t aes -k 11223344556677889900112233445566

# Set default profile to AES
hf mfdes default -n 0 -t aes -k 54686973206973206120746573742121

# List all apps with the new default AES config
hf mfdes lsapp

# Check free memory
hf mfdes freemem

# Format the card
hf mfdes formatpicc
```

### Revert master key to default
```sh
# List all apps
hf mfdes lsapp
hf mfdes lsapp --no-auth

# Change card master key from AES to DES (default)
hf mfdes changekey -t aes -k 54686973206973206120746573742121 --newalgo des --newkey 0000000000000000

# Set default profile to DES (default)
hf mfdes default -n 0 -t des -k 0000000000000000
```

### Other ...
```
hf mfdes createapp --aid 123456 --fid 2345 --dfname aid123456 --dstalgo aes

[usb] pm3 --> hf mfdes changekey --aid 123456 -t aes --newkey 54686973206973206120746573742121 --oldkey 11223344556>
[=] Changing key for AID 123456
[=] auth key 0: aes [16] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
[=] changing key number  0x00 (0)
[=] old key: aes [16] 11 22 33 44 55 66 77 88 99 00 11 22 33 44 55 66
[=] new key: aes [16] 54 68 69 73 20 69 73 20 61 20 74 65 73 74 21 21
[=] new key version: 0x00
[+] Change key ( ok )

hf mfdes changekey -t des --oldkey 54686973206973206120746573742121  --newkey 0000000000000000
hf mfdes changekey --aid 123456 -t aes --key 54686973206973206120746573742121 --newkey 00000000000000000000000000000000

hf mfdes auth --aid 123456 -n 0 -t AES -k 00000000000000000000000000000000
```
