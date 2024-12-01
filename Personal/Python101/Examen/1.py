def count_lucky_numbers(N, lucky_digits, G, unlucky_digits, a, b):
    lucky = set(lucky_digits)
    unlucky = set(unlucky_digits)
    is_lucky = lambda num: any(int(digit) in lucky for digit in str(num)) and not any(int(digit) in unlucky for digit in str(num))
    
    return sum(1 for num in range(a, b + 1) if is_lucky(num))

if __name__ == "__main__":
  # Citim datele de intrare
  N, *lucky_digits = map(int, input().split())
  G, *unlucky_digits = map(int, input().split())
  a, b = map(int, input().split())

  # Apelam functia si afisam rezultatul
  print(count_lucky_numbers(N, lucky_digits, G, unlucky_digits, a, b))
 