from flask import Flask
from flask_sqlalchemy import SQLAlchemy 




# CREATE AN INSTANCE OF THE FLASK CLASS

app = Flask(__name__)

# A SECRET KEY FOR THE CRIF TOKEN
# LERN MORE ABOUT IT 
# WITHOUT THIS CONFIG SITE WITH CRIF TOKEN WON'T WORK
app.config['SECRET_KEY'] = 'A_JIBBRISH_string'

# FOR SQLALCHEMY
# WE WILL USE THE SQLITE DATABASE SYSTEM
# NAME OF DATABASE IS 'data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


# GET THE INSTANCE FOR THE DATABASE
db = SQLAlchemy(app)



# --------------- MOVE ALL THESE ROUTES TO ROUTES.PY FOR BETTER READABILITY ---------#

# # DEVELOP THE ROUTES


# # THIS WILL TELL THE WEB BROWSER 
# # TO RUN THIS FUNCTION WHEN
# # THIS PATH IS ENTERED IN THE ADDRESS BAR
# # WE CAN HAVE MULTIPLE PATHS 
# @app.route('/')
# @app.route('/index')

# # IN THESE FUNCTIONS YOU CAN RETURN :
# #       TEXT
# #       HTML SNIPPET
# #       ENTIRE HTML FILE
# def index():
    
#     # return 'Hello World'
#     # return "<h1>Hello World</h1>"

#     # render_template IS THE FUNCTIO TO 
#     # PROVIDE THE ENTIRE HTML FILE TO THE BROWSER
#     # BY DEFAULT ALL THESE FILES NEEDS TO KEPT IN THE 'templates' FOLDER
#     # return render_template('index.html')

#     # WE CAN ALSO PASS INFORMATION OR VARIABLES TO THE HTML FILES
#     return render_template('index.html', current_title='custom Title(Example)')
#     # AND IN THE HTML FILE WE CAN ACCESS IT AS : {{current_title}}
    

# # ROUTE FOR THE ABOUT PAGE
# @app.route('/about')
# def about():
#     return render_template('about.html')

#-----------------------------------------------------------------------------#


# TO GET THINGS FROM THE ROUTES.PY FILE 

from routes import *



# TO RUN THE APP
if __name__ == '__main__':
    # RUN FUNCTION TO EXECUTE THE APP
    # DEBUD IS TRUE TO ENABLE SOME DEBUG FUNCTIONALITIES
    # THUS THE SERVER WILL START
    # ALTHOUGH UPTILL HERE WITHOUT ANY |----ROUTER----| 
    # THE WEB BROWSER DOESN'T KNOW WHERE TO GO
    # THUS, THE BROWSER WILL SHOW NO URL FOUND    
    app.run(debug=True)


    # ------------------ IMPORTANT NOTE ------------------#
    # WHEN WE ARE IN THE DEBUG MODE
    # IF WE MAKE SOME CHANGES IN THE FILES AND SAVE THEM
    # AND THE SERVER IS STILL RUNNING
    # IT WILL AUTOMATICALLY DETECT THE CHANGES
    # AND WILL IMPLEMENT IT WITHOUT RESTARTING THE SERVER
    # THUS, CONSIDER THE DEBUG MODE AS THE LIVE SERVER PROPERTY

