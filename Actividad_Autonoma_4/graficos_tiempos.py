import matplotlib.pyplot as plt


tiempo_original = 9.690     
tiempo_optimizado = 0.101    

# Gráfico 1: Comparación de Tiempos
plt.figure()
plt.bar(["Original", "Optimizado"], [tiempo_original, tiempo_optimizado])
plt.title("Comparación de tiempos de ejecución")
plt.ylabel("Tiempo (segundos)")
plt.xlabel("Versión del código")
plt.savefig("comparacion_tiempos.png")
plt.show()


# Gráfico 2: Distribución simple de tiempos 
plt.figure()
plt.hist([tiempo_original, tiempo_optimizado], bins=5)
plt.title("Distribución de tiempos")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Frecuencia")
plt.savefig("distribucion_tiempos.png")
plt.show()
