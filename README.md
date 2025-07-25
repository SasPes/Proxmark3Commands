# Proxmark3 Commands
<img src="img/RFID-Card-3-e1587108734574.png" width="350"> <img src="img/pm3easy.png" width="400">

## Low Frequency (LF)
125 KHz or 134.2 KHz   
Protocol: ISO 11784 / 11785   
Short reading range, around 1-5 cm   
   
```
lf search
```

### T55xx
```
lf t55xx config
lf t55xx dump
lf t55xx wipe
```

### EM 410x / T55xx
Old cards (H,T)   
Old tags (DW) 
```
lf em 410x reader
lf em 410x clone --id <card_id>

lf t5 detect
```

### EM4x05 / EM4x69 / Indala ID
Old card (D)
```
lf em 4x05 info
lf em 4x05 chk
lf em 4x05 dump

lf indala reader
lf indala clone -r <raw>
```

---
   
<img src="img/RFID-Card-4-e1587108920704.png" width="350">

## High  Frequency (HF)
13.56 MHz   
Protocol: ISO 14443A / 14443B / 15693   
Short reading range, around 2-10 cm   
(ISO 15693 RFID cards & tags could reach up to around 1 meter)   

```
hf search
```

### ISO 14443-A / Mifare Classic
| Type | Gen |
|---|---|
| UID | Magic Gen 1 (backdoor command 20:23 auth) |
| CUID | Magic Gen 2 (Mifare Classic Tool compatible direct write) |
| GDM / USCUID | Magic Gen 4 |

Old card (SL)   
Old debit card (M,S)
Old gym card (247, P&T)
```
hf mf info
hf mf chk
hf mf autopwn
hf mf cview
hf mf view -f hf-mf-12345678-dump-001.bin

hf mf csetuid -u <UID>
hf mf wipe
hf mf restore
hf mf dump --ns

hf mf csetblk -b 063 -d 53617350657320546573742045563121
hf mf cwipe

hf mf nested --4k --blk <Blk> -a -k <key A>
```

### MIFARE Ultralight/C/NTAG
imagotag G1 retail 2.6 red NFC
```
hf mfu info
hf mfu keygen -r
hf mfu pwdgen -r
hf mfu dump
```
```
emv list
emv test
emv gpo
```

### MIFARE DESFire EV1
Old card (T)
```
hf mfdes info
hf mfdes default

hf mfdes freemem

hf mfdes lsapp
hf mfdes lsfiles --aid <AID> --no-auth

hf mfdes createapp --aid <AID> --fid 2345 --dfname aid<AID>

hf mfdes createfile --aid <AID> --fid 01 --isofid 0001 --size 000010
hf mfdes getfileids --aid <AID>

hf mfdes write --aid <AID> --fid 01 -d 53617350657320546573742045563121
hf mfdes read --aid <AID>

hf mfdes deletefile --aid <AID> --fid 01
hf mfdes deleteapp --aid <AID>

hf mfdes formatpicc
```

### eMRTD
Passport
Old card (MC, ID)
```
hf em info -n <DOC_NR> -d <birthday YYMMDD> -e <expiry date YYMMDD>
hf emrtd info -n <DOC_NR> -d <birthday YYMMDD> -e <expiry date YYMMDD> -i
```

### HID SEOS
Old card (D,ID)
```
hf seos info
hf seos managekeys -p
```

### MIM256 / LEGIC Prime tag
Old bracelet (Blue)
```
hf legic info
hf legic list
hf legic dump
```

## Links
1. [Getting started with the proxmark3 easy](https://forum.dangerousthings.com/t/getting-started-with-the-proxmark3-easy/9050)
2. [Windows binaries for the Proxmark3](https://www.proxmarkbuilds.org/)
3. [Proxmark Wiki](https://github.com/Proxmark/proxmark3/wiki)
4. [Proxmark 3 CheatSheet](https://tagbase.ksec.co.uk/resources/proxmark3-cheatsheet/)
5. [MIFARE Classic: exposing the static encrypted nonce variant](https://eprint.iacr.org/2024/1275.pdf)
6. [Mifare HowTo](https://github.com/Proxmark/proxmark3/wiki/Mifare-HowTo)
7. [Study of vulnerabilities in MIFARE Classic cards](https://www.sidechannel.blog/en/mifare-classic-2/)
8. [RFID / NFC Card](https://nexqo.com/portfolio-items/rfid-nfc-card/)
9. [Awesome RFID Talks](https://github.com/doegox/awesome-rfid-talks)
10. [Backing Up Your Amiibo With A Proxmark3](https://farewell-ladmin.com/backing-up-your-amiibo-with-a-proxmark3/)
11. [MIFARE DESFire](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/desfire.md)
12. [Electronic Machine Readable Travel Document - eMRTD](https://developers-old.innovatrics.com/digital-onboarding/docs/functionalities/document/nfc-reading/)
