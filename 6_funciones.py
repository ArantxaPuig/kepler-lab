def analizar_ventas(ventas):
    """
    Analiza una lista de ventas y devuelve estadísticas.
    
    Args:
        ventas (list): Lista de valores de ventas
    
    Returns:
        dict: Diccionario con estadísticas
    """
    total = sum(ventas)
    promedio = total / len(ventas)
    maximo = max(ventas)
    minimo = min(ventas)
    
    return {
        'total': total,
        'promedio': promedio,
        'maximo': maximo,
        'minimo': minimo
    }

# Usar la función
ventas_mes = [1500, 2000, 1800, 2200, 1900]
estadisticas = analizar_ventas(ventas_mes)

print(f"Total: {estadisticas['total']}")
print(f"Promedio: {estadisticas['promedio']}")
print(f"Máximo: {estadisticas['maximo']}")
print(f"Mínimo: {estadisticas['minimo']}")
