# Readme

This standalone application runs in a raspberry pi zero. It gets the weather information combined with a calendar and a quote, then generates an output to an e-ink screen (Waveshare 7.5 inch).

## Finished Picture

![Finished](/docs/images/finished.JPG)

## Install the application to Raspberry Zero

### 1. Prepare

- I. Add your openweathermap.org API key before running the application
  - Register an account from openweathermap.org
  - Get the API key
  - Modify cwt/conf-dev.py, Use your own key, and define the city based on the openweathermap.org
  - rename conf-dev.py to conf.py
- II. Change quote
  - open file: cwt/sentence.txt
  - Each quote one line

### 2. Build

- Windows

``` shell
python setup.py sdist bdist_wheel
```

- Linux and Mac:

```  shell
python3 setup.py sdist bdist_wheel
```

### 3. Deploy

- SSH pi zero
- Install python3 and pip3
- Upload the .whl file in ./dist folder
- At Pi zero, Run:

``` shell
pip3 install XXXX.whl
```

### 4. Set up cron

- SSH pi zero
- Run

``` shell
crontab -e
```

- Add this line (I set run the refresh every 5 minutes):

``` cron
0,5,10,15,20,25,30,35,40,45,50,55 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23 * * * /home/pi/.local/bin/run-standalone
```
