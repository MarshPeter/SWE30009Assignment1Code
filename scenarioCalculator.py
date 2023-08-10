class Calculator:
    def __init__(self):
        self.possibilities = ['+', '-', '*', '/']

    def calculateScenario(self, x, y):
        correctAnswer = self.calculate('-', '*', x, y)
        print(f"CorrectAnswer = {correctAnswer}")
        for symbolOne in self.possibilities:
            for symbolTwo in self.possibilities:
                if symbolOne == '-' and symbolTwo == '*':
                    continue
                result = self.calculate(symbolOne, symbolTwo, x, y)
                print(result, symbolOne, symbolTwo)
                if result == correctAnswer:
                    return False

        return True

    def calculate(self, s1, s2, x, y):
        firstResult = self.firstCalculation(s1, x, y)
        return self.secondCalculation(s2, firstResult)

    def firstCalculation(self, s1, x, y):
        if s1 == "+":
            return x + y
        elif s1 == "-":
            return x - y
        elif s1 == '*':
            return x * y
        else:
            return x / y

    def secondCalculation(self, s2, x):
        if s2 == "+":
            return x + 2
        elif s2 == "-":
            return x - 2
        elif s2 == '*':
            return x * 2
        else:
            return x / 2


print("Task 3 Start")
task3Tester = Calculator()
print(task3Tester.calculateScenario(2, 1))
print("Task 3 end")
