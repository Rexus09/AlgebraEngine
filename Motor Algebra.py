import os
import numpy as np
import scipy.linalg
from scipy.linalg import lu


def Main():
    # Menú de selección
    print("Bienvenido al motor de álgebra")
    print("==============================")
    print("Opciones")
    print("1 - Resolver un sistema")
    print("2 - Calcular un determinante")
    print("3 - Hallar el polinomio característico de una AL")
    print("4 - Sacar los autovalores de una AL")
    print("5 - Operaciones de matrices")
    eleccion = 2
    #eleccion = int(input("->"))
    if eleccion == 1:  # 1 - Resolver un sistema
        resolverSistema()
    elif eleccion == 2:  # 2 - Calcular un determinante
        calcularDet()
    elif eleccion == 3:  # 3 - Hallar el polinomio característico
        pass
    elif eleccion == 4:  # 4 - Sacar los autovalores
        pass
    else:
        print("Opción equivocada, elige un número correcto.")
        os.system("cls")
        Main()

def imprimir_matriz(mat):
    for fila in mat:
        print("|", end = " ")
        print(" ".join(f"{elem:8.2f}" for elem in fila), end = "")
        print("\t|")
    

def solve(A, m, n):
    """
    Resuelve un sistema de ecuaciones Ax = b usando la factorización LU.

    Parámetros:
    A -- Matriz ampliada (m x (n + 1))
    m -- Número de ecuaciones
    n -- Número de incógnitas

    Retorna:
    x -- Vector solución (n) o None si el sistema no tiene solución
    """
    # Separar A en matriz de coeficientes y vector de términos independientes
    coeff_matrix = A[:, :n]
    b = A[:, n]

    # Construir la matriz aumentada
    A_augmented = np.hstack([coeff_matrix, b.reshape(-1, 1)])

    # Calcular el rango de la matriz de coeficientes
    rank_A = np.linalg.matrix_rank(coeff_matrix)
    # Calcular el rango de la matriz aumentada
    rank_A_augmented = np.linalg.matrix_rank(A_augmented)

    # Verificar la consistencia del sistema
    if rank_A != rank_A_augmented:
        print("El sistema no tiene solución.")
        return None
    elif rank_A < n:
        print("El sistema es compatible indeterminado (infinitas soluciones).")
        # Encontrar una solución particular cuando k = 0
        # Resolviendo el sistema usando mínimos cuadrados
        # Aquí, x puede ser una solución particular con k = 0
        # Resolviendo el sistema usando la descomposición SVD para encontrar una solución particular
        U, s, Vt = np.linalg.svd(coeff_matrix)
        c = np.dot(U.T, b)
        x = np.dot(Vt.T, np.dot(np.diag(1 / s), c))
        # Si x contiene NaN o inf, debe ser ajustado, aquí simplemente retornamos la solución particular
        print("\n\nUna solución particular con lambda = 0 es -> ", x)
        return x

    # Factorización LU
    P, L, U = scipy.linalg.lu(coeff_matrix)
    
    # Resolver Ly = Pb para y
    Pb = np.dot(P, b)
    y = scipy.linalg.solve_triangular(L, Pb, lower=True)
    
    # Resolver Ux = y para x
    x = scipy.linalg.solve_triangular(U, y)
    print("Solución:", x)
    return x  

def resolverSistema():
    os.system("cls")
    print("RESOLVER SISTEMA")
    print("================")
    """
    try:
        incognitas = int(input("Numero de incognitas"))
        ecuaciones = int(input("Numero de ecuaciones"))
    except:
        print("Pon un numero, no pongas letras ni espacios")
        incognitas = 0
        ecuaciones = 0        
    """
    incognitas = 3
    ecuaciones = 3 
    if incognitas == 0 or ecuaciones == 0:
        print("Lo siento, pero no me vale un 0.")
    else:
        print("Quieres que use python o C para el paso de resolucion?\n Para resoluciones más complejas C puede ser mas rapido")
        print("1 - Python")
        print("2 - C")
        solver = int(input("->"))
        print("Perfecto, dame un momento \n")
        if solver == 1: #Uso python
            mat = np.zeros((ecuaciones, incognitas + 1))
            """
            for i in range(ecuaciones):
                for j in range(incognitas + 1):
                    imprimir_matriz(mat)
                    if j < incognitas:
                        print(f"Introduce el coeficiente para la posición ({i+1},{j+1}): ", end="")
                    else:
                        print(f"Introduce el término independiente para la ecuación {i+1}: ", end="")
                    valor = float(input())
                    mat[i][j] = valor
                    os.system("cls")  # Limpiar la pantalla después de cada entrada
                    print("\n")
            #SCD
            mat = np.array([[1, 1, -1, 5], 
                    [2, 3, 2, 14], 
                    [-3, -1, 2, 3]], dtype=float)
            """
            #SCI
            mat = np.array([[1, 1, 1, 3], 
                    [2, 1, -1, 4], 
                    [5, 2, -4, 9]], dtype=float)
            print("Matriz final:")
            imprimir_matriz(mat)
            solve(mat, ecuaciones, incognitas)
        else: #Uso C
            print("Usaré C para resolver, un segundo ")
            os.system("")

        print("Quieres algo más?\n1 - Si \n2 - No\n")
        if input("->") == "1":
            Main()
        else:
            pass  

def calcularDet():
    os.system("cls")
    print("CALCULAR DETERMINANTES")
    print("======================")
    """
    try:
        tam = int(input("Tamagno de la matriz"))
    except:
        print("Pon un numero, no pongas letras ni espacios")
        exit()
    """
    tam = 3 
    if tam == 0 :
        print("Tu determinante vale 0, espabilao")
    else:
        print("Quieres que use python o C para el paso de resolucion?\n Para resoluciones más complejas C puede ser mas rapido")
        print("1 - Python")
        print("2 - C")
        solver = int(input("->"))
        print("Perfecto, dame un momento \n")
        if solver == 1: #Uso python
            mat = np.zeros((tam, tam))
            for i in range(tam):
                for j in range(tam):
                    imprimir_matriz(mat)
                    print(f"Introduce el coeficiente para la posición ({i},{j}): ", end="")
                    mat[i][j] = float(input())
                    os.system("cls")  # Limpiar la pantalla después de cada entrada
                    print("\n")

            """mat = np.array([[1, 1, 1], 
                    [2, 1, -1], 
                    [5, 2, -4]], dtype=float)
            """
            print("Matriz final:")
            imprimir_matriz(mat)
            P, L, U = lu(mat)
            print(f"El determinante da {np.prod(np.diag(U))}")
        else: #Uso C
            print("Usaré C para resolver, un segundo ")
            #os.system("")

        print("Quieres algo más?\n1 - Si \n2 - No\n")
        if input("->") == "1":
            Main()
        else:
            pass  

# Ejecutar el programa principal
if __name__ == "__main__":
    Main()
