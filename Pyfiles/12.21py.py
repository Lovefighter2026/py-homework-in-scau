class RomanNumber:
    def __init__(self, roman_string):
        """
        初始化RomanNumber对象
        :param roman_string: 罗马数字字符串
        """
        self.__roman_string = roman_string.upper()  # 私有属性
        self.__roman_to_int_map = {  # 私有属性
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    # Getter 和 Setter 方法
    def get_roman_string(self):
        """获取罗马数字字符串"""
        return self.__roman_string
    
    def set_roman_string(self, roman_string):
        """设置罗马数字字符串"""
        self.__roman_string = roman_string.upper()
    
    def roman_to_int(self):
        """
        将罗马数字转换为整数
        """
        if not self.__roman_string:
            return 0
        
        if not self._is_valid_roman():
            raise ValueError(f"无效的罗马数字: {self.__roman_string}")
        
        total = 0
        prev_value = 0
        
        for char in reversed(self.__roman_string):
            current_value = self.__roman_to_int_map[char]
            
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value
        
        return total
    
    def _is_valid_roman(self):
        """
        验证罗马数字字符串是否有效
        """
        for char in self.__roman_string:
            if char not in self.__roman_to_int_map:
                return False
        
        return True
    
    def _get_roman_string_internal(self):
        """内部使用的getter方法"""
        return self.__roman_string
    
    def __repr__(self):
        int_value = self.roman_to_int()
        return f"RomanNumber('{self.__roman_string}' = {int_value})"
    
    def __str__(self):
        return self.__roman_string


# 定义子类
class RomanNumberChild(RomanNumber):
    """
    RomanNumber 的子类，增加整数转罗马数字、算术运算等功能
    """
    
    @staticmethod
    def int_to_Roman(num):
        """
        将整数转换为罗马数字字符串
        :param num: 要转换的整数 (1-3999)
        :return: 罗马数字字符串
        """
        if not isinstance(num, int):
            raise TypeError("输入必须是整数")
        
        if num <= 0:
            raise ValueError("罗马数字只能表示正整数")
        
        if num > 3999:
            raise ValueError("罗马数字表示范围是1-3999")
        
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        
        return roman_num
    
    @classmethod
    def from_int(cls, num):
        """
        类方法：从整数创建 RomanNumberChild 对象
        :param num: 整数
        :return: RomanNumberChild 对象
        """
        roman_str = cls.int_to_Roman(num)
        return cls(roman_str)
    
    def add(self, other):
        """
        加法运算（返回罗马数字字符串）
        :param other: 另一个 RomanNumberChild 对象
        :return: 结果的罗马数字字符串
        """
        if not isinstance(other, RomanNumberChild):
            raise TypeError("只能与 RomanNumberChild 对象相加")
        
        result = self.roman_to_int() + other.roman_to_int()
        if result > 3999:
            raise ValueError("结果超出罗马数字表示范围")
        
        return self.int_to_Roman(result)
    
    def sub(self, other):
        """
        减法运算（返回罗马数字字符串）
        :param other: 另一个 RomanNumberChild 对象
        :return: 结果的罗马数字字符串
        """
        if not isinstance(other, RomanNumberChild):
            raise TypeError("只能与 RomanNumberChild 对象相减")
        
        result = self.roman_to_int() - other.roman_to_int()
        if result <= 0:
            raise ValueError("减法结果必须是正整数")
        
        return self.int_to_Roman(result)
    
    def is_even(self):
        """
        判断罗马数字是否为偶数
        :return: 如果是偶数返回 True，否则返回 False
        """
        return self.roman_to_int() % 2 == 0
    
    # 魔法方法实现运算符重载
    def __add__(self, other):
        """
        魔法方法：实现 + 运算符
        :param other: 另一个 RomanNumberChild 对象
        :return: 新的 RomanNumberChild 对象
        """
        if not isinstance(other, RomanNumberChild):
            raise TypeError("只能与 RomanNumberChild 对象相加")
        
        result = self.roman_to_int() + other.roman_to_int()
        if result > 3999:
            raise ValueError("结果超出罗马数字表示范围")
        
        return RomanNumberChild.from_int(result)
    
    def __sub__(self, other):
        """
        魔法方法：实现 - 运算符
        :param other: 另一个 RomanNumberChild 对象
        :return: 新的 RomanNumberChild 对象
        """
        if not isinstance(other, RomanNumberChild):
            raise TypeError("只能与 RomanNumberChild 对象相减")
        
        result = self.roman_to_int() - other.roman_to_int()
        if result <= 0:
            raise ValueError("减法结果必须是正整数")
        
        return RomanNumberChild.from_int(result)
    
    def __mul__(self, other):
        """
        魔法方法：实现 * 运算符
        :param other: 另一个 RomanNumberChild 对象 或 整数
        :return: 新的 RomanNumberChild 对象
        """
        if isinstance(other, RomanNumberChild):
            result = self.roman_to_int() * other.roman_to_int()
        elif isinstance(other, int):
            result = self.roman_to_int() * other
        else:
            raise TypeError("只能与 RomanNumberChild 对象或整数相乘")
        
        if result > 3999:
            raise ValueError("结果超出罗马数字表示范围")
        
        return RomanNumberChild.from_int(result)
    
    def __rmul__(self, other):
        """
        魔法方法：实现右侧乘法（整数 * RomanNumberChild）
        """
        return self.__mul__(other)
    
    def __repr__(self):
        """
        改进对象的字符串表示
        """
        int_value = self.roman_to_int()
        # 使用父类的内部getter方法获取私有属性
        roman_str = self._get_roman_string_internal()
        return f"RomanNumberChild('{roman_str}' = {int_value})"
    
    def __str__(self):
        """
        用户友好的字符串表示
        """
        return self._get_roman_string_internal()


# 测试代码
if __name__ == "__main__":
    print("=== 测试题目要求的功能 ===")
    
    # i. 测试 add 方法
    a = RomanNumberChild('III')
    b = RomanNumberChild('XIII')
    print(f"a.add(b) = {a.add(b)}")  # 输出: XVI
    print()
    
    # ii. 测试 is_even 方法
    print("=== 测试 is_even() 方法 ===")
    even_test = RomanNumberChild('XII')  # 12
    odd_test = RomanNumberChild('XI')    # 11
    print(f"{even_test} 是偶数吗? {even_test.is_even()}")  # 输出: True
    print(f"{odd_test} 是偶数吗? {odd_test.is_even()}")    # 输出: False
    print()
    
    # iii. 测试私有属性和getter/setter
    print("=== 测试私有属性和getter/setter ===")
    r = RomanNumber('V')
    print(f"获取罗马数字: {r.get_roman_string()}")  # 输出: V
    r.set_roman_string('IX')
    print(f"设置后罗马数字: {r.get_roman_string()}")  # 输出: IX
    print()
    
    # 回答问题1: 测试运算符重载
    print("=== 回答问题1: 测试运算符重载 ===")
    x = RomanNumberChild('IV')  # 4
    y = RomanNumberChild('II')  # 2
    
    # 使用 + 运算符
    z1 = x + y
    print(f"{x} + {y} = {z1}")  # 输出: VI (6)
    print(f"z1的类型: {type(z1)}")  # 输出: RomanNumberChild
    print(f"z1的值: {z1.roman_to_int()}")  # 输出: 6
    
    # 使用 - 运算符
    z2 = x - y
    print(f"{x} - {y} = {z2}")  # 输出: II (2)
    
    # 使用 * 运算符（RomanNumberChild * RomanNumberChild）
    z3 = x * y
    print(f"{x} * {y} = {z3}")  # 输出: VIII (8)
    
    # 使用 * 运算符（RomanNumberChild * int）
    z4 = x * 3
    print(f"{x} * 3 = {z4}")  # 输出: XII (12)
    
    # 使用 * 运算符（int * RomanNumberChild）
    z5 = 3 * x
    print(f"3 * {x} = {z5}")  # 输出: XII (12)
    print()
    
    # 回答问题2: 测试 from_int 类方法
    print("=== 回答问题2: 测试 from_int 类方法 ===")
    num1 = 25
    rn1 = RomanNumberChild.from_int(num1)
    print(f"整数 {num1} 转换为 RomanNumberChild: {rn1}")  # 输出: XXV
    print(f"rn1.roman_to_int() = {rn1.roman_to_int()}")  # 输出: 25
    print()
    
    # 回答问题3: 测试 __repr__ 方法
    print("=== 回答问题3: 测试 __repr__ 方法 ===")
    print(f"repr(a): {repr(a)}")  # 输出: RomanNumberChild('III' = 3)
    print(f"repr(b): {repr(b)}")  # 输出: RomanNumberChild('XIII' = 13)
    print()
    
    # 测试直接打印对象
    print("=== 测试直接打印对象 ===")
    print(f"a = {a}")  # 使用 __str__: 输出: III
    print(f"b = {b}")  # 输出: XIII
    print()
