# __init__ 먼저 실행 하라는 명령어
# 실질 적으로 알고리즘을 활요하는 로직
from calcaulator.model import Model
from calcaulator.logic import Logic


class Controller:
    def exec(self, num1, num2, opcode):
        model = Model()
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        logic = Logic(model)

        opcodes = {
            '+': logic.add(),
            '-': logic.subract(),
            '*': logic.multiply(),
            '/': logic.divide()
        }

        return opcodes[opcode]










