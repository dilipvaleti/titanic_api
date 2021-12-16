# Deploy ML model with Flask to Heroku

Click the button below to quickly clone and deploy into your own Heroku acount.
If you don't have one it'll prompt you to setup a free one.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Once deployed to your Heroku instance run the following:

```bash
curl -s -XPOST 'https://<name-of-your-heroku-app>.herokuapp.com/predict/982' -H 'accept-content: application/json'
```

Alternatively a simple python script:

```python
import requests
import json
url = 'https://<name-of-your-heroku-app>.herokuapp.com/predict/982'
response = requests.get(url)
print(response.json())
```
