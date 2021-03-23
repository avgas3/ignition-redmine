# Redmine + Ignition Quickstart

Features:

- Traefik Reverse Proxy
- Ignition with python-redmine preloaded
- Redmine + MySQL

<!-- TODO: fill this out more -->
## Launch everything

```bash
docker network create db
docker-compose -f stack-proxy.yml -p proxy up -d
docker-compose up -d
```

## Access everything

- <http://proxy.vcap.me> - Traefik Dashboard
- <http://redmine.vcap.me> - Redmine (admin/admin)
- <http://gateway.vcap.me> - Ignition

## From Designer

```
from redminelib import Redmine
redmine = Redmine('http://gateway.vcap.me/redmine', username='admin', password='password')
print(redmine.project.get('test-project'))
```
