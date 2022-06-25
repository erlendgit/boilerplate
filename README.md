Copy .env-example to .env
===

settings.py should contain as little exact values as possible. Default environment settings
should go in the .env-example file.

Start your project
===

```bash
docker-compose pull
docker-compose up -d

```

Create a random secret key
===

Replace the SECRET_KEY in .env with the output of this file.

```bash
docker-compose exec web python manage.py shell
```

```python
from django.core.management import utils
print(utils.get_random_secret_key())
```

Restart your machine
===

```bash
docker-compose stop
docker-compose pull
docker-compose up -d
```

Create a requirements.txt file
===

Update versions at requirements.txt

```
docker-compose exec web pip freeze
```

Keep requirements that you did not explicitly use out of the requirements.txt, to make maintenance easier.

Setup Grunt
===

To start working with your assets, install nodejs dependencies.

```bash
npm install grunt \
            grunt-contrib-copy \
            grunt-contrib-sass \
            grunt-contrib-watch
```

Add lines to the package.json file to start building and watching assets:

```json
{
  "scripts": {
    "watch": "grunt",
    "build": "grunt build"
  }
}
```

Test it 

```bash
npm run build
npm run watch
```

Note: watch will build first, then start watching. It is not manditory to run `build` before `watch`


Initialize django database
===

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

And now visit http://localhost:8000/admin

Replace README.md
===

Create your own README.md

Start developing
===

Last but not least... start developing your, super special - one of a kind, web application.