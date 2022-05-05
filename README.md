# TradePoints Visits

ITFactory

## Установка

```sh
git clone https://github.com/staffluck/factory.git
nano .env ( по шаблону .env.template )
python manage.py migrate
python manage.py runserver 5000
```

Из-за того что phone это query параметр, телефон лучше сохранять и искать по формату "81234567890"
## Эндпоинты
```sh
[GET] http://127.0.0.1:5000/tradepoints/?phone=<phone>

[POST] http://127.0.0.1:5000/create_visit/?phone=<phone>
    body:
        {
            "tradepoint": <pk>,
            "latitude": <float>,
            "longitude": <float>
        }
```

