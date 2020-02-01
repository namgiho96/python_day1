from contacts.model import Model
from contacts.logic import Logic


class Ctrl:
    def __init__(self):
        self.logic = Logic()

    def register(self, name, email, phone, addr):
        model = Model()
        model.name = name
        model.email = email
        model.phone = phone
        model.addr = addr
        self.logic.add_contact(model)

    def list(self):
        return self.logic.get_contacts()

    def remove(self, name):
        self.logic.del_contact(name)
