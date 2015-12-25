localrun=source localenv/bin/activate

run: localenv src/db.sqlite3
	$(localrun) && cd src && python manage.py runserver

doc:
	mkdocs serve

localenv: 
	virtualenv --no-site-package localenv && $(localrun) && pip install -r requirements.txt 
	cp src/Weather/settings/local.sample.env src/Weather/settings/local.env 

src/db.sqlite3: localenv
	$(localenv) && cd src && python manage.py startmigrations && python manage.py migrate

test: localenv src/db.sqlite3
	$(localrun) && cd src && python manage.py test

shell: localenv src/db.sqlite3
	$(localrun) && cd src && python manage.py shell
