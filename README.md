# News API Application
## Description
Welcome to this news application. Using the options provided one can access news from various sources or even search news using domain name or the source platform.This application uses [New API](https://newsapi.org/) to fetch and generate News 
for you from various news sources.

## Author
- [Kenneth Thumi](https://github.com/KenThumi)

## Contact
Email:kenthumi@gmail.com

## Setup instructions
Below are steps to follow:
1. Open cli, navigate to your project folder and clone the project: <br/>
    `git clone https://github.com/KenThumi/NewsAPI.git`
2. Install python, preferably python3.
3. Create a virtual environment: <br/>
    `python3 -m venv virtual`
4. To activate the virtual environment run:<br/>
    `source virtual/bin/activate`
5. Now, in the virtual environment, install Flask to the project using the following command:<br/>
    `pip install flask`
6. Install flak bootstrap and flask script respectively:<br/>
        `pip install flask-bootstrap`<br/>
        `pip install flask_script`
7. Head over to [New API](https://newsapi.org/) and generate API key. To generate SECRET KEY 
    , open REPL by typing command `python3`. Enter these commands: <br/>
            `import secrets` <br/>
            `secrets.token_hex(16)`<br/>
    Where 16 is key length. Copy the keys to somewhere.
8. To register the API KEY and SECRET KEY to OS for use, enter these command. Enter the respective key where necessary <br/>
    `export MOVIE_API_KEY='api key generated'`<br/>
    `export SECRET_KEY='secret key generated'`

9. Inside the same folder,  type following commands to start the application:<br/>
    `python3 manage.py`
10. Open browser and input `http://127.0.0.1:5000`
11. To edit, use IDE of your choice to work with the project, e.g VsCode, Sublime text ,etc.

## Technologies Used
In this project, below is a list of technologies used:
- [Python version 3](https://www.python.org/)

## Dependencies 
Use command `pip freeze` to check if all these dependecies are present. 
1. click==7.1.2
2. dominate==2.6.0
3. Flask==1.1.2
4. Flask-Bootstrap==3.3.7.1
5. Flask-Script==2.0.6
6. itsdangerous==1.1.0
7. Jinja2==2.11.3
8. MarkupSafe==1.1.1
9. visitor==0.1.3
10. Werkzeug==1.0.1

## License info
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2021 © News API Application
