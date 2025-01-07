---
date: "2024-11-12T23:59:29+01:00"
title: "Guide til HUGO"
ShowToc: true
TocOpen: true
---

Bettys hjemmeside er jo lavet i et værktøj som hedder HUGO. Man kan læse en masse om det her https://gohugo.io.

Ideen er ret simpel. Den forvandler mapper og filer skrevet i markdown om til en super lækker hjemmeside (næsten 100% automatisk)

Markdown er også ret simpel. Det er det moderne svar på "word frustrerer mig". Markdown kan ikke lige så meget som word og det er en god ting :P

## Quickstart

1. Gå ind på https://github.com/UniSail/traeskibetbetty.dk og søg medlemskab. Det gør at du kan ændre i filerne
2. Gå ind i mappen "Content"

### Hvis du skal ændre i en fil:

3. Find din fil i "Content"
4. Lav dine ændringer og tryk commit eller push eller noget

### Hvis du skal tilføje nye filer:

3. Gå ind på https://github.com/UniSail/traeskibetbetty.dk og søg medlemskab. Det gør at du kan ændre i filerne
4. Gå ind i mappen "Content" og tryk "Add file"
5. Tilføj følgende til toppen af dit dokument:

```
---
date: "2024-11-12T23:59:29+01:00"
title: "Guide til HUGO"
---
```

6. Skriv din markdown fil og tryk commit eller push eller noget
7. Søg hjælp hvis det ikke virker "jeppefirring@gmail.com"

## Hvordan får jeg hugo til at køre på min computer?

Hugo kan hentes ved at følge guiden på https://gohugo.io/getting-started/quick-start/
Vi bruger PaperMod til HUGO https://github.com/adityatelange/hugo-PaperMod

1. Søg medlemskab hos https://github.com/UniSail/traeskibetbetty.dk
2. Installer et programmeringsværktøj såsom VSCODE https://code.visualstudio.com
3. Installer git (tror jeg)
4. Åbn vscode og login med github
5. Lav en klon af traeskibetbetty.dk (du burde kunne trykke dig frem til det. Ellers er google din ven)
   Nu skulle du gerne have en masse filer og have installeret hugo og papermod
6. git submodule update --init --recursive
7. Find en terminal i VSCODE og kør `hugo serve`
8. Se hvordan det andet er lavet / Søg på google. Det er ikke super svært men det er lidt svært nogle gange

### Tips

#### Billeder
Man skal lægge sit billede i mappen /static/img/ og så skal man sætte billedet ind som:
- `![Beskrivelse af billedet til synshandicappet](/img/navnPåBillede + filtype)`

Eksempelvis `![kristiansand2023](/img/kristiansand2023.jpg)`

##### Seje billeder
Man kan også skrive det ind således:
```
<div style="text-align: center;">
  <img src="/img/kristiansand2023.jpg" alt="alt" title="This is the title attribute" width="60%" >
</div>
```
#### Links

Links sættes ind med `[titel på link](link)`

#### HUGO fil ting

https://adityatelange.github.io/hugo-PaperMod/posts/papermod/papermod-features/

```
ShowToc: true #Viser indholdet af filen
TocOpen: true #inholdfortegnelsen er åben som standard
draft: true #Gemmer filen så den ikke kommer på hjemmesiden

```

### Hvordan laver jeg avanceret stuff

Det ved jeg godt nok ikke. Måske ring til en voksen.
