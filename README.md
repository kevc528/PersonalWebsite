# PersonalWebsite

## About
My personal website built using Python and Django!

## Running
Django: Navigate to the `PersonalSite` folder and use the command `python3 manage.py runserver` and then go to `localhost:8000`

Database Tool: Commands here will be run from the project directory.

* DATABASE OVERVIEW: `python3 db_tool.py overview` is the command to get a list of all the tables
* TABLE INFORMATION: `python3 db_tool.py info table_name`. 
	* Ex: `python3 db_tool.py info projects_project`
	* Note that table names are usually in the format `appname_classname`. To see all tables run the overview command.

## Description

### Django Structure
All Django project components are located in the `PersonalSite` folder. Within the Django 
project I created three apps: about, contact, and projects. The about app is for the splash 
page, which is just a bio page. The contact app is for contact information, so email, github, 
linkedin. The projects app has code for the portfolio, which has information about some projects 
that I have worked on. I have also created two base layout templates that all other templates extend from. They contain the nav bar on the top and the footer on the bottom for all templates. There are two because sometimes with a longer page, we want the footer to stick to the bottom and not overlap.

### Django App: about
The about app contains the splash page which is just the bio. It's not very complicated and just does the job of rendering the bio page. Additionally, there is a resume route that is specified in views. This route just downloads a copy of the resume pdf.

Routes:

* `/`, the splash page which is just a bio
* `resume/`, request to download the resume pdf

### Django App: projects
This is the main part of the project. This is the app that controls the portfolio. In the portfolio, each of my projects will be listed. Additionally, you can click into each project to get more information about it. Inside each projects page, there will be a brief description, and then a discussion section. When you click into it, you can leave a comment or recommendation and also see other people's comments and recommendations. Additionally, on the list of projects, each project has buttons for the categories they are in. If you click the button, it will filter all of the projects by that category. Note that I don't have an add project method because I don't want any random user to change the content on my website.

Routes:

* `projects/`, route for the page with the list of projects
* `projects/<str:name>`, route for the individual page for a single project
* `comment/<str:id>`, POST route for leaving comments on a specific project with the specified id
* `projects/category/<str:name>`, route for getting projects all of the specified category name

### Django App: contact
The contact app displays a page with contact information and other sites listed. It's not very complicated and just does the job of rendering the contact page.

Routes:

* `contact/`, route for the contact page which displays contact information

### Classes: Django Models

	class ProjectCategory(models.Model):
	    name = models.CharField(max_length=200)

	    def __str__(self):
	        return self.name


	class Comment(models.Model):
	    author = models.CharField(max_length=200)
	    comment = models.TextField()
	    post_time = models.DateTimeField(auto_now=True)

	    def __str__(self):
	        return self.author

	    def __lt__(self, other):
	        return self.post_time < other.post_time


	class Project(models.Model):
	    title = models.CharField(max_length=200)
	    description = models.TextField()
	    start_date = models.DateTimeField()
	    end_date = models.DateTimeField()
	    category = models.ManyToManyField(ProjectCategory)
	    comments = models.ManyToManyField(Comment, blank=True)

	    def __str__(self):
	        return self.title

	    def __lt__(self, other):
	        return self.end_date < other.end_date

Above are the classes I created. These are for the projects, so models include category, comments, and projects. Note that category and comments are many to many fields for projects because they are all linked together. In `Comment` and `Project` I have two magic methods in each of those classes. I have `__str__` and `__lt__`. The string method was important for visualizing entries in the data in django admin. The less than method was useful for getting a sorted list of projects and comments from recent to old.

### Database Tool: uses sqlite3, sys, and pandas packages
The database tool is useful for looking at data in the sqlite database for django without having to connect to admin to do so. In the Running section above, I specify how to run this program. Basically there are two ways to run this program, depending on your command line arguments. You can get a basic overview of all of the tables in the database, or get an in-depth look at one of them. This is determined by the command line argument `info tablename` or `overview`. 

The command line arguments are found using the `sys` package. The `sqlite3` package is useful for establishing a connection with the database, running queries, and closing the connection at the end. The `pandas` package is used when we recieve the `info tablename` command line arguments. Then `pandas` will read sql into a dataframe, and have nice methods to get information on shape, datatypes, and display the table nicely (instead of a list of tuples).
