
# Sección 3: Análisis de Código (30 minutos)

## Parte 2: Ejercicios Prácticos (45 minutos)

Codigo Original:
 ```python
          import boto3
          def upload_file_to_s3(filename, bucket):
          s3 = boto3.client('s3')
          s3.upload_file(filename, bucket, filename)

 ```


Podemos aplicar los principios *SOLID* para separar responsabilidades y hacer el codigo reutilizable, tambien tener un manejo adecuado como trabajamos con archivos y esto puede hacerse asincrono es recomendado implementar un manejo de errores para evitar desbordes en nuestra aplicación. y tambien para teber un manejo adecuado de nuestro BAM de operaciones.
 ```python
        import boto3
        import logging
        from botocore.exceptions import BotoCoreError, ClientError
        
        def get_s3_client():
            return boto3.client('s3')
        
        def upload_file_to_s3(filename, bucket, object_name=None, s3_client=None):
            if s3_client is None:
                s3_client = get_s3_client()
            
            if object_name is None:
                object_name = filename
            
            try:
                s3_client.upload_file(filename, bucket, object_name)
                logging.info(f"Archivo {filename} subido exitosamente a {bucket}/{object_name}")
                return True
            except (BotoCoreError, ClientError) as e:
                logging.error(f"Error al subir {filename} a {bucket}: {e}")
                return False

 ```python
