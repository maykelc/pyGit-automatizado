import subprocess
from time import sleep
import sys
import os

# funcion para ejecutar comandos de la terminal
def run_command(command):
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

# funcion que verifica si esta instalado Git
def check_git_installed():
    try:
        subprocess.run(["git", "--version"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Git está instalado.")
        return True
    except subprocess.CalledProcessError:
        print("Git no está instalado.")
        return False

# funcion que instala Git segun Sistema Operativo
def install_git():
    if sys.platform.startswith("win32"):
        print("Instalando Git en Windows...")
        run_command("winget install --id Git.Git -e --source winget")
    elif sys.platform.startswith("darwin"):
        print("Instalando Git en macOS...")
        run_command(
            "/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        run_command("brew install git")
    elif sys.platform.startswith("linux"):
        print("Instalando Git en Linux...")
        distro = subprocess.run(
            ["lsb_release", "-is"], capture_output=True, text=True).stdout.strip().lower()
        if distro in ["ubuntu", "debian"]:
            run_command("sudo apt update && sudo apt install git -y")
        elif distro in ["fedora"]:
            run_command("sudo dnf install git -y")
        elif distro in ["centos"]:
            run_command("sudo yum install git -y")
        else:
            print(f"Distribución no soportada: {distro}")
            sys.exit(1)
    else:
        print(f"Sistema operativo no soportado: {sys.platform}")
        print("No se pudo instalar Git. Por favor, instálalo manualmente.")
        sys.exit(1)


print("Este script automatiza varias tareas comunes relacionadas con Git, facilitando el proceso de instalacion, configuración y gestión de repositorios.")
print("SI este script no te funciona, considera utilizar Git de la manera habitual\n\n")





# Menu Soporte Git
while True:
    print("\n**************************************************************************")
    print("**                                                                      **")
    print("**\t\tBienvenido al programa de gestión de proyectos.\t\t**")
    print("**                                                                      **")
    print("**************************************************************************\n")
    print("==========================================================")
    print("==                                                      ==")
    print("==\t\t¿Qué deseas realizar?\t\t\t==")
    print("==                                                      ==")
    print("==\t1. Ver Si Esta Instalado Git\t\t\t==")
    print("==\t2. Instalar Git \t\t\t\t==")
    print("==\t3. Configuracion Global de tu Cuenta\t\t==")
    print("==\t4. Subir proyecto a Git\t\t\t\t==")
    print("==\t5. Salir\t\t\t\t\t==")
    print("==                                                      ==")
    print("==========================================================")

    opciones = input("\nSelecciona una opción (1-5): ")

    if opciones == "1":
        check_git_installed()
    elif opciones == "2":
        print("Instalando Git")
        install_git()
        print("Git instalado")
    elif opciones == "3":
        print("*********************************************************")
        print("**                                                     **")
        print("**             CONFIGURACION GLOBAL DE GIT             **")
        print("**                                                     **")
        print("*********************************************************\n")
        nombre = input("Introduzca Nombre del Usuario de Git: ")
        correo = input("Introduzca Correo del Usuario de Git: ")
        run_command(f'git config --global user.name {nombre}')
        sleep(2)
        run_command(f'git config --global user.email {correo}')
        print(f"Nombre de Usuario: {nombre}")
        print(f"Correo del Usuario: {correo}\n")
        
        list = input("Desea ver la configuracion global de git? (y/n): ")
        if list.lower() == "y":
            print("\nMostrar configuracion global")
            run_command("git config --global --list")
            print( "comando  git config --global --list ejecutado\n" )
    elif opciones == "4":
        # Solicita la información al usuario
        print("\n--------------------------------------")
        print("--                                  --")
        print("--  CONFIGURACIONES BASICAS DE GIT  --")
        print("--                                  --")
        print("--------------------------------------")
        print("\nPara subir un proyecto a Git-Hub debes configurar la informacion, como el commit, la rama, la url del repositorio y el nombre del remoto. esto se solicitara a continuacion... \n")
        commit_message = input('Introduce el mensaje del commit  ')
        branch_name = input("Introduce el nombre de la rama: ")
        repo_url = input("Introduce el URL del repositorio: ")
        remote_name = input("Introduce el nombre del remoto (default 'origin'): ")
        if not remote_name:
            remote_name = "origin"
        print("\n...........................................")
        print("...                                     ...")
        print("...   MENU Para Subir Proyecto a Git    ...")
        print("...                                     ...")
        print("...........................................")
            # Menú para las acciones de Git
        while True:
            print("\nConsidera tener el archivo .gitignore para ignorar o no subir los archivos sensibles, como contraseñas, token de paginas, base de datos, etc\n")
            print("\n¿Qué acción deseas realizar?\n")
            print("***************************************************************************")
            print("***                                                                     ***")
            print("***\t\t   VER O MODIFICAR CONFIGURACION BASICA   \t\t***")
            print("***                                                                     ***")
            print("***\t1. Ver URL del Git   \t\t\t\t\t\t***")
            print("***\t2. Ver Nombre del Commit   \t\t\t\t\t***")
            print("***\t3. Ver Nombre de la Rama   \t\t\t\t\t***")
            print("***\t4. Ver Todo   \t\t\t\t\t\t\t***")
            print("***                                                                     ***")
            print("***                                                                     ***")
            print("***\t\t SUBIR PROYECTO MANUAL A GIT \t\t\t\t***")
            print("***                                                                     ***")
            print("***\t5. Iniciar Git  \t\t\t\t\t\t***")
            print("***\t6. Ver Git Status   \t\t\t\t\t\t***")
            print("***\t7. Agregar todo o parcial a Git   \t\t\t\t***")
            print("***\t8. Crear Commit   \t\t\t\t\t\t***")
            print("***\t9. Crear y cambiar a la Rama   \t\t\t\t\t***")
            print("***\t10. Agregar el repositorio a Git Remote Add origin   \t\t***")
            print("***\t11. Subir proyecto a Git (Hacer Git Push)   \t\t\t***")
            print("***                                                                     ***")
            print("***                                                                     ***")
            print("***\t\t SUBIR PROYECTO AUTOMATICAMENTE A GIT \t\t\t***")
            print("***                                                                     ***")
            print("***\t12. Subir todo Automatizado   \t\t\t\t\t***")
            print("***                                                                     ***")
            print("***\t\t\tSalir\t\t\t\t\t\t***")
            print("***\t13. Salir   \t\t\t\t\t\t\t***")
            print("***                                                                     ***")
            print("***************************************************************************\n")

            option = input("Selecciona una opción (1-13): ")

            if option == "1":
                print(repo_url)
                print("¿Está bien escrito?\n")
                result = input("Escribe 'y' para Sí o 'n' para No: ")
                if result.lower() == "n":
                    repo_url = input("Introduce el URL del repositorio: ")
                    sleep(2)
                    print(f"La nueva URL del repositorio es: {repo_url}\n")
            elif option == "2":
                print(commit_message)
                print("¿Está bien escrito?\n")
                result = input("Escribe 'y' para Sí o 'n' para No: ")
                if result.lower() == "n":
                    commit_message = input("Introduce el mensaje del commit: ")
                    sleep(2)
                    print(f"El nuevo commit es: {commit_message}\n" )
            elif option == "3":
                print(branch_name)
                print("¿Está bien escrito?\n")
                result = input("Escribe 'y' para Sí o 'n' para No: ")
                if result.lower() == "n":
                    branch_name = input("Introduce el nombre de la rama: ")
                    sleep(2)
                    print(f"El nombre de la rama es: {branch_name}")
            elif option == "4":
                print("\nConfiguración Para Subir a Git\n")
                print("----------------------------------------------------------------------")
                print("---                                                                ---")
                print(f"---\tEl Nombre del commit es: {commit_message}\t\t\t---" )
                print(f"---\tEl Nombre de la rama es: {branch_name}\t\t\t\t---")
                print(f"---\tLa URL del repositorio Git es: {repo_url}\t---")
                print("---                                                                ---")
                print("----------------------------------------------------------------------\n")
            elif option == "5":
                run_command("git init")
                print("Git Iniciado\n")
            elif option == "6":
                run_command("git status")
                sleep(3)
            elif option == "7":
                print("Escribe 'a' si deseas agregar todo o 'b' si deseas agregar solo un archivo específico: \n")
                dime = input('"a" o "b"')
                if dime.lower() == "b":
                    print("Escribe el nombre del archivo que deseas agregar:\n")
                    archivo = input()
                    run_command("git add " + archivo)
                    sleep(3)
                    print("Archivo agregado\n")
                elif dime.lower() == "a":
                    run_command("git add .")
                    sleep(5)
                    print("Todos los archivos agregados\n")
            elif option == "8":
                run_command(f'git commit -m "{commit_message}"')
                sleep(5)
                print("Commit realizado\n")
            elif option == "9":
                run_command(f"git branch -M {branch_name}")
                sleep(2)
                print("Branch creado y cambiado\n")
            elif option == "10":
                run_command("git remote add origin " + repo_url)
                sleep(2)
                print("Agregado al repositorio remoto\n")
            elif option == "11":
                run_command(f"git push -u {remote_name} {branch_name}")
                print("Subido a Git, ¡Felicidades!\n")
            elif option == "12":
                print(f"Este comando sube el proyecto al git {repo_url} de forma automática. Considere tener configurado su archivo .gitignore con los nombres de carpeta u archivo que no subirá a Git. \n Este comando sube todo lo que hay en el proyecto")
                run_command("git init")
                sleep(2)
                run_command("git add .")
                sleep(5)
                run_command(f'git commit -m "{commit_message}"')
                sleep(5)
                run_command(f"git branch -M {branch_name}")
                sleep(5)
                run_command("git remote add origin " + repo_url)
                sleep(2)
                run_command(f"git push -u {remote_name} {branch_name}")
                sleep(3)
                print(f"\nProyecto Subido, ¡Felicidades! Visite {repo_url} para confirmar.\n")
            elif option == "13":
                    break
            else:
                print("\nOpción no válida, por favor intenta de nuevo.\n")
        print("\nOperaciones para subri proyecto a Git completadas.\n")    
    elif opciones == "5":
        break
    else:
        print("\nOpción no válida, por favor intenta de nuevo.\n")
print("\nOperaciones de Git completadas.")
