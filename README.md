# traeskibetbetty.dk

# Installation

Find guides on https://gohugo.io/getting-started/quick-start/

After cloning repository run this command to setup Papermod (The theme for this website)

```
git submodule update --init --recursive # needed when you reclone your repo (submodules may not get cloned automatically)
```

```
hugo serve
```

For at konvertere et dokument til pdf kan følgende bruges:

```
pandoc "April 2024.md" -o test.pdf --pdf-engine=xelatex
```
