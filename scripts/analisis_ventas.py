import pandas as pd

# Carga de datos con rutas relativas
df = pd.read_csv('datos/ventas_bim.csv')

# Lógica de cálculo de indicadores
ventas_totales = df['Monto_USD'].sum()
servicio_mas_vendido = df['Servicio_BIM'].value_counts().idxmax()

# Guardar resultados
with open('resultados/indicadores.txt', 'w') as f:
    f.write(f"VENTAS TOTALES: USD {ventas_totales}\n")
    f.write(f"SERVICIO LÍDER: {servicio_mas_vendido}\n")

print("Análisis completado. Resultados guardados en /resultados.")
