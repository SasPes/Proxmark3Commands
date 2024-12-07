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
Old cards/tags
```
lf em 410x reader
lf em 410x clone --id <card_id>
```

### EM4x05 / EM4x69 / Indala ID
Old cards/tags
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

### MIM256 / LEGIC Prime tag
Blue bracelet
```
hf legic info
```
