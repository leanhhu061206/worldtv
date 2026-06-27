# Livetv — Proxy per stream TV

Server proxy che autentica e ritrasmette stream WebM per usarli in VLC/MPV/IINA.

Aprendo il pannello web trovi le liste TV pronte da copiare per ogni paese.

## Con Docker (x86/amd64)

```bash
docker build -f Dockerfile -t livetv .
docker run -d --name livetv --restart unless-stopped -p 8042:8042 -e PROXY_PORT=8042 livetv
```

## Con Docker (ARM)

```bash
docker build -f Dockerfilearm -t livetv-arm .
docker run -d --name livetv --restart unless-stopped -p 8042:8042 -e PROXY_PORT=8042 livetv-arm
```

> La porta si cambia con la variabile d'ambiente `PORT` (es. `-e PROXY_PORT=8080`, e mappa `-p 8080:8080`).

## Su Hugging Face Spaces

1. Crea uno Space con **Docker**.
2. Carica i file di nel repo (senza il README.md o le versioni con arm nel nome).
3. Apri il pannello web dello Space per copiare i link delle liste.
