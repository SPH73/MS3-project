# MS3-project

## Project Helpers

[pipenv](https://pypi.org/project/pipenv/) was used to create a virtual environment. It is the recommended python virtual envirinment management according to the official docs.  
[Python secret key generator](https://docs.python.org/3/library/secrets.html) generated in the python repl using `secrets.token_hex(16)`, which is designed for security and cryptography and returns a random text string in hexadecimal using the os and secrets module.  
[Flask](https://flask.palletsprojects.com/en/1.1.x/)
[Flask tutorial](https://hackersandslackers.com/series/building-flask-apps)
[flask-wtf](https://flask-wtf.readthedocs.io/en/stable/quickstart.html)
[WtForms](https://wtforms.readthedocs.io/en/2.3.x/)
[Recaptcha Tutorial](https://pusher.com/tutorials/google-recaptcha-flask)  
[Google reCAPTCHA Tutorial](https://codelabs.developers.google.com/codelabs/reCAPTCHA/index.html#5)
[Flask_PyMongo Docs](https://flask-pymongo.readthedocs.io/en/latest/)  
[Flask-Pymongo](https://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php)
[Flask deployment options](https://flask.palletsprojects.com/en/1.1.x/deploying/?highlight=deploying)
[Deploying to Heroku](https://medium.com/technest/build-a-crud-app-with-flask-bootstrap-heroku-60dfa3a788e8)  
[Favicon-generator](https://www.favicon-generator.org/)

I improved the project organisation by turning the application into a package with `__init__.py` and moving the routes to `views.py`. to avoid confusion I renamed `app.py` to `run.py` to be different from the package name. At the same time I created a `requirements.txt` to be inclusive of choice for other developers or the assessors.
