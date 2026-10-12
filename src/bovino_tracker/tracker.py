# tracker.py

def calcular_metricas(peso_ingreso: float, peso_actual: float, dias: int):
    # 1. Calcula la ganancia neta (peso_actual - peso_ingreso)
    ganancia_peso=peso_actual - peso_ingreso
    # 2. Calcula la GDP (ganancia neta / dias)
    gdp = ganancia_peso / dias
    # 3. Calcula el requerimiento de Materia Seca (2.8% del peso actual: peso_actual * 0.028)
    materia_seca_requerida = peso_actual * 0.028
    # 4. Retorna estos 3 valores
    return ganancia_peso, gdp, materia_seca_requerida


def evaluar_desempeno(gdp: float) -> str:
    # Regla:
    # Si gdp >= 0.90 -> retorna "ÓPTIMO (En meta de ceba)"
    if gdp >= 0.90:
        print('optimo') 
    # Si no -> retorna "ALERTA (Bajo rendimiento - revisar ración)"
    else:
        print('maute bajo de peso')

# --- DATOS DE PRUEBA ---
arete = "CO-042"
dias = 35
ingreso = 340.5
actual = 385.0

# LLAMA A TUS FUNCIONES AQUÍ E IMPRIME EL REPORTE
maute1= calcular_metricas(ingreso,actual,dias)
print(maute1)
gdp=dias
alerta=evaluar_desempeno(gdp)

# Debe imprimir:
print(f'Arete: {arete}')
# Arete: CO-042
# Ganancia neta: XX.XX kg
# GDP: X.XX kg/día
# Requerimiento MS: XX.XX kg/día
# Estado: ÓPTIMO / ALERTA