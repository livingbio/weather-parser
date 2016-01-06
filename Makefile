port = 8000
IMG_NAME = weather
MAKE_LOG_PATH = .make
localrun=docker run --rm -i -t -p $(port):$(port) -v $(shell pwd):/work -w /work/src $(IMG_NAME) 
vpath %.build $(MAKE_LOG_PATH)
migration_files = $(shell find src -type f -name '*.py'|grep "migrations")
model_files = $(shell find src -type f -name 'models.py')
env_files = $(shell find env -type f -name '*')


run:  db.build
	$(localrun)  python manage.py runserver 0.0.0.0:8000

doc:
	echo $(migrations) $(models)


image.build: $(env_files)
	docker build  -t $(IMG_NAME) env
	echo "" > $(MAKE_LOG_PATH)/$@

db.build: image.build $(migration_files) $(model_files)
	$(localrun)  python manage.py makemigrations ; $(localrun) python manage.py migrate 
	echo "" > $(MAKE_LOG_PATH)/$@

test: db.build
	$(localrun) python manage.py test

shell: db.build
	$(localrun) /bin/bash

manage: db.build
	$(localrun) python manage.py $(args)

clean: 
	rm -rf src/db.sqlite3 .make

