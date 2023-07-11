from flask import Flask, request, jsonify, make_response
import firebase_admin
from firebase_admin import credentials, db
import datetime
import sys
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
    log_file = open('app.log', 'a')
    sys.stdout = log_file
    print(data)
    resp = ''
    if data['queryResult']['intent']['displayName'] == 'askThanks - yes':
       resp  = storeDataIntoDB(data);

    if data['queryResult']['intent']['displayName'] == 'Welcome':
       resp  = setWelcomeMessage();

    if data['queryResult']['intent']['displayName'] == 'askRoles':
       resp = setContextVariable(data);

    if data['queryResult']['intent']['displayName'] == 'askEquimentType':
       resp = setContextVariableEquimentType(data)

    if isinstance(resp, str):
        response = make_response(resp)
    else:
        response = resp

    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'

    log_file.flush()
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

def setWelcomeMessage():
     msg = "Hi there! Please tell us your name."
     response = {
     "fulfillmentMessages": [
         {
             "text": {
                 "text": [msg]
             }
         },
         {
             "payload": {
                 "platform": "kommunicate",
                 "message": "",
                 "ignoreTextResponse": False
             }
         }
       ]
     }
     return jsonify(response)

def setContextVariable(data:dict):
        print("Active Intent: askRoles")
        rest_name = ''
        resp = "Error"
        try:
          user_context = data["queryResult"]["outputContexts"]
          print("INSIDE1")
          for context in user_context:
            if 'session_data' in context['name']:
                print("INSIDE2")
                # Check if the payload contains the form data
                if 'originalDetectIntentRequest' in data and 'payload' in data['originalDetectIntentRequest']:
                    # Get the form data
                    form_data = data['originalDetectIntentRequest']['payload']

                     # Update the context variables if the form data fields exist in the payload
                    if 'name' in form_data:
                        context['parameters']['person'] = form_data['name']
                        context['parameters']['person.original'] = form_data['name']
                    if 'restaurant' in form_data:
                        context['parameters']['any'] = form_data['restaurant']
                        context['parameters']['any.original'] = form_data['restaurant']
                        rest_name = form_data['restaurant']
                    if 'city' in form_data:
                        context['parameters']['geo-city'] = form_data['city']
                        context['parameters']['geo-city.original'] = form_data['city']
                    if 'street' in form_data:
                        context['parameters']['street-address'] = form_data['street']
                        context['parameters']['street-address.original'] = form_data['street']
                    print("INSIDE4")
                    # Now the context variables have been updated with the new values
          resp = getRespOfAskRoles(rest_name, user_context)

        except KeyError:
           print('Error while updating the context variables')

        return jsonify(resp)


def setContextVariableEquimentType(data:dict):
    print("Active Intent: askEquimentType")
    resp = "Error"
    try:
        user_context = data["queryResult"]["outputContexts"]
        person_name  = ''
        print("INSIDE1")
        for i, context in enumerate(user_context):
            if 'session_data' in context['name']:
                print("INSIDE2")
                user_context[i]['parameters']['app-fee'] = data["queryResult"]["queryText"]
                person_name = user_context[i]['parameters']['person.original']

        print("user_context", user_context)
        resp = getRespOfAskEquimentResp(person_name, user_context)

    except KeyError:
        print('Error while updating the context variables')

    return jsonify(resp)


def getRespOfAskRoles(rest_name: str, user_context: dict):
     msg =f"Thanks, we got you, please tell us about your role at {rest_name}"
     response = {
     "fulfillmentMessages": [
         {
             "text": {
                 "text": [msg]
             }
         },
         {
             "payload": {
                 "platform": "kommunicate",
                 "message": "",
                 "ignoreTextResponse": False,
                 "metadata": {
                     "templateId": "6",
                     "payload": [
                         {
                             "message": "Manager",
                             "title": "Manager"
                         },
                         {
                             "title": "Owner",
                             "message": "Owner"
                         },
                         {
                             "message": "Staff",
                             "title": "Staff"
                         },
                         {
                             "title": "Other",
                             "message": "Other"
                         }
                     ],
                     "contentType": "300"
                 }
             }
         }
     ],
     "outputContexts": user_context
     }
     return response


def getRespOfAskEquimentResp(person_name:str, user_context: dict):
     msg = f"Awesome {person_name}, what kind of equipment is integral to your business?"
     response = {
        "fulfillmentMessages": [
         {
             "text": {
                 "text": [msg]
             }
         },
         {
            "payload":
                {
                    "platform": "kommunicate",
                    "message": "",
                    "ignoreTextResponse": False,
                    "metadata": {
                       "templateId": "6",
                       "payload": [
                            {
                             "message": "Freezer",
                             "title": "Freezer"
                            },
                            {
                             "title": "Fryer",
                             "message": "Fryer"
                            },
                            {
                             "title": "Oven",
                             "message": "Oven"
                            },
                            {
                             "title": "More than one",
                             "message": "More than one"
                            }
                         ],
                       "contentType": "300"
                    },
               }
         }
        ],
        "outputContexts": user_context
     }
     return response

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
        "session_id":session_id
    }
    print(f'data to push: {refine_user_data}')
    return refine_user_data






if __name__ == '__main__':
    # Close the log file when the application exits
    app.run()
