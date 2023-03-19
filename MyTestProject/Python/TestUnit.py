import os
from delphifmx import *


class TestForm(Form):

    def __init__(self, owner):
        self.taskEdit = None
        self.Label1 = None
        self.btnAdd = None
        self.bthDelete = None
        self.listBox = None
        self.LoadProps(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "TestUnit.pyfmx"))

    def btnAddClick(self, Sender):
        if self.taskEdit.Text != '':
            self.listBox.Items.Add(self.taskEdit.Text)
            self.taskEdit.Text = ''

    def bthDeleteClick(self, Sender):
        index = self.listBox.ItemIndex
        if index >= 0:
            self.listBox.Items.Delete(index)
