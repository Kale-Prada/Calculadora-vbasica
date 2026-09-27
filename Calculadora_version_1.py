# 1. Mensaje de bienvenida
welcome_message = "\n####### Bienvenido a la calculadora ########\n"
print(welcome_message)


# 2. DEFINICIÓN DE FUNCIONES

def intro_nums():
    """
    Pide que el usuario introduzca dos números por teclado y los devuelve convertidos a decimales.
    """
    # Usamos float() para que el usuario pueda meter números enteros o con decimales
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Devolvemos los números para que la otra función los reciba
    return num1, num2


def intro_operation() -> str:
    """
    Pide al usuario que introduzca una operación matemática por teclado y 
    devuelve la seleccionada
    """
    print("\n---ELIGE UNA DE LAS SIGUIENTES OPERACIONES---")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir(/)")

    opcion = input("\nElige el número de la operación, ESCRIBE LA OPCIÓN DEL 1 AL 4: \n")
    return opcion



def calculate_operation(num1: float, num2: float, op: str):
    """
    Calcula la operación elegida proveniente de la función "intro_operation"
    """

    if  op == "1":
        print(f"✅ Resultado de la suma: {num1} + {num2} = {num1 + num2}")
        
    elif op == "2":
        print(f"✅ Resultado de la resta: {num1} - {num2} = {num1 - num2}")

    elif op == "3":
         print(f"✅ Resultado de la multiplicación: {num1} * {num2} = {num1 * num2}")

    elif op == "4":
         print(f"✅ Resultado de la división: {num1} / {num2} = {num1 / num2}")
    else: 
        print("⚠️ Opción no válida. No se pudo realizar el cálculo.")


    

def ejecutar_menu():
    """
    Se encarga de llevar el control de la calculadora. 
    Pide al usuario si quiere continuar calculando o de lo contrario SALIR de la calculadora.
    """
    while True:
        select_option = input('\nPara empezar a usar la calculadora escribe la palabra "INICIAR", de lo contrario "SALIR" y luego pulsa la tecla INTRO: \n').upper()
        
        if select_option == "INICIAR":
            print("\n▶️ Iniciando la calculadora...\n")
            
            # Guardamos los dos números que devuelve la función intro_nums
            n1, n2 = intro_nums()
            print(f"\nNúmero 1: {n1} | Número 2: {n2}\n")

            # Elegimos la operación a realizar
            operacion = intro_operation()
            print(f"\nLa operación elegida es: {operacion}\n")

            #Calculamos la operación 
            calculate_operation(n1, n2, operacion) 
            
        elif select_option == "SALIR":
            print("\n👋 Saliendo del programa. ¡Espero volver a verte pronto!\n")
            break  
            
        else:
            print("\n⚠️ Opción no válida. Por favor, intentalo de nuevo.\n")


# 3. EJECUCIÓN DEL PROGRAMA 
ejecutar_menu()