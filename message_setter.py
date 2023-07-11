from flask import jsonify


def getAskResturantNameMessage(person_name, user_context):
    msg = f"Hello, {person_name}, and welcome to MealTicket. Can you provide us with the name of your restaurant?"
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
          ],
        "outputContexts": user_context
       }
       
    return response


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



def getRespOfAskCityName(resturant_name: str, user_context: dict):
    msg = f"Great, it's {resturant_name}! In which city is your restaurant located?"
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
                              "message": "Los Angeles",
                              "title": "Los Angeles"
                            },
                            {
                               "message": "Seattle",
                               "title": "Seattle"
                            },
                            {
                                "message": "London",
                                "title": "London"
                            },
                            {
                                "message": "Other",
                                "title": "Other"
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


def getRespOfAskAppFee(app_names: str, user_context: dict):
    print(app_names)
    msg = "Can you please provide us with an idea of the fees associated with each apps?"
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
                             "title": "above 1000 $",
                             "message": "above 1000 $"
                            },
                            {
                               "title": "above 2000 $",
                               "message": "above 2000 $"
                            },
                            {
                               "title": "above 3000 $",
                               "message": "above 3000 $"
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


def getRespOfDefaultContext(user_context: dict):
    msg = "HI, would you like to continue with us?"
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
                             "title": "restart",
                             "message": "restart"
                            },
                            {
                               "title": "quit",
                               "message": "quit"
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
 