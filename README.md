# traeskibetbetty.dk

## Installation

Hugo guides: https://gohugo.io/getting-started/quick-start/

After cloning:

```shell
git submodule update --init --recursive
```

### Run with Docker

Create a `.env` file:

```env
TS_AUTHKEY=your-tailscale-auth-key
HUGO_BASEURL=https://your-tailscale-hostname.ts.net/
```

Start:

```shell
docker compose up -d
```

Stop:

```shell
docker compose down
```

View logs:

```shell
docker compose logs -f
```

### Run Hugo locally

```shell
hugo serve
```

### Convert Markdown to PDF

```shell
pandoc "April 2024.md" -o test.pdf --pdf-engine=xelatex
```
