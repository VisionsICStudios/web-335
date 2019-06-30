#
#============================================
# Title:  wilsonA-user-update.py 
# Author: Professor Krasso
# Modified By: Aaron Wilson
# Date: 25 June 2019
# Description: Finding/Updating in Python
#===========================================
#

from pymongo import MongoClient
import pprint
import datetime 

client = MongoClient('localhost', 27017)

db = client.web335

{"employee_id": "0000099"}, {
        "$set": {
            "email": "arwilson@my365.bellevue.com"
        }
}

pprint.pprint(db.users.find_one({"employee_id": "0000099", },{"date_created":0}))