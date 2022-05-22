class DivisibleNumberFile:
    def __init__(self):
        self.number = int (input("Enter The Number :"))
    def CheckDivisibility(self):
        for num in range(2,15):
            if self.number % num == 0:
                print(f"{self.number} is divisible by {num}")

