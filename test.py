import requests
import time
url = "https://public-apis-api.herokuapp.com/api/v1/auth/token"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)


import json

json_object = json.loads(response.text)

token_generated = json_object["token"]

print(token_generated)


url = "https://public-apis-api.herokuapp.com/api/v1/apis/categories"

payload={}
headers = {"Authorization": "Bearer "+token_generated }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
json_object = json.loads(response.text)

# token_generated = json_object["categories"]
# print(token_generated)


print("PAGE-{}".format(1))
time.sleep(10)
payload={}
headers = {"Authorization": "Bearer "+token_generated }
api_url = "https://public-apis-api.herokuapp.com/api/v1/apis/entry?page={}&category={}".format(1,"Data Validation")
print(api_url)
catlist_response = requests.request("GET", api_url, headers=headers, data=payload)
# print(catlist_response)
json_api_list = json.loads(catlist_response.text)
print(json_api_list)
for api in json_api_list["categories"]:
    # print(api)
    print("********")
    print("API: {} - LINK: {} - CAT_ID: {}".format(api['API'], api['Link'], id))
    # cur.execute("INSERT INTO products(category, apiName, link) VALUES (?,?,?)", 
    # (id,api['API'], api['Link']))


print("PAGE-{}".format(2))
time.sleep(10)
payload={}
headers = {"Authorization": "Bearer "+token_generated }
api_url = "https://public-apis-api.herokuapp.com/api/v1/apis/entry?page={}&category={}".format(2,"Data Validation")
print(api_url)
catlist_response = requests.request("GET", api_url, headers=headers, data=payload)
# print(catlist_response)
json_api_list = json.loads(catlist_response.text)
print(json_api_list)
for api in json_api_list["categories"]:
    # print(api)
    print("********")
    print("API: {} - LINK: {} - CAT_ID: {}".format(api['API'], api['Link'], id))



# url = "https://public-apis-api.herokuapp.com/api/v1/apis/entry?page=1&category=Animals"

# payload={}
# # headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
# print("\n\n")
# # print(response.text)

# json_object = json.loads(response.text)
# print(json_object)
# for cat in json_object["categories"]:
#     print(cat)
#     print("\n")

# url = "https://public-apis-api.herokuapp.com/api/v1/apis/entry?page=2&category=Animals"

# payload={}
# # headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
# print("\n\n")
# # print(response.text)

# json_object = json.loads(response.text)
# print(json_object)
# for cat in json_object["categories"]:
#     print(cat)
#     print("\n")
    