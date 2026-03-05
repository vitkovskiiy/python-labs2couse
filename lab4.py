tempCelsius = int(input("Write current temp Celsium : "))

def toFahrenheit(temp):
  converted = temp * 1.8 + 32
  return converted

print(toFahrenheit(tempCelsius))
 