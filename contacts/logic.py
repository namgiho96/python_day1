class Logic:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contacts(self):
        contacts = []
        for i in self._contacts:
            contacts.append(i.to_string)
        return ' '.join(contacts)

    def del_contact(self, name):
        for i, t in enumerate(self._contacts):
            if t.name == name:
                del self._contacts[i]