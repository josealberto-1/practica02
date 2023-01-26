def temp_conversion(temp_c):
    temp_f = (temp_c * 9/5) + 32
    temp_k = temp_c + 273.15
    return temp_f, temp_k

temp_c = float(input("Ingrese la temperatura en °C: "))
temp_f, temp_k = temp_conversion(temp_c)
print("La temperatura en °F es: ", temp_f)
print("La temperatura en °K es: ", temp_k)
