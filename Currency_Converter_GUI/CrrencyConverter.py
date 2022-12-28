#Imports
import requests
from delphifmx import *

class CurrencyConvert(Form):
    def __init__(self, owner):
        self.SetProps(Caption = "Currency Converter App", width=350)

        #Non-editable Labels
        self.heading = Label(self)
        self.heading.SetProps(Parent = self, Text = "Currency Converter", Position = Position(PointF(70, 10)),
                              Width=200, Height=40, StyleLookup = 'listboxheaderlabel')

        self.fromm = Label(self)
        self.fromm.SetProps(Parent = self, Text = "From", Position = Position(PointF(20, 60)),
                            StyleLookup = 'listboxitemlabel')

        self.to = Label(self)
        self.to.SetProps(Parent = self, Text = "To", Position = Position(PointF(20, 180)),
                         StyleLookup = 'listboxitemlabel')

        self.C1 = Label(self)
        self.C1.SetProps(Parent = self, Text = "Currency: ", Position = Position(PointF(20, 90)))

        self.C2 = Label(self)
        self.C2.SetProps(Parent = self, Text = "Currency: ", Position = Position(PointF(20, 210)))

        self.A1 = Label(self)
        self.A1.SetProps(Parent = self, Text = "Amount: ", Position = Position(PointF(180, 90)))

        self.A2 = Label(self)
        self.A2.SetProps(Parent = self, Text = "Amount: ", Position = Position(PointF(180, 210)))

        self.A2Value = Label(self) #To display converted value
        self.A2Value.SetProps(Parent = self, Text = "-", Position = Position(PointF(180, 240)))

        #Editable textboxes
        self.editA1 = Edit(self) #Currency1 amount
        self.editA1.SetProps(Parent = self, Position = Position(PointF(180, 120)), Height = 20)

        #Drop menu for currency
        self.comboC1 = ComboBox(self) #Currency1 name
        self.comboC1.SetProps(Parent = self, Position = Position(PointF(20, 120)), Height = 20)

        self.comboC2 = ComboBox(self) #Currency2 name
        self.comboC2.SetProps(Parent = self, Position = Position(PointF(20, 240)), Height = 20)

        #Getting Country Codes
        self.__load_country_codes()

        #Button
        self.convert = Button(self)
        self.convert.SetProps(Parent = self, Text = "Convert", Position = Position(PointF(170, 300)),
                              Width = 100, OnClick = self.__button_click_convert)

    def __load_country_codes(self):
        pass

    def __button_click_convert(self, sender): #Method called when convert button clicked
        pass

def main():
    Application.Initialize()
    Application.Title = "Currency Converter Using Delphi FMX"
    Application.MainForm = CurrencyConvert(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()