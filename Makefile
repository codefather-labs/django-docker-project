ping_google:
	python3 manage.py ping_google

wait:
	python3 -c "import time; time.sleep(3)"

delete_migrations:
	find . -path "*/migrations/*.py" -not -path "*/site-packages/*" -not -path "*/migrations/__init__.py" -delete

truncate_db:
	python3 manage.py sqlflush | python3 manage.py dbshell

reinstall_db_with_new_migrations:
	rm -rf db.sqlite3
	make delete_migrations
	make truncate_db
	python3 manage.py makemigrations
	python3 manage.py migrate
	make load_common_fixtures

dump_fixtures:
	python3 manage.py dumpdata > fixtures.json

dump_common_fixtures:
	python3 manage.py dumpdata --exclude admin.logentry --exclude auth.permission --exclude contenttypes.contenttype --exclude sessions.session > fixtures/common.json

load_common_fixtures:
	python3 manage.py loaddata fixtures/common.json

load_fixtures:
	python3 manage.py loaddata fixtures/fixtures.json

migrate:
	docker-compose -f docker-compose.yml up -d backend
	make wait
	docker exec -t backend python3 /app/manage.py makemigrations
	docker exec -t backend python3 /app/manage.py migrate

create_superuser:
	docker-compose -f docker-compose.yml up -d backend

collect_static:
	docker-compose -f docker-compose.yml up -d backend
	docker exec -t backend python3 manage.py collectstatic --noinput

build:
	docker-compose -f docker-compose.yml build --no-cache
	make wait

	make migrate
	#make create_superuser

	#make load_fixtures
	make collect_static
	docker-compose -f docker-compose.yml down

up:
	docker-compose -f docker-compose.yml up

down:
	docker-compose -f docker-compose.yml down

reinstall_subdomains:
	pip3 uninstall django-subdomains
	pip3 install git+https://github.com/codefather-labs/django-subdomains.git