minutes = int(input("Ingresa una cantidad de minutos: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} minutos son {hours} horas y {remaining_minutes} minutos.")
