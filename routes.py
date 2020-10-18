from app import app
from flask.templating import render_template

# TO USE THE FLASK FORMS 
import forms



# DEVELOP THE ROUTES


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
@app.route('/about')
def about():

    # return render_template('about.html')
    
    # USE A FORM WE CREATED IN FORMS.PY
    taskForm = forms.AddTaskForm()

    # WE CAN PASS THESE FORMS USING THE PARAMETER 'form'
    return render_template('about.html', form=taskForm)
    # THUS WE NOW HAVE ACCES TO THE FORM IN THE about.html FILE

    