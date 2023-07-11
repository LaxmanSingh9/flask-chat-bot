import message_setter
from flask import jsonify


def setContextVariableRoles(data:dict):
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
                    if 'restaurant' in form_data:
                        context['parameters']['resturant-name'] = form_data['restaurant']
                        rest_name = form_data['restaurant']
                    if 'city' in form_data:
                        context['parameters']['geo-city'] = form_data['city']
                    if 'street' in form_data:
                        context['parameters']['street-address'] = form_data['street']
                    print("INSIDE4")
                    # Now the context variables have been updated with the new values
          resp = message_setter.getRespOfAskRoles(rest_name, user_context)

        except KeyError:
           print('Error while updating the context variables')

        return jsonify(resp)


def setContextVariableAskResturantName(data: dict):
    print("Active Intent: askResturantName")
    resp = "Error"
    try:
        user_context = data["queryResult"]["outputContexts"]
        person_name = ''
        print("INSIDE1")
        for i, context in enumerate(user_context):
            if 'session_data' in context['name']:
                print("INSIDE2")
                person_name = user_context[i]['parameters']['any.original']
                user_context[i]['parameters']['person'] = person_name

        print("user_context", user_context)
        resp = message_setter.getAskResturantNameMessage(person_name, user_context)

    except KeyError:
        print('Error while updating the context variables')

    return jsonify(resp)


def setContextVariableEquimentType(data: dict):
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
                person_name = user_context[i]['parameters']['person']

        print("user_context", user_context)
        resp = message_setter.getRespOfAskEquimentResp(person_name, user_context)

    except KeyError:
        print('Error while updating the context variables')

    return jsonify(resp)


def setContextVariableAskCityName(data: dict):
    print("Active Intent: askCityName")
    resp = "Error"
    try:
        user_context = data["queryResult"]["outputContexts"]
        resturant_name = ''
        print("INSIDE1")
        for i, context in enumerate(user_context):
            if 'session_data' in context['name']:
                print("INSIDE2")
                resturant_name = user_context[i]['parameters']['any.original']
                user_context[i]['parameters']['resturant-name'] = resturant_name
        print("user_context", user_context)
        resp = message_setter.getRespOfAskCityName(resturant_name, user_context)

    except KeyError:
        print('Error while updating the context variables')

    return jsonify(resp)


def setContextVariableAskAppFee(data: dict):
    print("Active Intent: askAppFee")
    resp = "Error"
    try:
        user_context = data["queryResult"]["outputContexts"]
        app_names = ''
        print("INSIDE1")
        for i, context in enumerate(user_context):
            if 'session_data' in context['name']:
                print("INSIDE2")
                app_names = user_context[i]['parameters']['any.original']
                user_context[i]['parameters']['app-names'] = app_names
        print("user_context", user_context)
        resp = message_setter.getRespOfAskAppFee(app_names, user_context)

    except KeyError:
        print('Error while updating the context variables')

    return jsonify(resp)
