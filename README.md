# traeskibetbetty.dk

## Installation

Find guides on <https://gohugo.io/getting-started/quick-start/>

After cloning repository run this command to setup Papermod (The theme for this website)

```shell
git submodule update --init --recursive # needed when you reclone your repo (submodules may not get cloned automatically)
```

```shell
hugo serve
```

For at konvertere et dokument til pdf kan følgende bruges:

```shell
pandoc "April 2024.md" -o test.pdf --pdf-engine=xelatex
```
