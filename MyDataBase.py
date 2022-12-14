import json

class DataBase:

    def add_data(self,name,email,password):

        with open('DataBase.json','r') as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = [name,password]
            with open('DataBase.json','w') as wf:
                json.dump(database,wf)
                return 1

    def search(self,email,password):
        with open('DataBase.json','r') as rf:
            database = json.load(rf)

            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            return 0
