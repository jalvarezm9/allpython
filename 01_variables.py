"""
Variables
"""

my_string_variable = "my string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_float_variable = False
print(my_float_variable)

# concatenacion de variables en un print
print(my_string_variable, my_int_to_string_variable, my_float_variable)
print("Este es el valor de", my_float_variable)

# Funciones del sistema
print(len(my_string_variable))  # len () -> cant de caracteres

# Variables en una sola linea
name, surname, alias, age = "Juan Carlos", "Alvarez", "jalvarez", 42
print("Me llamo:", name, surname, "Mi edad es:", age, ". Y mi alias es:", alias)

# input
name = input("Cual es tu nombre?")
age = input("Cual es tu edad?")

print(name)
print(age)

print("Me llamo:", name, surname, "Mi edad es:", age, ". Y mi alias es:", alias)

# cambiamos su tipo
name = 35
age = "juanC"

print("Me llamo:", name, surname, "Mi edad es:", age, ". Y mi alias es:", alias)

# Forzamos el tipo
address: str = "Jr Pedregal 357"

address = True
address = 5
address = 2.5

print(type(address))
