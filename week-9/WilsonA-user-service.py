#
#============================================
# Title:  wilsonA-user-service.py 
# Author: Professor Krasso
# Modified By: Aaron Wilson
# Date: 25 June 2019
# Description: Finding/Adding in Python
#===========================================
#

from pymongo import MongoClient
import pprint
import datetime 

client = MongoClient('localhost', 27017)

db = client.web335

user = {
    "first_name": "Dude",
    "last_name": "Bubby",
    "email": "Bubbyd@home.com",
    "employee_id": "0000099",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id
print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000099"}))