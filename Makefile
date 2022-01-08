init: init.compose_up

init.compose_up: init.copy_env 
	docker-compose up -d --wait

init.copy_env:
	cp ./.env.example ./.env && cp ./frontend/.env.example ./frontend/.env