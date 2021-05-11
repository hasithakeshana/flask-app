from flask import Flask
application = Flask(__name__)  

@application.route('/df')        
def hello():         
    return 'Hello World'

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	application.run(debug=True) # running the app


#https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-specific.html