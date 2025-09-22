Local run instructions

1. Build and run locally (uses existing Postgres container aliases)

```bash
chmod +x scripts/run-local.sh
./scripts/run-local.sh
```

2. Verify

```bash
curl http://localhost:8000/health
```

3. Stop

```bash
docker rm -f myprod
```

Notes:
- The script builds `myproductionapp:local` using `Dockerfile.prod` and attaches it to
  the `leetcode_app_net` docker network so `DB_HOST=db` resolves to the existing Postgres container.
- If your local Postgres runs under a different network or name, edit `scripts/run-local.sh` and change `DB_HOST`.
