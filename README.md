# Proxmark3 Commands

[Proxmark Wiki](https://github.com/Proxmark/proxmark3/wiki)

## Low Frequency (LF)
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
Old cards (HT)
Old tags (DW) 
```
lf em 410x reader
lf em 410x clone --id <card_id>
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

## High  Frequency (HF)
```
hf search
```

### ISO 14443-A / Mifare Classic 1K
| Type | Gen |
|---|---|
| UID | Magic Gen 1 (backdoor command 20:23 auth) |
| CUID | Magic Gen 2 (Mifare Classic Tool compatible direct write) |
| GDM / USCUID | Magic Gen 4 |
```
hf mf info
hf mf autopwn

hf mf wipe
hf mf restore
hf mf dump --ns

hf mf chk
hf mf nested --4k --blk <Blk> -a -k <key A>
```

### MIM256 / LEGIC Prime tag
Blue bracelet
```
hf legic info
```

## Links
1. [MIFARE Classic: exposing the static encrypted nonce variant](https://eprint.iacr.org/2024/1275.pdf)
2. [Mifare HowTo](https://github.com/Proxmark/proxmark3/wiki/Mifare-HowTo)
3. [Study of vulnerabilities in MIFARE Classic cards](https://www.sidechannel.blog/en/mifare-classic-2/)
