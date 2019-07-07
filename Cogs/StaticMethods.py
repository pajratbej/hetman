from pymongo import MongoClient
import random as r
import os

client = MongoClient(os.environ["MONGO_LAB"])
db = client.get_database("hetmanbot")
collection = db['data_base']

class StaticMethods():
    @staticmethod
    def push_record(name, txt, number):
        records = collection.find_one({"document_id": number})

        for i in records[name]:
            if txt[10:] == str(list(i.values()))[2:-2]:
                return "Ten cytat już istnieje"
            else:
                size = len(records[name])
                print(records[name])
                collection.update({"document_id": number}, {'$push': {name: {str(size): txt[10:]}}})
                print("Dodano nowy cytat")
                return "Dodano nowy cytat"
    @staticmethod
    def get_random_record(name, number):
        records = collection.find_one({"document_id": number})
        for i in records[name]:
            str(list(i.values()))[2:-2]

        return str(list(r.choice(records[name]).values()))

    @staticmethod
    def get_specific_record(name, number, r_number):
        records = collection.find_one({"document_id": number})
        return str(list(records[name][r_number].values()))

    @staticmethod
    def number_of_quotes(name, number):
        records = collection.find_one({"document_id": number})
        size = len(records[name])
        return size
                    
    @staticmethod
    def replace(string):
        collection.update({"document_id": 3}, {'$set' : {"plan": string}})
                
    @staticmethod
    def getPlan():
        record = collection.find_one({"document_id": 3})
        return record["plan"]
