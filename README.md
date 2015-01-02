# Training on Flask (Python)

### Set up

- Install **Python 2.7.x**;
- Install **virtualenv**;
- Inside the app root directory, create a virtual environment called **flask**: `virtualenv flask`;
- Use **pip** from the virtual environment to install dependencies: `flask/bin/pip install -r requirements.txt`;
- Create a `config_local.py` file at the root directory of our app and fill it with the following properties to set up mail:
  ````
  MAIL_SERVER = <value>
  MAIL_PORT = <value>
  MAIL_USERNAME = <value>
  MAIL_PASSWORD = <value>
  ````

- Launch migrations: `./db_migrate.py`.

