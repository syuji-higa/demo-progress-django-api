## Check API Key

```sh
$ docker-compose run web python manage.py shell
```

```python
from rest_framework_api_key.models import APIKey
api_key = APIKey.objects.get(name="{api_key_name}")
api_key.pk
```
