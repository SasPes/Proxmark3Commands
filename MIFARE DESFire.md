# MIFARE DESFire

String to Hex → https://dencode.com/en/string/hex   
Hex to String → https://dencode.com/en/string

## MIFARE DESFire EV3 4K
<img src="img/MIFARE-DESFire-EV3.png" width="300">

### How to store recovery codes on MIFARE DESFire EV3

```sh
# GitHub - example recovery codes
c9sye-vpw90
so7aw-4f82w
z9a73-3deh2

# Set new card master key (AES) → key: This is a test!!
hf mfdes changekey -t des --newalgo aes --newkey 54686973206973206120746573742121

# Set default profile to AES
hf mfdes default -n 0 -t aes -k 54686973206973206120746573742121

# Create app
hf mfdes createapp --aid 000001 --fid 0001 --dfname github --dstalgo aes --ks1 0B --ks2 AE

# Set app key
hf mfdes changekey --aid 000001 -t aes --key 00000000000000000000000000000000 --newkey 54686973206973206120746573742121

# Create file (ex. 01)
hf mfdes createfile --aid 000001 --fid 01 --isofid 0001 --size 000100 --rrights key0 --wrights key0 --rwrights key0 --chrights key0

# Write data to file 01 (ex. recovery codes: c9sye-vpw90, so7aw-4f82w, z9a73-3deh2")
hf mfdes write --aid 000001 --fid 01 -d 63397379652d7670773930 -o 000000
hf mfdes write --aid 000001 --fid 01 -d 736f3761772d3466383277 -o 000010
hf mfdes write --aid 000001 --fid 01 -d 7a396137332d3364656832 -o 000020

# Read all github recovery codes
hf mfdes read --aid 000001 --fid 01

[=] ------------------------------- File 01 data -------------------------------
[+] Read 256 bytes from file 0x01 offset 0
[=]  Offset  | Data                                            | Ascii
[=] ----------------------------------------------------------------------------
[=]   0/0x00 | 63 39 73 79 65 2D 76 70 77 39 30 00 00 00 00 00 | c9sye-vpw90.....
[=]  16/0x10 | 73 6F 37 61 77 2D 34 66 38 32 77 00 00 00 00 00 | so7aw-4f82w.....
[=]  32/0x20 | 7A 39 61 37 33 2D 33 64 65 68 32 00 00 00 00 00 | z9a73-3deh2.....
[=]  48/0x30 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=]  64/0x40 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=]  80/0x50 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=]  96/0x60 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 112/0x70 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 128/0x80 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 144/0x90 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 160/0xA0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 176/0xB0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 192/0xC0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 208/0xD0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 224/0xE0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 240/0xF0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
```

### Step by step with explanation

#### Change master key on a new card
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

#### Revert master key to default
```sh
# List all apps
hf mfdes lsapp
hf mfdes lsapp --no-auth

# Change card master key from AES to DES (default)
hf mfdes changekey -t aes -k 54686973206973206120746573742121 --newalgo des --newkey 0000000000000000

# Set default profile to DES (default)
hf mfdes default -n 0 -t des -k 0000000000000000
```

#### Create app with recovery codes
```sh
# Create app
hf mfdes createapp --aid 000001 --fid 0001 --dfname github  --dstalgo aes

# List all apps
hf mfdes lsapp

# Create file (ex. 01)
hf mfdes createfile --aid 000001 --fid 01 --isofid 0001 --size 000100

# List all files
hf mfdes getfileids --aid 000001

# Write data to file 01 (ex. recovery codes "c9sye-vpw90")
hf mfdes write --aid 000001 --fid 01 -d 63397379652d7670773930

# Read all files
hf mfdes read --aid 000001

# Write data to file 01 (ex. recovery codes "c9sye-vpw90 & so7aw-4f82w & z9a73-3deh2 & ...")
hf mfdes write --aid 000001 --fid 01 -d 63397379652d7670773930 -o 000000
hf mfdes write --aid 000001 --fid 01 -d 736f3761772d3466383277 -o 000010
hf mfdes write --aid 000001 --fid 01 -d 7a396137332d3364656832 -o 000020

# Read all github recovery codes
hf mfdes read --aid 000001 --fid 01
[=] ------------------------------- File 01 data -------------------------------
[+] Read 256 bytes from file 0x01 offset 0
[=]  Offset  | Data                                            | Ascii
[=] ----------------------------------------------------------------------------
[=]   0/0x00 | 63 39 73 79 65 2D 76 70 77 39 30 00 00 00 00 00 | c9sye-vpw90.....
[=]  16/0x10 | 73 6F 37 61 77 2D 34 66 38 32 77 00 00 00 00 00 | so7aw-4f82w.....
[=]  32/0x20 | 7A 39 61 37 33 2D 33 64 65 68 32 00 00 00 00 00 | z9a73-3deh2.....
[=]  48/0x30 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=]  64/0x40 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=]  80/0x50 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=]  96/0x60 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 112/0x70 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 128/0x80 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 144/0x90 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 160/0xA0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 176/0xB0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 192/0xC0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 208/0xD0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 224/0xE0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
[=] 240/0xF0 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................

# Delete file
hf mfdes deletefile --aid 000001 --fid 01

# Delete app
hf mfdes deleteapp --aid 000001
```

### Links
1. https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/ndef_type4a.md
2. https://x41-dsec.de/lab/blog/telenot-complex-insecure-keygen/
