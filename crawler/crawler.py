"""
    PYTON FILE TO GENERATE AND SAVE ALL THE APIS CRAWLED TO THE DATABASE
    LANGUAGE: PYTHON
    DATABSE: SQL (RELATIONAL DATABASE)(LIBRARY: SQLITE)
    
"""





# REQUIRED LIBRARIES
import requests
import json
import time
import threading

# IMPORT THE DATABASE CLASS
from database import Database


# TOKEN VARIABLE
token_generated = ""

# FUNCTION TO REGENERATE THE TOKEN
def token_regeneration():
    global token_generated
    generate_session_token()
    print("\n------------------------- ATTENTION TOKEN RENEWED -------------------------\n")
    myThread.run()

# THREAD TO REGENERARTE TOKEN AFTER 250 SECONDS
myThread = threading.Timer(250, token_regeneration)


# FUNCTION TO GENERATE A TOKEN    
def generate_session_token():
    # URL FROM POSTMAN API
    url = "https://public-apis-api.herokuapp.com/api/v1/auth/token"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    json_object = json.loads(response.text)
    global token_generated
    token_generated = json_object["token"]


# FUNCTIN TO SCRAP THE LIST OF CATEGORIES
# ARGUMENT: AUTHENTICATION TOKEN
# RETURN: LIST OF CATEGORIES
def scrap_categories():
    
    payload={}
    global token_generated
    headers = {"Authorization": "Bearer "+token_generated }

    url = "https://public-apis-api.herokuapp.com/api/v1/apis/categories?page=1"
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    categories_list_json_object = json.loads(response.text)

    # EXTRACT CATEGORIES OF FIRST PAGE
    category_list = categories_list_json_object["categories"]
    # print(category_list)

    # CHECK FOR MORE PAGES
    if(categories_list_json_object['count'] % 10 != 0):
        n_pages = categories_list_json_object['count'] // 10 + 1
    else:
        n_pages = categories_list_json_object['count'] // 10

    # PRINT NUMBER OF PAGES
    print("NUMBER OF CATEGORY PAGES: {}\n".format(n_pages))

    # EXTRACT CATEGORIES FROM FURTHER PAGES
    # THUS, PAGINATION IS SUPPORTED
    for i in range(1,n_pages):
        url = "https://public-apis-api.herokuapp.com/api/v1/apis/categories?page={}".format(i+1)
        response = requests.request("GET", url, headers=headers, data=payload)
        # print(response.text)
        categories_list_json_object = json.loads(response.text)
        category_list = category_list + categories_list_json_object["categories"]

    return category_list

# FUNCTIN TO GET THE NUMBER OF PAGES IN A CATEGORY
# ARGUMENT: AUTHENTICATION TOKEN, CATEGORY
# RETURN: CEIL(NUMBER OF APIS IN THE CATEGORY / 10 )
def apiPagesInCategory(cat):
        # SLEEP TO ENSURE RATE LIMIT IS NOT CROSSED
        time.sleep(6)
        payload={}
        global token_generated
        headers = {"Authorization": "Bearer "+ token_generated }
        api_url = "https://public-apis-api.herokuapp.com/api/v1/apis/entry?page=1&category={}".format(cat)
        print(api_url)
        catlist_response = requests.request("GET", api_url, headers=headers, data=payload)
        # print(catlist_response)
        json_cat_api_list = json.loads(catlist_response.text)
        # print(json_cat_api_list)

        if(json_cat_api_list['count'] % 10 != 0):
            api_pages = json_cat_api_list['count'] // 10 + 1
        else:
            api_pages = json_cat_api_list['count'] // 10
        
        return api_pages



# FUNCTIN TO GENERATE A LIST OF API ON THE NTH PAGE
# ARGUMENT: AUTHENTICATION TOKEN, N VALUE, CATEGORY
# RETURN: API DATA
def pageApiList(i, cat):

    # SLEEP TO ENSURE RATE LIMIT IS NOT CROSSED
    time.sleep(6)
    payload={}
    global token_generated
    headers = {"Authorization": "Bearer "+token_generated }
    api_url = "https://public-apis-api.herokuapp.com/api/v1/apis/entry?page={}&category={}".format(i+1,cat)
    print(api_url)
    catlist_response = requests.request("GET", api_url, headers=headers, data=payload)
    # print(catlist_response)
    json_api_list = json.loads(catlist_response.text)
    return json_api_list







# MAIN FUNCTION
def main():
    # FIRST TIME GENERATE THE TOKEN
    global token_generated 
    generate_session_token()
    
    # GET CATEGORIES
    category_list = scrap_categories()

    # INITIALIZE DATABASE
    db = Database("database1.db")

    # SAVE CATEGORIES IN DATABSE
    categories = db.save_categories(category_list)
 
    # START MULTI THREADING 
    # TO ENSURE THE NEW TOKEN IS REGENERATED (250s)
    # BEFORE THE PREVIOS TOKEN IS EXPIRED
    myThread.start()
    
    # ITERATE OVER EACH CATEGORY
    for id, cat in categories:

        print("---------------------------------------------------")
        print("{} : {}".format(id, cat))

        # GET NUMBER OF PAGES IN A CATEGORY
        api_pages = apiPagesInCategory(cat)
        print("NUMBER OF API PAGES: {}\n".format(api_pages))

        # ITERATE  OVER ALL PAGES IN A CATEGORY
        for i in range(api_pages):
            
            print("PAGE-{}".format(i+1))

            # GENERATE LIST OF APIS IN A PAGE
            api_list = pageApiList(i, cat)
    
            # SAVE THE APIS IN iTH PAGE IN THE DB
            for api in api_list["categories"]:
                print("API: {} - LINK: {} - CAT_ID: {}".format(api['API'], api['Link'], id))
                db.saveApi(id, api['API'], api['Link'])

    # STOP THREADING IE STOP REGENERATING THE TOKEN
    if myThread.is_alive():
        myThread.cancel()


# START PROGRAM
main()



################## END OF THE PROGRAM #############################