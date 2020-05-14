while True:
    try:
        num = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Error, se esperaba un numero")
        resp = input("Desea seguir ingresando? s/n: ")
        if resp.lower() != "s":
            raise
        print("Vuelva a intentarlo")