from app import app
from flask.templating import render_template

# TO USE THE FLASK FORMS 
import forms
from flask import Flask,redirect,url_for,render_template,request



#------------------ DEVELOP THE ROUTES ------------------#


# THIS WILL TELL THE WEB BROWSER 
# TO RUN THIS FUNCTION WHEN
# THIS PATH IS ENTERED IN THE ADDRESS BAR
# WE CAN HAVE MULTIPLE PATHS 
@app.route('/')
@app.route('/index')

# IN THESE FUNCTIONS YOU CAN RETURN :
#       TEXT
#       HTML SNIPPET
#       ENTIRE HTML FILE
def index():
    
    # return 'Hello World'
    # return "<h1>Hello World</h1>"

    # render_template IS THE FUNCTIO TO 
    # PROVIDE THE ENTIRE HTML FILE TO THE BROWSER
    # BY DEFAULT ALL THESE FILES NEEDS TO KEPT IN THE 'templates' FOLDER
    # return render_template('index.html')

    # WE CAN ALSO PASS INFORMATION OR VARIABLES TO THE HTML FILES
    return render_template('index.html', current_title='custom Title(Example)')
    # AND IN THE HTML FILE WE CAN ACCESS IT AS : {{current_title}}
    

# ROUTE FOR THE ABOUT PAGE

# FLASK BY DEFAULT CONSIDER ONLY THE GET REQUESTS
# SO TO HAVE A POST REQUEST WE NEED TO EXPLICITLY 
# DEFINE THE METHODS OF THE FORM IN THE ROUTES
@app.route('/about', methods=['GET', 'POST'])
def about():

    # return render_template('about.html')
    
    # USE A FORM WE CREATED IN FORMS.PY
    taskForm = forms.AddTaskForm()

    # IF THE FORM IS SUBMITTED
    # AND VALIDATION IS TRUE
    # WE CAN GET THE DATA OF THE TITLE INPUT BOX BY taskForm.title.data
    if taskForm.validate_on_submit():
        print(taskForm.title.data)

        # NOW TO RENDER THIS DATA TO A PAGE
        return render_template('about.html', form=taskForm, title=taskForm.title.data)

    # WE CAN PASS THESE FORMS USING THE PARAMETER 'form'
    return render_template('about.html', form=taskForm)
    # THUS WE NOW HAVE ACCES TO THE FORM IN THE about.html FILE

    