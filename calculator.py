class Calculator:
    
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно!")
        return a / b

    def is_prime_number(self, n):
        if n <= 1:
            return False
        
        for i in range(2, n):
            if n % i == 0:
                return False
        
        return True