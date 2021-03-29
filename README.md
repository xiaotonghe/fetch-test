# An automated webpage interaction testing
Web page: http://ec2-54-208-152-154.compute-1.amazonaws.com/

### Stacks:
- python (3.7.0)
- selenium

### Run local:
1. Build virtual environment:
```
python3 -m venv fetch-venv && source fetch-venv/bin/activate
```
2. Install the requirements:
```
(fetch-venv)$ pip install -r requirements.txt
```
3. Install Chrome Driver:

Selenium requires a driver to interface with the chosen browser (this program uses Chrome driver). Please follow the instruction below to download and once the Chrome driver is downloaded, please place it in PATH " /fetch-venv/bin":<br>
https://selenium-python.readthedocs.io/installation.html#drivers

4. Run the program:
```
python main.py
```
5. Run unit tests:
```
pytest -vvv tests.py
```

