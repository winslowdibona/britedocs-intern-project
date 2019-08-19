

## Problem Statement
Our CEO Phil Reynolds is the biggest Newk's fan alive and the one he goes to for lunch everyday has just closed. To prevent the company from going under due to his impending meltdown, we have decided to open a new Newk's and first we need a menu.


## Goal
The goal of this project is to produce of pdf of a menu given the data set provided in `data.json`. You'll be using [Jinja2](http://jinja.pocoo.org/docs/2.10/templates/) to develop an html template representation of the menu. You are not provided an example as that tends to guide your decision making, rather this project allows you to design the menu however you see fit, utilizing the data provided.


## Steps to get started

**If you are running Windows 10 Home Edition skip these steps and go to the next section**

1. Install [Docker](https://www.docker.com/) on your machine
	- If your machine does not support Docker, continue on until step 4
2. Fork this repo
3. Clone locally
4. From the project directory
	- If you are able to run Docker, run `docker-compose up`
	  - This will build a docker container that hosts a small web app used to render the pdf.
	  - To stop the web app run `docker-compose down`
  	- If you are not able to run docker
  		- Run `python3 -m venv /path/to/your/project/.venv`
  		- Run `source .venv/bin/activate`
  		- Run `python3 -m pip install -r requirements.txt`
  		- Run `FLASK_APP=app.py flask run`

From here you can begin developing the template in `britedocs-intern-project/templates/Menu.html`. The data provided in `data.json` will automatically be available to your template when you attempt to render it.
To test rendering your template, make sure the docker container is running and in a separate window run

```
curl -X POST http://0.0.0.0:5000 -d '{"template_name": "Menu"}' -H "Content-Type: application/json"
```

and you should recieve a response that says `Documents Rendered!`. The rendered HTML and PDF documents will appear in the `britedocs-intern-project/output/` directory.


## Windows 10 Home Edition Workaround

Unfortunately Docker cannot run on Windows 10 Home edition. To get around this limitation, you can utilize the site [pythonanywhere](pythonanywhere.com/).

Sign up for the free account and follow the steps below.

1. Create a new bash console
2. Clone your repo
3. Run `cd britedocs-intern-project`
4. Run `python3 -m venv .venv`
5. Run `source .venv/bin/activate`
6. Run `python3 -m pip install -r requirements.txt`
7. Run `mkdir output`
8. Develop your template in the `Menu.html` file
    - You can do this on your own machine and upload it into the `templates` directory
		- Or you can use the editor provided in the site to edit your template
9. When you want to see what your template looks like run `python workaround.py`
10. You should see the console output `Document Rendered!`. Your rendered template will appear in the `output` directory.


## Deliverables
Once you are done with the project:

1. Add the contents of the `/templates/` and `/output/` directories to your repo
2. Update the README with your approach to designing the template (you may also add any other thoughts/questions)
3. Make sure your fork of the repository is updated in Github
4. Email winslow@britecore.com with a link to your forked repository


## Bonus Points
 - No inline CSS styling, instead all CSS is contained within `<style>` tags within a template
 - Usage of DRY (Don't Repeat Yourself) principles

## Hints:

 - You don't have to put everything in one template, you can break it out into multiple templates. The packaged web app provides a jinja helper statement `include` which allows you to pull in the contents of another template. Usage would look like `{% include 'Other_template' %}`. Just ensure that any new templates you add are added to the `templates` directory
 - You can use the `curl` terminal command to preview what any of the templates you've created look like, just change the `template_name` param
 - HTML tables are your friend
