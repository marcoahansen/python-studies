class Number:
    n: float
    def __init__(self, n) -> None:
        self.n = n
    def potencia(self, x: int) -> float:
        return self.n ** x 
    def fatorial(self) -> float:
      fat = 1
      for i in range(1, self.n+1):
          
  
num = Number(2)
print(num.potencia(3))