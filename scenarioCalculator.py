class Calculator:
    def __init__(self):
        self.possibilities = ['+', '-', '*', '/']

    def calculateScenario(self, x, y):
        correctAnswer = self.calculate('-', '*', x, y)
        for symbolOne in self.possibilities:
            for symbolTwo in self.possibilities:
                if symbolOne == '-' and symbolTwo == '*':
                    continue
                result = self.calculate(symbolOne, symbolTwo, x, y)
                if result == correctAnswer:
                    print(f"CorrectAnswer = {correctAnswer}")
                    print(result, symbolOne, symbolTwo)
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

    def calculateBadSolutionsInRange(self, absVal):
        erroneous = []
        for n in range(-absVal, absVal):
            if not self.calculateScenario(n, 1):
                erroneous.append(n)

        return erroneous


print("Task 3 Start")
task3Tester = Calculator()
print(task3Tester.calculateScenario(2, 1))
print("Task 3 end")

print("task 4 start")
task4Tester = Calculator()
print(task4Tester.calculateBadSolutionsInRange(10000))
print("task4End")
