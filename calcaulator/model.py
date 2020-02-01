# 데코레이터 패턴이다 프로 퍼티를 가져오는 공간
class Model:
    def __init__(self):
        self._num1 = 0
        self._num2 = 0
        self._opcode = ''

    @property
    def num1(self) -> int:
        return self._num1

    @num1.setter
    def num1(self, num1):
        self._num1 = num1

    @property
    def num2(self) -> int:
        return self._num2

    @num2.setter
    def num2(self, num2):
        self._num2 = num2

    @property
    def opcode(self) -> str:
        return self._opcode

    @opcode.setter
    def opcode(self, opcode):
        self._opcode = opcode

