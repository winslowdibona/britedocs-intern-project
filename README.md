

## Problem Statement
Our CEO Phil Reynolds is the biggest Newk's fan alive and the one he goes to for lunch everyday has just closed. To prevent the company from going under due to his impending meltdown, we have decided to open a new Newk's and first we need a menu.


## Goal
The goal of this project is to produce of pdf of a menu given the data set provided in `data.json`. The template should be developed using [Jinja2](http://jinja.pocoo.org/docs/2.10/templates/) and a pdf of the menu should be generated using this project.


## Steps to get started
1) Fork this repo
2) Clone locally
3) From the project directory run `docker-compose up`
  - This will build a docker container that host a small web app used to render the pdf.
  - To stop the web app run `docker-compose down`

From here you can begin developing the template in `/templates/Menu.html`. 
To test rendering your template run

```
curl -X POST http://0.0.0.0:5000 -d '{"template_name": "Menu"}' -H "Content-Type: application/json"
```

and you should recieve a response that says `Documents Rendered!`. The rendered HTML and PDF documents will appear in the `/output/` directory.


## Deliverables
Once you are done with the project add your templates and rendered documents to your forked git repository. Once done please email the link to your repository to winslow@britecore.com.



## Bonus Points
 - No inline CSS styling, instead all CSS is contained within `<style> tags within a template`
 -

## Hints:

 - You don't have to put everything in one template, you can break it out into multiple templates. The packaged web app provides a jinja helper `include` which allows you to pull in the contents of another template. Usage would look like `{% include 'Other_template' %}`
 - You can use the above terminal command to preview what any of the templates you've created look like, just change the `template_name` param.
 - HTML tables are your friend.
