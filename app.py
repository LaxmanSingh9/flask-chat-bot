from flask import Flask, request, jsonify, make_response
import firebase_admin
from firebase_admin import credentials, db
import datetime
import mysql.connector
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
    if data['queryResult']['intent']['displayName'] == 'Welcome':
        storeDataIntoDB(data, True)
        resp = message_setter.setWelcomeMessage()

    elif ((data['queryResult']['intent']['displayName'] == 'askThanks') 
            or
          (data['queryResult']['intent']['displayName'] == 'endOfConversation')
          ):
        print("Active Intent: askThanks Inside If")
        resp = storeDataIntoDB(data, False)
       
    elif data['queryResult']['intent']['displayName'] == 'askResturantName':
        storeDataIntoDB(data, False)
        resp = context_setter.setContextVariableAskResturantName(data)
     
    elif data['queryResult']['intent']['displayName'] == 'askRoles':
        resp = context_setter.setContextVariableRoles(data)
        
    elif data['queryResult']['intent']['displayName'] == 'askCityName':
        storeDataIntoDB(data, False)
        resp = context_setter.setContextVariableAskCityName(data)

    elif data['queryResult']['intent']['displayName'] == 'askEquimentType':
        storeDataIntoDB(data, False)
        resp = context_setter.setContextVariableEquimentType(data)
    
    elif data['queryResult']['intent']['displayName'] == 'askAppFee':
        storeDataIntoDB(data, False)
        resp = context_setter.setContextVariableAskAppFee(data)
        
    elif data['queryResult']['intent']['displayName'] == 'Default Fallback Intent':
        storeDataIntoDB(data, False)
        resp = context_setter.setContextDefault(data)
    
    elif data['queryResult']['intent']['displayName'] == 'askCuisine':
        storeDataIntoDB(data, False)
        resp = context_setter.setContextAskCuisine(data)

    if isinstance(resp, str):
        response = make_response(resp)
    else:
        response = resp

    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'

    # log_file.flush()
    return response


def storeDataIntoDB(data: dict, insertion: bool):
      print("Active Intent: askThanks ")
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
              storeDataIntoDBMySql(data_to_store, insertion)
      except KeyError:
         status = "Error"
         print('Error while storing or getting the data')
      return status + "in storing data"


def storeDataIntoDBMySql(dic: dict, insertion: bool):
    print("Inside Saving into MySql")
    try:
        cnx = mysql.connector.connect(
            user='admin',
            password='LpgKASCOqNsGpsFvY8Vh',
            host='meal-ticket.cqycsjh1wnuy.us-east-1.rds.amazonaws.com',
            database='MealTicket'
        )
        
        data = (dic.get("session_id", "1"), dic.get("person_name", ""),
                dic.get("person_role", ""), 
                dic.get("restaurant_name", ""), 
                dic.get("city", ""), 
                dic.get("street_address", ""),
                dic.get("cuisine_types", ""),
                dic.get("resource_idle", ""), dic.get("other_apps", ""),
                dic.get("app_costing", ""), dic.get("adding_sales_costing", ""),
                dic.get("equipments", ""),
                dic.get("timestamp", ""),
                dic.get("extra_capacity", ""))
        if (insertion):
            cursor = cnx.cursor()
            # Define the insert query
            insert_query = ("INSERT INTO MealTicketUsers"
                            "(session_id, person_name, person_role, restaurant_name, city, street_address, cuisine_types, resource_idle, other_apps, app_costing, adding_sales_costing, equipments, dates, extra_capacity)"
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(insert_query, data)
            cnx.commit()
        else:
            print(type(data))
            cursor = cnx.cursor()
            update_query = f"""UPDATE MealTicketUsers SET  
                           person_name = {data[1]}, person_role= {data[2]}, 
                           restaurant_name = {data[3]}, city={data[4]}, 
                           street_address = {data[5]}, cuisine_types = {data[6]}, 
                           resource_idle={data[7]}, other_apps = {data[8]},
                           app_costing = {data[9]}, adding_sales_costing = {data[10]},
                           equipments = {data[11]}, dates = {data[12]}, 
                           extra_capacity = {data[13]} where session_id = {data[0]}
                           """
            print("Update Query=", update_query)
            cursor.execute(update_query)
            cnx.commit()
    except Exception as e:
        print("Error while inserting data mysql:", e)
    return "Data saved into DB"
    
    
def refine_data(user_data, session_id):
    print(f'data to be refine: {user_data}')
    refine_user_data = {
        "person_name": user_data.get("person", ""),
        "person_role": user_data.get("Role.original", ""),
        "restaurant_name": user_data.get("resturant-name", ""),
        "city": user_data.get("geo-city", ""),
        "street_address": user_data.get("street-address", ""),
        "cuisine_types": ", ".join(user_data.get("cuisine.original", "")),
        "resource_idle": user_data.get("ResourceIdleNess", ""),
        "other_apps": ", ".join(user_data.get("app-names", "")),
        "app_costing": user_data.get("app-fee", ""),
        "adding_sales_costing": user_data.get("number.original", ""),
        "equipments": ", ".join(user_data.get("Equipment.original", "")),
        "extra_capacity": user_data.get("CapacityType", ""),
        "timestamp": str(datetime.datetime.now()),
        "session_id": session_id.replace("projects/mealticket-bdeo/agent/sessions/dfMessenger-", "")
    }
    print(f'data to push: {refine_user_data}')
    return refine_user_data


if __name__ == '__main__':
    # Close the log file when the application exits
    app.run()
