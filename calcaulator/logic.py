# 로직을 저장하는 공간 수식이나 연산 알고리증 넣는곳
class Logic:
    def __init__(self, payload):
        self._num1 = payload.num1
        self._num2 = payload.num2

    def add(self):
        return self._num1 + self._num2

    def subract(self):
        return self._num1 - self._num2

    def multiply(self):
        return self._num1 * self._num2

    def divide(self):
        return self._num1 / self._num2
