class RomanNumber:
    def __init__(self, roman_string):
        self.roman_string = roman_string.upper() 
        self.roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def roman_to_int(self):
        total = 0
        prev_value = 0
        for char in reversed(self.roman_string):
            current_value = self.roman_to_int_map[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value
        
        return total
    
    def __str__(self):
        return self.roman_string
    
    def __repr__(self):
        return f"RomanNumber('{self.roman_string}')"

if __name__ == "__main__":
    test_cases = [
        ('III', 3),
        ('XIII', 13),
        ('IV', 4),
        ('IX', 9),
        ('LVIII', 58),  
        ('MCMXCIV', 1994), 
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000),
        ('MMXXIII', 2023), 
    ]

    a = RomanNumber('III')
    b = RomanNumber('XIII')
    print(a.roman_to_int())  
    print(b.roman_to_int())  


