import json

class Json:
    def save_info(self,data):
        data_list=[]
        data_list.append(data)
        with open('data.json', 'w') as json_file:
            json.dump(data_list,json_file,indent=4)

    def read_info(self):
        with open("data.json","r+") as file:
            data = json.load(file)
            for x in data:
                my_data=x
        return my_data

#w  = Json()
#print(w.read_info())






