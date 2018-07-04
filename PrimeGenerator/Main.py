
class PrimeGenerator:

    def __init__(self):
        self.value = 2

    def __is_prime(self, x):
        for i in range(2, x):
            if x % i == 0 and x != i:
                return False

        return True
        

    def next(self):
        x = self.value + 1
        while not(self.__is_prime(x)):
            x = x + 1
        self.value = x

    def get_val(self):
        return self.value



gen = PrimeGenerator()
#print(gen.get_val())
for x in range(100):
    print(gen.get_val())
    gen.next()






