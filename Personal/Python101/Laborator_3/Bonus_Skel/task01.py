class Complex:

    def __init__(self, real_part: int = 0, imaginary_part: int = 0, var_name: str = 'var') -> None:
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        self.name = var_name

    def __str__(self) -> str:
        if self.real_part == 0 and self.imaginary_part == 0:
            return f"{self.name} = 0"
        elif self.imaginary_part == 0:
            return f"{self.name} = {self.real_part}"
        elif self.real_part == 0:
            return f"{self.name} = {self.imaginary_part}i"
        elif self.imaginary_part < 0:
            return f"{self.name} = {self.real_part} - {abs(self.imaginary_part)}i"
        else: 
            return f"{self.name} = {self.real_part} + {self.imaginary_part}i"

    def add_complex_numbers(self, other) -> None:
        self.real_part += other.real_part
        self.imaginary_part += other.imaginary_part

    def substract_complex_numbers(self, other) -> None:
        self.real_part -= other.real_part
        self.imaginary_part -= other.imaginary_part


    def multiply_complex_numbers(self, other) -> None:
        x = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        y = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        self.real_part = x
        self.imaginary_part= y       