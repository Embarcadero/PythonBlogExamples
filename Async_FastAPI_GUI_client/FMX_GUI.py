import requests
from delphifmx import *

BASE = "http://127.0.0.1:8000/" # Base URL where the web service is being hosted locally

class EmployeeManager(Form):
    def __init__(self, owner):
        self.SetProps(Caption = "Employee Management", Width = 600, Height = 420)

        # Adding labels for each textbox
        self.fName = Label(self)
        self.fName.SetProps(Parent = self, Text = "First Name: ", Position = Position(PointF(20, 20)))

        self.lName = Label(self)
        self.lName.SetProps(Parent = self, Text = "Last Name: ", Position = Position(PointF(20, 50)))

        self.gender = Label(self)
        self.gender.SetProps(Parent = self, Text = "Gender: ", Position = Position(PointF(20, 80)))

        self.role = Label(self)
        self.role.SetProps(Parent = self, Text = "Role: ", Position = Position(PointF(20, 110)))

        self.year = Label(self)
        self.year.SetProps(Parent = self, Text = "Year Joined: ", Position = Position(PointF(20, 140)))

        self.id = Label(self)
        self.id.SetProps(Parent = self, Text = "Employee ID: ", Position = Position(PointF(400, 60)))

        # Adding textboxes
        self.editFName = Edit(self)
        self.editFName.SetProps(Parent = self, Position = Position(PointF(100, 20)), Height = 20)

        self.editLName = Edit(self)
        self.editLName.SetProps(Parent = self, Position = Position(PointF(100, 50)), Height = 20)

        self.editGender = Edit(self)
        self.editGender.SetProps(Parent = self, Position = Position(PointF(100, 80)), Height = 20)

        self.editRole = Edit(self)
        self.editRole.SetProps(Parent = self, Position = Position(PointF(100, 110)), Height = 20)

        self.editYear = Edit(self)
        self.editYear.SetProps(Parent = self, Position = Position(PointF(100, 140)), Height = 20)

        self.editId = Edit(self)
        self.editId.SetProps(Parent = self, Position = Position(PointF(400, 80)), Height = 20)

        # Adding buttons to call the 3 methods of our API endpoint
        self.addEmployee = Button(self)
        self.addEmployee.SetProps(Parent = self,Text = "Add Employee", Position = Position(PointF(250, 110)),
                                  Width = 100, OnClick = self.__button_click_add)

        self.view = Button(self)
        self.view.SetProps(Parent = self, Text = "View Employees", Position = Position(PointF(250, 140)),
                           Width = 100, OnClick = self.__button_click_view)

        self.update = Button(self)
        self.update.SetProps(Parent = self, Text = "Update Employee", Position = Position(PointF(400, 110)),
                             Width = 100, OnClick = self.__button_click_update)

        self.delete = Button(self)
        self.delete.SetProps(Parent = self, Text = "Delete Employee", Position = Position(PointF(400, 140)),
                             Width = 100, OnClick = self.__button_click_delete)

        # List box to display all API call responses or any other messages
        self.list = ListBox(self)
        self.list.SetProps(Parent = self, Position = Position(PointF(20, 170)),
                           Width = 550, Height = 200)

    def __button_click_add(self, sender): # Called when addEmployee button clicked
        data = {"firstName":self.editFName.text,
                "lastName":self.editLName.text,
                "gender":self.editGender.text,
                "role":self.editRole.text,
                "joinYear":int(self.editYear.text)}
        endpointURL = BASE+"employees"
        response = requests.post(endpointURL, params=data)
        self.list.items.add("Your Entry was successfully added!")
        self.list.items.add(response.json())

        self.editFName.text = self.editLName.text = self.editGender.text = self.editRole.text = self.editYear.text = ""

    def __button_click_update(self, sender): # Called when update button clicked
        # If conditions to support the optional feature of your update call
        if self.editFName.text=="":
            fname = None
        else:
            fname = self.editFName.text
        if self.editLName.text=="":
            lname = None
        else:
            lname = self.editLName.text
        if self.editGender.text=="":
            gender = None
        else:
            gender = self.editGender.text
        if self.editRole.text=="":
            role = None
        else:
            role = self.editRole.text
        if self.editYear.text=="":
            year = None
        else:
            year = int(self.editYear.text)

        endpointURL = BASE+"employees/"
        data = {"firstName":fname ,
                "lastName":lname ,
                "gender":gender,
                "role":role,
                "joinYear":year}
        response = requests.put(endpointURL+str(self.editId.text), params=data)
        response = response.json()
        self.list.items.add("Your Entry was successfully updated!")
        self.list.items.add(response)

    def __button_click_view(self, sender): # Called when view button clicked
        response = requests.get(BASE + "employees")
        response = response.json()

        if response != []:
            for employee in response:
                self.list.items.add(employee)
        else:
            self.list.items.add("Your Employee Database is empty!")

    def __button_click_delete(self, sender):
        endpointURL = BASE+"employees/"
        response = requests.delete(endpointURL+str(self.editId.text))
        response = response.json()
        self.list.items.add("Your Entry was successfully deleted!")
        self.list.items.add(response)



def main():
    Application.Initialize()
    Application.Title = "Employee Management Using Delphi FMX"
    Application.MainForm = EmployeeManager(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()



if __name__ == '__main__':
    main()