import os
import sys
import math

# Código hecho para mi buen amigo Rodrigo Aguilera
# Con este código podrás rotar y trasladar átomos sin ningún problema
#
# Hecho por Otilio Enrique Rodríguez López
# Instituto de Física, UASLP.
# San Luis Potosí, México.

print("======================\
      Bienvenido a AtomRoT\
      =======================")

print("")

rot_flag = False
tras_flag = False

flag = True

while flag:
    what_to_do = input("¿Qué deseas realizar: Rotación o Traslación?(" + "\033[1m" + "r" + "\033[0m" + "ot/"\
                       "\033[1m" + "t" + "\033[0m" + "as): ")
    
    if what_to_do.lower() == 'rot' or what_to_do.lower() == 'r'\
        or what_to_do.lower() == 'rotacion' or what_to_do.lower() == 'rotación':
        print("Se realizará una rotación.")
        print("Ingrese los ángulos de rotación en grados.")

        alpha_ = input("Alfa: ")
        beta_ = input("Beta: ")
        gamma_ = input("Gama: ")

        print("Los ángulos de rotación son Alfa:", alpha_,", Beta:", beta_,", Gama: ", gamma_)
        alpha = math.radians(float(alpha_))
        beta = math.radians(float(beta_))
        gamma = math.radians(float(gamma_))
        flag = False
        rot_flag = True

    elif what_to_do.lower() == 'tras' or what_to_do.lower() == 't'\
        or what_to_do.lower() == 'traslacion' or what_to_do.lower() == 'traslación':
        print("Se realizará una traslación")
        print("Ingrese los deltas(\u0394) para realizar la traslación.")
        dx = input("\u0394x: ")
        dy = input("\u0394y: ")
        dz = input("\u0394z: ")
        
        print("Los deltas son \u0394x:", dx,", \u0394y:", dy,", \u0394z: ", dz)
        dx = float(dx)
        dy = float(dy)
        dz = float(dz)

        flag = False
        tras_flag = True

    else:
        print("Respuesta inválida")


# while flag:

#     rot_input = input("¿Deseas realizar una rotación? (sí/no): ")

#     if rot_input.lower() == 'si' or rot_input.lower() == 's'\
#         or rot_input.lower() == 'yes' or rot_input.lower() == 'y':
        
#         print("Ingrese los ángulos de rotación en grados.")
#         alpha_ = input("Alfa: ")
#         beta_ = input("Beta: ")
#         gamma_ = input("Gama: ")
        
#         print("Los ángulos de rotación son Alfa:", alpha_,", Beta:", beta_,", Gama: ", gamma_)
#         alpha = math.radians(float(alpha_))
#         beta = math.radians(float(beta_))
#         gamma = math.radians(float(gamma_))
#         flag = False

#     elif rot_input.lower() == 'no' or rot_input.lower() == 'n':
#         print('¡Ninguna rotación será efectuada!')
#         flag = False
#         rot_flag = False

#     else:
#         print("Respuesta inválida")



# while flag and rot_flag != True:
        
#     tras_input = input("Deseas realizar una traslación? (sí/no): ")

#     if tras_input.lower() == 'si' or tras_input.lower() == 's'\
#         or tras_input.lower() == 'yes' or tras_input.lower() == 'y':
        
#         print("Ingrese los deltas(\u0394) para realizar la traslación.")
#         dx = input("\u0394x: ")
#         dy = input("\u0394y: ")
#         dz = input("\u0394z: ")
        
#         print("Los deltas son \u0394x:", dx,", \u0394y:", dy,", \u0394z: ", dz)
#         dx = float(dx)
#         dy = float(dy)
#         dz = float(dz)

#         flag = False

#     elif rot_input.lower() == 'no' or rot_input.lower() == 'n':

#         print('¡Ninguna traslación será efectuada!')
#         flag = False
#         tras_flag = False

#     else:
#         print("Respuesta inválida")


flag = True

while flag and tras_flag == True:
    fgen_input = input("¿Deseas generar más de un(1) archivo? (sí/no): ")

    if fgen_input.lower() == 'si' or fgen_input.lower() == 's'\
        or fgen_input.lower() == 'yes' or fgen_input.lower() == 'y':
    
        fnumber = input("Ingrese el número de archivos: ")
        
        print("Serán generados ", fnumber, " archivos")
        flag = False
        fnumber = int(fnumber)
        if fnumber > 50:
            confirmation_input = input("¿Está seguro? (sí/no)")
            if confirmation_input.lower() != 'si' or confirmation_input.lower() != 's'\
            or confirmation_input.lower() != 'yes' or confirmation_input.lower() != 'y':
                flag = True
        
    elif fgen_input.lower() == 'no' or fgen_input.lower() == 'n':

        print('Sólo un (1) archivo será generado.')
        fnumber = 1
        flag = False

    else:
        print("Respuesta inválida")

if tras_flag == False and rot_flag == False:
    print("No hay nada que hacer.")
    print("Hasta luego.")
    exit()

#Leyendo archivo .vasp
file = open("POSCAR.vasp", "r")
lines = file.readlines()

if rot_flag:
    print("")
    print("--------------------------------")
    print(" ~ ~ Iniciando Rotación ~ ~ ")
    print("--------------------------------")
    print("")
    #Creando carpeta
    folder = "rot-" +  str(alpha_) + "-" +  str(beta_) + "-" +  str(gamma_)
    os.mkdir(folder)
    #Creando archivo nuevo
    new_file = open(folder + "/POSCAR", "w")
    #Escribiendo las primeras líneas
    new_file.write(lines[0])
    new_file.write(lines[1])

    #Iniciando rotación de los vectores base
    for i in range(3):
        x = float(lines[2 + i].split()[0])
        y = float(lines[2 + i].split()[1])
        z = float(lines[2 + i].split()[2])

        x_rot = x * math.cos(alpha) * math.cos(beta) + y * (math.cos(alpha) * math.sin(beta) * math.sin(gamma) - math.sin(alpha) * math.cos(gamma)) + z *(math.cos(alpha) * math.sin(beta) * math.cos(gamma) + math.sin(alpha) * math.sin(gamma))
        y_rot = x * math.sin(alpha) * math.cos(beta) + y * (math.sin(alpha) * math.sin(beta) * math.sin(gamma) + math.cos(alpha) * math.cos(gamma)) + z *(math.sin(alpha) * math.sin(beta) * math.sin(gamma) - math.cos(alpha) * math.sin(gamma))
        z_rot = -x * math.sin(beta) + y * math.cos(beta) * math.sin(gamma) + z * math.cos(beta) * math.cos(gamma)
        
        x_rot = round(x_rot, 10)
        y_rot = round(y_rot, 10)
        z_rot = round(z_rot, 10)

        new_file.write(f"{x_rot : 20.10f}{y_rot : 20.10f}{z_rot : 20.10f}" + "\n")
    
    new_file.write(lines[5])
    new_file.write(lines[6])
    
    elements = lines[6].split()
    total_cartesian = 0

    for i in range(len(elements)):
        total_cartesian += int(elements[i])
   
    new_file.write(lines[7])

    for i in range(total_cartesian):
        x = float(lines[8 + i].split()[0])
        y = float(lines[8 + i].split()[1])
        z = float(lines[8 + i].split()[2])

        x_rot = x * math.cos(alpha) * math.cos(beta) + y * (math.cos(alpha) * math.sin(beta) * math.sin(gamma) - math.sin(alpha) * math.cos(gamma)) + z *(math.cos(alpha) * math.sin(beta) * math.cos(gamma) + math.sin(alpha) * math.sin(gamma))
        y_rot = x * math.sin(alpha) * math.cos(beta) + y * (math.sin(alpha) * math.sin(beta) * math.sin(gamma) + math.cos(alpha) * math.cos(gamma)) + z *(math.sin(alpha) * math.sin(beta) * math.sin(gamma) - math.cos(alpha) * math.sin(gamma))
        z_rot = -x * math.sin(beta) + y * math.cos(beta) * math.sin(gamma) + z * math.cos(beta) * math.cos(gamma)
        
        x_rot = round(x_rot, 10)
        y_rot = round(y_rot, 10)
        z_rot = round(z_rot, 10)

        if i != (total_cartesian - 1):
            new_file.write(f"{x_rot : 20.10f}{y_rot : 20.10f}{z_rot : 20.10f}" + "\n")
        else:
            new_file.write(f"{x_rot : 20.10f}{y_rot : 20.10f}{z_rot : 20.10f}")

    new_file.close()

elif tras_flag:
    print("")
    print("--------------------------------")
    print(" ~ ~ Iniciando Traslación ~ ~ ")
    print("--------------------------------")
    print("")

    #Creando múltiples archivos
    for n in range(fnumber):
        N = n + 1
        folder = "tras-" +  str(round(N * dx, 2)) + "-" +  str(round(N * dy, 2)) + "-" +  str(round(N * dz, 2))
        os.mkdir(folder)
        new_file = open(folder + "/POSCAR", "w")
        #Escribiendo las primeras líneas
        new_file.write(lines[0])
        new_file.write(lines[1])
        new_file.write(lines[2])
        new_file.write(lines[3])
        new_file.write(lines[4])
        new_file.write(lines[5])
        new_file.write(lines[6])

        elements = lines[6].split()
        total_cartesian = 0

        for i in range(len(elements)):
            total_cartesian += int(elements[i])
    
        new_file.write(lines[7])

        for i in range(total_cartesian):
            x = float(lines[8 + i].split()[0])
            y = float(lines[8 + i].split()[1])
            z = float(lines[8 + i].split()[2])

            x_tras = round(x + N * dx, 10)
            y_tras = round(y + N * dy, 10)
            z_tras = round(z + N * dz, 10)

            if i != (total_cartesian - 1):
                new_file.write(f"{x_tras : 20.10f}{y_tras : 20.10f}{z_tras : 20.10f}" + "\n")
            else:
                new_file.write(f"{x_tras : 20.10f}{y_tras : 20.10f}{z_tras : 20.10f}")

        new_file.close()

print("--------------------------------")
print(" ~ ~ Terminado ~ ~ ")
print("--------------------------------")