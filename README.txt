# Proyecto: Calculadora en Python

Actualmente, la calculadora solo tiene implementada la operación de **Potencia**.

## Tarea para el colaborador
Agregar la operación **Raíz Cuadrada** en la clase `Calculadora` dentro de `clases/avanzadas.py`.

### Instrucciones:

1. Crear un nuevo método en la clase `Calculadora` llamado `raiz_cuadrada`.
   - Este método debe pedir un número al usuario.
   - Si el número es negativo, debe mostrar un mensaje de error.
   - Si el número es positivo o cero, debe calcular la raíz cuadrada y mostrar el resultado.
   - Se recomienda usar la función `math.sqrt()`.

2. Modificar el archivo `main.py` para:
   - Agregar la opción **2. Raíz Cuadrada** en el menú.
   - Llamar al método `raiz_cuadrada` cuando se seleccione esa opción.

3. Probar la calculadora:
   - Ejecutar el programa con `python main.py`.
   - Verificar que la opción de raíz cuadrada funciona correctamente.
   - Confirmar que la opción de potencia sigue funcionando.

4. Hacer commit y push de los cambios:
## Objetivo final
La calculadora debe permitir al usuario elegir entre:
- Potencia
- Raíz Cuadrada
- Salir