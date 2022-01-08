<h1 align="center">
🎨 Gallery 🎨
</h1> 

<h2 align="center">
Gallery is a place where you can explore throught wikidata-registered paintings (and that's much paintings)
</h2>

## Technical stack
- Django
- Vuejs
- PostgreSQL
- RabbitMQ + Celery + Flower (asynchronous job and admin panel for them)
- Docker

## Get Started
To launch the project you need to
- Use Docker
- remove .example suffixes from ./env.example and ./frontend/.env.example
- place current working directory at root (before backend and frontend)
- run : docker-compose up
- feed database with : gunzip < ./backend/seeds/initial_dump.gz | docker exec -i db psql -U postgres -d postgres
- wait until end of feeding (this may take a while)
- go to http://localhost:3000/#/painting/all

clear tasks queue:
  celery -A celery purge (le second celery = appli normalement worker.worker.app mais bizaremment non. A verifier pourquoi)

```Backup Database```
generate sql:
  docker exec -t your-db-container pg_dumpall -c -U your-db-user > dump_$(date +%Y-%m-%d_%H_%M_%S).sql

to reduce the size of the sql you can generate a compress:
  docker exec -t your-db-container pg_dumpall -c -U your-db-user | gzip > ./dump_$(date +"%Y-%m-%d_%H_%M_%S").gz

Restore Database:
  cat your_dump.sql | docker exec -i your-db-container psql -U your-db-user -d your-db-name

to restore a compressed sql:
  gunzip < ./backend/seeds/initial_dump.gz | docker exec -i db psql -U postgres -d postgres
