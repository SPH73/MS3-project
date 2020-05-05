# MS3-project - CodeFlow

## Introduction

[CodeFlow](http://codeflow-app.herokuapp.com) was created to help bridge the gap to employed status for students. Based on the idea of the seasonal Hackathons held by Code Institute, where a brief is given and students collaborate to create finished projects, similarly developers (or anyone with an idea) can upload projects that require full or partial contribution, called 'Piece Projects'. The idea being that the more experience a student developer gains from working in a team or from developing code snippets to be used in a project, the more skilled they become at breaking down the project parts into smaller more manageable pieces or problems; resulting in a more confident developer who is naturally more appealing in the talent pool to employers.

As a student, I find that describing and realising the whole-parts or 'pieces' of my projects is a challenging task and leaves me questioning how long it will take for me to become suitably experienced enough for employment in the industry. I would like exposure to others' projects and an opportunity to offer pieces of code I have written according to a brief to help me improve my skillset (level of understanding), increase speed and boost my confidence. I am certain that I am not alone and that the majority of software developer students, whether they are studying on a course or self-teaching will find value in the same.

Any entity with a project or idea, be it developer, student or whomever, who would like to share it in part or whole with other developers to collaborate on, CodeFlow provides the platform for that.

All 'noobs' are blessed when we can stand on the shoulders of giants and learn from our more experienced counterparts. The CodeFlow Blog invites the community to post articles that imparts knowledge or learning based on experience, interesting articles about new technologies or absolutely anything of a related nature that benefits the readers.

## Table of Contents

1. [UX](#ux)
   - [Goals](#goals)
   - [User Stories](#user-stories)
     - [Visitor Stories](#visitor-stories)
     - [Business Stories](#business-stories)
   - [Wireframes](#wireframes)

## UX

## Features

## Technologies Used

## Testing

## Deployment

## Credits

## Acknowledgements

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

I improved the project organisation by turning the application into a package with `__init__.py` and moving the routes to `views.py`. to avoid confusion I renamed `app.py` to `run.py` to be different from the package name. At the same time I created a `requirements.txt` to be inclusive of choice for other developers, deployment and the assessors.
