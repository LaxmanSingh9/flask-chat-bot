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
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "Manager",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Owner",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Staff",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Other",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    
                            
                                ]
                            }
                        ]
                    ]
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
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "Freezer",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Fryer",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Oven",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "More than one",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    ]
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

def getRespOfAskCityName(restaurant_name: str, user_context: dict):
    msg = f"Great, it's {restaurant_name}! In which city is your restaurant located?"
    response = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [msg]
                }
            },
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "Los Angeles",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Seattle",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "London",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Other",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    ]
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
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "above 1000 $",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "above 2000 $",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "above 3000 $",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    }
                            
                                ]
                            }
                        ]
                    ]
                }
          }
        ],
        "outputContexts": user_context
     }
    return response


def getRespOfDefaultContext(user_context: dict):
    msg = "Sorry for any misunderstanding. Would you like to continue with us?"
    response = {
        "fulfillmentMessages": [
         {
             "text": {
                 "text": [msg]
             }
         },
         {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "Restart",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Quit",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    }
                            
                                ]
                            }
                        ]
                    ]
                }
            }
        ],
        "outputContexts": user_context
     }
    return response


def getRespOfAskCuisine(resturant_name: str, user_context: dict):
    msg = f"Thank you, Can you please let us know the type of cuisine that {resturant_name} offers?"
    response = {
        "fulfillmentMessages": [
         {
             "text": {
                 "text": [msg]
             }
         },
         {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "American",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Mexican",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Italian",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    {
                                        "text": "Other",
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        }
                                    },
                                    
                            
                                ]
                            }
                        ]
                    ]
                }
            }
        ],
        "outputContexts": user_context
     }
    return response
 
