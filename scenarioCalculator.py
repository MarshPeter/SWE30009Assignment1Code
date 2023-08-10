class Calculator:
    def __init__(self):
        self.possibilities = ['+', '-', '*', '/']

    # returns true if the scenario accomplishes the test objective
    def calculateScenario(self, x, y):
        correctAnswer = self.calculate('-', '*', x, y)
        for symbolOne in self.possibilities:
            for symbolTwo in self.possibilities:
                if symbolOne == '-' and symbolTwo == '*':
                    continue
                result = self.calculate(symbolOne, symbolTwo, x, y)
                if result == correctAnswer:
                    print(f"CorrectAnswer = {correctAnswer}")
                    print(x, y, result, symbolOne, symbolTwo)
                    return False

        return True

    def calculate(self, s1, s2, x, y):
        firstResult = self.firstCalculation(s1, x, y)
        return self.secondCalculation(s2, firstResult)

    def firstCalculation(self, symbol, x, y):
        if symbol == "+":
            return x + y
        elif symbol == "-":
            return x - y
        elif symbol == '*':
            return x * y
        else:
            return x / y

    def secondCalculation(self, symbol, x):
        if symbol == "+":
            return x + 2
        elif symbol == "-":
            return x - 2
        elif symbol == '*':
            return x * 2
        else:
            return x / 2

    def calculateBadSolutionsInRange(self, absVal):
        erroneousValues = []
        for n in range(-absVal, absVal):
            if not self.calculateScenario(n, 1):
                erroneousValues.append(n)

        return erroneousValues


print("Task 3 Start")
task3Tester = Calculator()
print("Testing (2, 1)")
print(task3Tester.calculateScenario(2, 1))
print("Task 3 end")

print("task 4 start")
task4Tester = Calculator()
print(task4Tester.calculateBadSolutionsInRange(10000))
print("task 4 End")
