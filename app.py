from flask import Flask, request, jsonify, make_response
import firebase_admin
from firebase_admin import credentials, db
import datetime
import sys
import context_setter
import message_setter

#import os
# import uuid
# import base64
# import pyttsx3
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keyfile.json"
# Open the log file in append mode
  # Log the received data



# Use a service account
cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://polar-city-332413-default-rtdb.firebaseio.com'
})


app = Flask(__name__)

@app.route('/', methods=['GET'])
def webhook_1():
    return "Flask app"


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # log_file = open('app.log', 'a')
    # sys.stdout = log_file
    print(data)
    resp = ''
    if data['queryResult']['intent']['displayName'] == 'askThanks - yes':
        resp = storeDataIntoDB(data)
       
    if data['queryResult']['intent']['displayName'] == 'askResturantName':
        resp = context_setter.setContextVariableAskResturantName(data)
     
    if data['queryResult']['intent']['displayName'] == 'Welcome':
        resp = message_setter.setWelcomeMessage()

    if data['queryResult']['intent']['displayName'] == 'askRoles':
        resp = context_setter.setContextVariableRoles(data)
        
    if data['queryResult']['intent']['displayName'] == 'askCityName':
        resp = context_setter.setContextVariableAskCityName(data)

    if data['queryResult']['intent']['displayName'] == 'askEquimentType':
        resp = context_setter.setContextVariableEquimentType(data)
    
    if data['queryResult']['intent']['displayName'] == 'askAppFee':
        resp = context_setter.setContextVariableAskAppFee()

    if isinstance(resp, str):
        response = make_response(resp)
    else:
        response = resp

    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'

    # log_file.flush()
    return response


def storeDataIntoDB(data: dict):
      print("Active Intent: askThanks - yes ")
      session_id = data["session"]
      status = "Success"
      try:
        user_context = data["queryResult"]["outputContexts"]
        for d in user_context:
          context_name = d["name"]
          if(context_name.find("session_data") != -1):
              data = d["parameters"]
              data_to_store = refine_data(data, session_id)
              print("Data to store", data_to_store)
              ref = db.reference('webhook_data')
              ref.push(data_to_store)
      except KeyError:
         status = "Error"
         print('Error while storing or getting the data')
      return status + "in storing data"


def refine_data(user_data, session_id):
    print(f'data to be refine: {user_data}')
    refine_user_data = {
        "person_name": user_data.get("person.original", ""),
        "person_role": user_data.get("Role.original", ""),
        "restaurant_name": user_data.get("any.original", ""),
        "city": user_data.get("geo-city.original", ""),
        "street_address": user_data.get("street-address.original", ""),
        "cuisine_types": ", ".join(user_data.get("cuisine.original", "")),
        "resource_idle": user_data.get("ResourceIdleNess", ""),
        "other_apps": ", ".join(user_data.get("OtherApp.original", "")),
        "app_costing": user_data.get("app-fee", ""),
        "adding_sales_costing": user_data.get("number.original", ""),
        "equipments": ", ".join(user_data.get("Equipment.original", "")),
        "extra_capacity": user_data.get("CapacityType", ""),
        "timestamp": str(datetime.datetime.now()),
        "session_id": session_id
    }
    print(f'data to push: {refine_user_data}')
    return refine_user_data


if __name__ == '__main__':
    # Close the log file when the application exits
    app.run()
