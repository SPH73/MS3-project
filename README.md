# MS3-project

[pipenv](https://pypi.org/project/pipenv/) was used to create a virtual environment. It is the recommended python virtual envirinment management according to the official docs.  
[secret key](https://docs.python.org/3/library/secrets.html) generated in the python repl using `secrets.token_hex(16)`, which is designed for security and cryptography and returns a random text string in hexadecimal using the os and secrets module.  
[Flask-Pymongo](https://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php)  
[Flask-PyMongo on medium](https://medium.com/@riken.mehta/full-stack-tutorial-flask-react-docker-ee316a46e876)  
[Flask_PyMongo Documentation](https://flask-pymongo.readthedocs.io/en/latest/)  
[Favicon-generator](https://www.favicon-generator.org/)  
After creating the basic project I chose to improve the project organisation by turning the application into a package with `__init__.py` and moving the routes to `views.py`. to avoid confusion I renamed `app.py` to `run.py` to be different from the package name. At the same time I created a `requirements.txt` to be inclusive of choice for other developers or the assessors.
