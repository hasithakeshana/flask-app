from flask import Flask
from flask_restful import Api,Resource

import pickle
import pandas as pd 
from fbprophet import Prophet

application = Flask(__name__)
api = Api(application)

class vegPrices(Resource):
    def get(self,name):

        # pickle file name
        file_name = 'prophet_pickle_model'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'))

        # hardcoded input of the user
        future_date = pd.DataFrame({'ds':['2018-04-01']})

        # forecast using the model
        out = loaded_model.predict(future_date)

        print("%.2f" % out.yhat[0])

        return {"data": round(out.yhat[0],2)}

    def post(self,name):
        return {"data": name}




api.add_resource(vegPrices,"/vegPrices/<string:name>")

if __name__ == "__main__":
    application.run(debug=True)