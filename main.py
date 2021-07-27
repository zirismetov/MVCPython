import json

class Model:
    def __init__(self):
        with open('data.json', 'r') as file:
            self.datasource = json.load(file)

    def getdata(self):
        return self.datasource

    def setdata(self, newdata):
        self.datasource = newdata


class Controller:
    @staticmethod
    def add_data(key, value):
        data = m.getdata()
        data[key] = value
        m.setdata(data)

    @staticmethod
    def delete_data(key):
        data = m.getdata()
        del data[key]
        m.setdata(data)

    @staticmethod
    def view_data():
        new_json = json.dumps(m.getdata(), indent=2)
        return new_json

    def __init__(self, action):
        if str(action).lower() == 'add':
            inp = input("Enter key and value like: 'key value' ")
            inp = inp.split()
            try:
                self.add_data(inp[0], inp[1])
            except NameError:
                print("Enter valid 'key value'")
        elif str(action).lower() == 'delete':
            inp = input("Enter key to delete: ")
            try:
                self.delete_data(inp)
            except NameError:
                print("Enter valid key " + NameError)
        elif str(action).lower() == "view":
            print(self.view_data())

class View:

    @staticmethod
    def printFile():
        with open('export.json', 'w') as ex:
            json.dump(m.getdata(), ex, indent= 2)

m = Model()
v = View()
# Write your action to controller:
c = Controller('view')
v.printFile()