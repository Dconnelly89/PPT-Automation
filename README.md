# PPT-Automation

Monorepo scaffold for local development with:

- `api`
- `worker`
- `web`
- `automation-bridge`
- `memory`
- `voice-gateway`

## Project structure

```text
.
├── api/
├── worker/
├── web/
├── automation-bridge/
├── memory/
├── voice-gateway/
└── docker-compose.yml
```

## Local development

### Prerequisites

- Docker
- Docker Compose (v2+)

### Start all services

```bash
docker compose up --build
```

### Service endpoints

- API: `http://localhost:8000/health`
- Web: `http://localhost:3000/health`
- Automation Bridge: `http://localhost:8003/health`
- Memory: `http://localhost:8004/health`
- Voice Gateway: `http://localhost:8005/health`

### Stop services

```bash
docker compose down
```
