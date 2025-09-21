"""
Lista de python - Participación
"""
"""
Requisitos:
- Crear dos listas vacías
- Agregar los datos de nombre, apellido paterno, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edades de ambas listas
- Sumar las listas y mostrar el resultado en la terminar
- Mostrar de forma inversa la suma de ambas listas
- Actualizar la nueva lista eliminando la edad de la primera y el apellido del segundo
(Utilizar cualquiera de los métodos de eliminación)
- Actualizar la profesión del segundo usuario
"""
usuario_1 = []

usuario_1.append("Rosaura")
usuario_1.append("Soto")
usuario_1.append(30)
usuario_1.append("Contadora")

usuario_2 = []

usuario_2.append("Raquel")
usuario_2.append("Gomez")
usuario_2.append(23)
usuario_2.append("Ingeniera")

suma_edades = usuario_1[2] + usuario_2[2]
print("Suma de edades: {}".format(suma_edades))

suma_listas = usuario_1 + usuario_2
print("Lista final: {}".format(suma_listas))

suma_listas.reverse()
print("Lista final: {}".format(suma_listas))

usuario_1.remove(30)
print("Mi lisa 1 actualizada: {}".format(usuario_1))

usuario_2.remove("Gomez")
print("Mi lisa 2 actualizada: {}".format(usuario_2))

usuario_2[2] = "Abogada"
print("Mi lisa 2 actualizada: {}".format(usuario_2))
"""
Actualización de valores por índice en la lista
usuario_2[2] = 35
usuario_1[0] = "Mario" 
print(usuario_2)
print(usuario_1)
"""

"""
Hora de entrega máxima: 6:00 pm
Correo: docente.cerseu.unmsm@gmail.com
Asunto: Participación a práctica 02
Adjuntar su archivo .py con su solución
"""


