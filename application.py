from flask import Flask
application = Flask(__name__)  

@application.route('/df')        
def hello():         
    return 'Hello World'

