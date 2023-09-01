import pandas as pd
import matplotlib.pyplot as plt


# Cargar los datos desde el archivo CSV con delimitador ';'
datos = pd.read_csv('archivo_2.csv', encoding='latin-1', delimiter=';')

# Mostrar las columnas del DataFrame
#print(datos.columns)

# 1 Calcular el promedio de ingresos por género
promedio_ingresos_por_genero = datos.groupby('genero')['ingresos'].mean()

# imprime el resultado del cálculo del promedio de ingresos por género
print(promedio_ingresos_por_genero)

# 1.1 Generar el gráfico de barras
promedio_ingresos_por_genero.plot(kind='bar')
plt.xlabel('Género')
plt.ylabel('Promedio de Ingresos')
plt.title('Promedio de Ingresos por Género')
plt.show()

# 2 distribución de niveles de educación en porcentajes
distribucion_educacion = datos['nivel_educativo'].value_counts(normalize=True) * 100

# imprimirá los niveles de educación en porcentajes que calculaste
print(distribucion_educacion)

# 2.2 Generar el gráfico de pastel
plt.figure(figsize=(8, 6))
distribucion_educacion.plot(kind='pie', autopct='%.1f%%')
plt.title('Distribución de Niveles de Educación')
plt.ylabel('')
plt.show()

# Calcular la distribución de niveles de educación en porcentajes
distribucion_educacion_por_estado = datos.groupby(['estado_civil', 'nivel_educativo']).size().unstack()
distribucion_educacion_por_estado = distribucion_educacion_por_estado.apply(lambda x: x / x.sum(), axis=1) * 100

print(distribucion_educacion_por_estado)

# Generar el gráfico de barras
distribucion_educacion_por_estado.plot(kind='bar', stacked=True)
plt.xlabel('Estado Civil')
plt.ylabel('Porcentaje')
plt.title('Distribución de Niveles de Educación por Estado Civil')
plt.legend(title='Nivel Educativo')
plt.show()

# Crear el diagrama de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(datos['edad'], datos['nivel_educativo'], alpha=0.5)
plt.xlabel('Edad')
plt.ylabel('Nivel Educativo')
plt.title('Relación entre Edad y Nivel de Educación')
plt.show()

