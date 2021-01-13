**To run it in on Windows**

`SET APP_COLOR=blue`

`python app.py`

**To run it in on Linux**

`export APP_COLOR=blue`

`python app.py`

**To build the docker image**

`docker build -t flasktest:latest .`

**To run the docker image**

`docker run -d -p 5000:8080 -e APP_COLOR=blue flasktest`

`docker run -d -p 5001:8080 -e APP_COLOR=red flasktest`

`docker run -d -p 5005:8080 -e APP_COLOR=yellow flasktest`

**To test it**

Open your browser and go to `http://127.0.0.1:<port>`. For example:

`http://127.0.0.1:5005` which will show you the **yellow** backgound
