
# Sección 2: 

## Parte 2: Ejercicios Prácticos (45 minutos)

      Requerimos **instalar** en nuestras maquinas o entorno 
      
      ### 1. Instalar Python
      
      tener instaldo, si no podemos validar:
      ```sh
      python --version
      ```
      
      ### 2. Crear un entorno virtual (se puedo global pero recomiento crear un entorno personalizado)
      ```sh
      python -m venv env
          source env/bin/activate  # En Linux/Mac
          env\Scripts\activate  # En Windows
      ```
      ### 3. Crear el archivo del proyecto
      Crea un archivo `nombre de nuestro proyecto` ejemp:sr_developer
      
      ### 4. Instalar dependencias (si es necesario)
      debemos intalar la libreria para trabajar con AWS:
      ```sh
          pip install boto3
      ```
      
      ### 5. Ejecutar el script
      Para correr el script, simplemente ejecutá:
      ```sh
      python sr_developer.py

      ```



## 1. Desarrollo en Python:
Crea una función en Python que reciba una lista de números y devuelva el promedio de esos
números.
 
 ```sh
       def calculate_average(numbers):
      if not numbers:
          return 0 
      return sum(numbers) / len(numbers)
  
  grades = [5.5, 5.8, 4.0, 5.0, 9.2]
  average = calculate_average(grades)
  print(f"The average grade is: {average}")
```

Resultado Ejecución:

![image](https://github.com/user-attachments/assets/b5f5faf9-e307-4b74-8dac-5b12881b4fd3)



## 2. Integración con Base de Datos SQL:
Escribe una consulta SQL que devuelva todos los usuarios cuyo correo electrónico termine en
"@gmail.com" de una tabla de usuarios (id, nombre, correo).

 ```sql
      SELECT * FROM users WHERE email LIKE '%@gmail.com';
 ```
Ejemplo práctico:

 ```sql
    CREATE TABLE users (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      email TEXT NOT NULL
    );
    -- insert
    INSERT INTO users VALUES (1,'John' ,'john@gmail.com');
    INSERT INTO users VALUES (2,'maria','maria@yahoo.com' );
    INSERT INTO users VALUES (2,'carlo' ,'carlos@gmail.com');
    
    -- filter data @gmail
    SELECT * FROM users WHERE email LIKE '%@gmail.com';
 ```

![image](https://github.com/user-attachments/assets/2e51a528-7c29-43df-8e9e-10585c0ab8c6)



## 3. AWS Lambda y SQS:
Escribe una función Lambda sencilla en Python que reciba un mensaje de una cola SQS y lo
imprima en la consola.




# Pasos para construir y ejecutar el proyecto en Python

Si querés construir y ejecutar este proyecto de manera local, seguí estos pasos:


