#include <stdio.h>
#include <stdlib.h>

// Función para realizar la factorización LU
void lu_decomposition(double* A, int n, double* L, double* U) {
    int i, j, k;
    for (i = 0; i < n; i++) {
        // U matrix
        for (j = i; j < n; j++) {
            U[i*n + j] = A[i*n + j];
            for (k = 0; k < i; k++) {
                U[i*n + j] -= L[i*n + k] * U[k*n + j];
            }
        }
        // L matrix
        for (j = i; j < n; j++) {
            if (i == j) {
                L[i*n + i] = 1;
            } else {
                L[j*n + i] = A[j*n + i];
                for (k = 0; k < i; k++) {
                    L[j*n + i] -= L[j*n + k] * U[k*n + i];
                }
                L[j*n + i] /= U[i*n + i];
            }
        }
    }
}

// Función para resolver el sistema Ly = b
void forward_substitution(double* L, double* b, double* y, int n) {
    int i, j;
    for (i = 0; i < n; i++) {
        y[i] = b[i];
        for (j = 0; j < i; j++) {
            y[i] -= L[i*n + j] * y[j];
        }
    }
}

// Función para resolver el sistema Ux = y
void backward_substitution(double* U, double* y, double* x, int n) {
    int i, j;
    for (i = n - 1; i >= 0; i--) {
        x[i] = y[i];
        for (j = i + 1; j < n; j++) {
            x[i] -= U[i*n + j] * x[j];
        }
        x[i] /= U[i*n + i];
    }
}

// Función principal para resolver el sistema Ax = b
void solve(double* A, double* b, double* x, int n) {
    double* L = (double*)malloc(n * n * sizeof(double));
    double* U = (double*)malloc(n * n * sizeof(double));
    double* y = (double*)malloc(n * sizeof(double));

    if (L == NULL || U == NULL || y == NULL) {
        fprintf(stderr, "Error al asignar memoria.\n");
        exit(1);
    }

    // Inicializar matrices L y U
    for (int i = 0; i < n * n; i++) {
        L[i] = 0;
        U[i] = 0;
    }

    // Realizar la factorización LU
    lu_decomposition(A, n, L, U);

    // Resolver Ly = b
    forward_substitution(L, b, y, n);

    // Resolver Ux = y
    backward_substitution(U, y, x, n);

    // Liberar memoria
    free(L);
    free(U);
    free(y);
}

int main() {
    int ecuaciones, incognitas;

    // Leer el número de ecuaciones y incógnitas
    printf("Introduce el número de ecuaciones: ");
    scanf("%d", &ecuaciones);
    printf("Introduce el número de incógnitas: ");
    scanf("%d", &incognitas);

    // Crear la matriz ampliada (A con b)
    double* A = (double*)malloc(ecuaciones * incognitas * sizeof(double));
    double* b = (double*)malloc(ecuaciones * sizeof(double));
    double* x = (double*)malloc(incognitas * sizeof(double));

    if (A == NULL || b == NULL || x == NULL) {
        fprintf(stderr, "Error al asignar memoria.\n");
        return 1;
    }

    // Leer los coeficientes y términos independientes
    for (int i = 0; i < ecuaciones; i++) {
        for (int j = 0; j < incognitas; j++) {
            printf("Introduce el coeficiente para la posición (%d,%d): ", i + 1, j + 1);
            scanf("%lf", &A[i * incognitas + j]);
        }
        printf("Introduce el término independiente para la ecuación %d: ", i + 1);
        scanf("%lf", &b[i]);
    }

    // Resolver el sistema
    solve(A, b, x, incognitas);

    // Imprimir la solución
    printf("Solución:\n");
    for (int i = 0; i < incognitas; i++) {
        printf("x%d = %f\n", i + 1, x[i]);
    }

    // Liberar memoria
    free(A);
    free(b);
    free(x);

    system("pause");
    return 0;
}


