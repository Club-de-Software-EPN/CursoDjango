# Denuncias

Crear una aplicación que permita realziar denuncias de manera anónima.

Las denuncias contienen la siguiente información:

1. Título
2. Temas (Acoso, Negligencia)
3. Denunciante (Código único)
4. Acusado (Nombre)
5. Mensaje detallado

## Restricciones de seguridad

1. El denunciante debe ser un estudiante activo de la EPN, pero no debemos saber quien es (HASH). Cualquier persona, incluida los admins de la base de datos no conocen 
el texto, pero si pueden llegar a saber cuando dos textos son iguales.
2. Algoritmo Criptográfico, criptar el nombre del Acusado, en algún momento se va a poder desencriptar el nombre del Acusado.
3. LA denuncia no puede ser eliminada, ni modificada ni leida desde la App.

