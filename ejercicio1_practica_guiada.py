# 🎯 Práctica Guiada: Ejercicios Progresivos

# Ejercicio 1: Análisis básico de ventas 🍦🍧🍨
# Objetivo: Practicar variables, operadores y condicionales

# Datos
enero = 2000
febrero = 2800
marzo = 4800
abril = 5000
mayo = 5500
junio = 5200
julio = 6000
agosto = 8000
septiembre = 7000
octubre = 4000
noviembre = 2000
diciembre = 2800

total = (enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + diciembre)
print(total)

# Tu código aquí
# Diccionario ventas mensuales
ventas_mensuales = {
    "enero": enero,
    "febrero": febrero,
    "marzo": marzo,
    "abril": abril,
    "mayo": mayo,
    "junio": junio,
    "julio": julio,
    "agosto": agosto,
    "septiembre": septiembre,
    "octubre": octubre,
    "noviembre": noviembre,
    "diciembre": diciembre,
}

# Suma ventas anuales
print("\033[1mAnálisis básico de ventas 🍦🍧🍨\033[0m") #Texto en negrita
ventas_anuales = sum(ventas_mensuales.values())
print(f" 📊 Total ventas anuales: {ventas_anuales}")

# Promedio
promedio = ventas_anuales/12
print(f" 📈 Promedio: {promedio}")

# Promedio redondeado
promedio_redondeado = round(promedio)
print(f"Promedio mensual redondeado: {promedio_redondeado}")
print(f"Promedio mensual redondeado con f: {promedio:.2f}") #Dentro de las llaves puedes poner formato del número: :=empieza la instruccion de formato, 2=decimales  f=float(decimal)

# Meta anual - Mes máximo - Valor máximo
meta_anual = 50000
mes_maximo = max(ventas_mensuales, key=ventas_mensuales.get) #key=ventas_mensuales.get=Busca la clave cuyo valor en el diccionario sea el más grande.
valor_maximo = ventas_mensuales[mes_maximo]
print (f" 🏆 El mes con más ventas es: {mes_maximo}, con unas ventas de 🎯 {valor_maximo}")

# Mirar si hemos alcanzado la meta anual desde la variable
if ventas_anuales >= meta_anual:
    print(f" 🎉 ¡Meta alcanzada! Ventas: {ventas_anuales}")
else:
    print(f"❌ Meta no alcanzada. Ventas: {ventas_anuales} / Meta: {meta_anual}")

# Prints de colores Color	Código 🔴 Rojo: \033[91m 🟢 Verde: \033[92m
if ventas_anuales >= meta_anual:
    print(f"\033[92m🎉 Meta alcanzada. Ventas: {ventas_anuales}\033[0m")
else:
    print(f"\033[91m❌ Meta no alcanzada. Ventas {ventas_anuales} / {meta_anual}\033[0m")



