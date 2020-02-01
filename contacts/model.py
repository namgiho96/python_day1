class Model:
    def __init__(self):
        self._name = ''
        self._phone = ''
        self._email = ''
        self._addr = ''

    @property
    def name(self) -> str:
        return self._name

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def email(self) -> str:
        return self._email

    @property
    def addr(self) -> str:
        return self._addr

    @name.setter
    def name(self, name):
        self._name = name

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @email.setter
    def email(self, email):
        self._email = email

    @addr.setter
    def addr(self, addr):
        self._addr = addr

    def to_string(self):
        return '이름 : {}, 전화번호 : {}, 이메일 : {}, 주소 : {}' \
            .format(self._name, self._phone, self._email, self._addr)
