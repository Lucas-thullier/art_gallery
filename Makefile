init: init.feed

init.feed: init.compose_up
	gunzip < ./backend/seeds/initial_dump.gz | docker exec -i db psql -U postgres -d postgres

init.compose_up: init.copy_env 
	docker-compose up 

init.copy_env:
	cp ./.env.example ./.env && cp ./frontend/.env.example ./frontend/.env