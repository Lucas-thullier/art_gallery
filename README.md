<h1 align="center">
 Gallery 🎨
</h1> 

## ⚠️ This project is under development ⚠️

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

## Useful commands
```Backup Database```
  docker exec -t db pg_dumpall -c -U postgres | gzip > ./dump_$(date +"%Y-%m-%d_%H_%M_%S").gz

```Restore Database```
  gunzip < ./backend/seeds/initial_dump.gz | docker exec -i db psql -U postgres -d postgres
