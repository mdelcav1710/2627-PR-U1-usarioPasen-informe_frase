def preparar_texto(frase: str) -> str:
    """
    Elimina los espacios de los extremos y convierte el texto a minúsculas. Devuelve el texto preparado.
    :param frase_arreglada: Convierte una frase a unos parametros concretos.
    :return: Devuelve un str con la frase preparada.
    """    
    frase_arreglada: str = frase.strip().lower()
    return frase_arreglada

def analizar_texto(frase_arreglada: str) -> tuple[int, int, int]:
    """
    Recibe el texto preparado y devuelve una tupla con tres datos: número de caracteres —incluidos los espacios interiores—, número de palabras y si contiene la palabra completa "python".
    :param caracter: Devuelve el número de caracteres de la frase.
    :param palabras: Devuelve el número de palabras de la frase.
    :param python: Devuelve un 0 o un 1 si tiene o no la palabra python en ella.
    :param lista_palabras: Separa las palabras de sus espacios.
    :return: Decuelve 3 int que definen las proporciones de una frase y encuentra una palabra concreta dentro de ella.
    """
    lista_palabras = frase_arreglada.split()
    caracter: int = len(frase_arreglada)
    palabras: int = len(lista_palabras)
    python: int = (1 if "python" in lista_palabras else 0)

    return (caracter,palabras,python)


def main():
    """
    Función principal del programa
    """
    #Entrada
    frase: str = str(input("Dime una frase para analizar: "))
    
    #Proceso
    frase_arreglada: str = preparar_texto(frase)
    solucion: tuple[int, int, int] = analizar_texto(frase_arreglada)
    
    #Salida
    print(f"Texto: {frase_arreglada}")
    print(f"Caracteres: {solucion[0]}.")
    print(f"Palabras: {solucion[1]}.")
    if solucion[2] == 1:
        print("Contiene la palabra python: Sí.")
    else:
        print("Contiene la palabra python: No.")

if __name__ == "__main__":
    main()