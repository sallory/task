Создание виртуального окружения:
* python3 -m venv env
* source env/bin/activate

Установка зависимостей:
* pip3 install -r requirements.txt

Настройки базы данных:
```
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'testdb',
			'USER': 'postgres',
			'PASSWORD': '123',
			'HOST': '127.0.0.1',
			'PORT': '5432',
		}
	}
```

Миграция:
* python3 manage.py migrate

Запуск:
* python3 manage.py runserver

Примеры запросов:
* https://github.com/sallory/task/blob/master/postman_collection.json
