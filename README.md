Copy .env-example to .env
===

settings.py should contain as little exact values as possible. Default environment settings
should go in the .env-example file.

Create a random secret key
===

Replace the SECRET_KEY in .env with the output of this file.

```python
from django.core.management import utils
print(utils.get_random_secret_key())
```

Create a requirements.txt file
===

Update versions at requirements.txt

```
docker-compose exec web pip freeze
```

Keep requirements that you did not explicitly use out of the requirements.txt, to make maintenance easier.

Replace README.md
===

Create your own README.md