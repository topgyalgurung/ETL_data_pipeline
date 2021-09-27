
# ETL Simple Project

## Python program that builds database of current weather data from OpenWeatherMap web APIs, parse data using Pandas library and store it in a local sqlite database

- [OpenWeatherMap](https://openweathermap.org/) 
- [Make Environment Variable in Python](https://www.nylas.com/blog/making-use-of-environment-variables-in-python/)
- [doctest](https://docs.python.org/3/library/doctest.html)

## Set Up:
- install dependencies:
    ```
  pip3 install -r requirements.txt
    ```
- get OpenWeatherMap API Key, copy the key and save into .env
- Run <code>$python3 main.py </code> to save New York current weather by default

# To build docker container for your app
- Create Dockerfile 
- Build Docker image 
   ```
   $ docker build -t yourdockerid/data-pipeline-test .
   $docker run --env api-token=<youapitoken>-t yourdockerid/data-pipeline-test
   ```

## Note:
- keep api key private in .env file (eg API_TOKEN="typeyourapikeyhere")
- load API into python code using dotenv library
  ```python
  from dotenv import load_dotenv 
  ```
- how to make api request 

```python
json_data=json_data=requests.get("http://api.openweathermap.org/data/2.5/weather?id=5128581&appid=6e7ca5ea2bcbd8c244b635632d4840ee").json() // eg api_token not real
```
- <code>$python3 main.py -v</code> # -v to the script prints detailed log of whats trying and prints summary
### CITY ID 
1. Kathmandu, Nepal =1283240
2. Mustang, Nepal =1283023
3. Pokhara, Nepal =1282898


