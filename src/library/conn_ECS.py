import boto3

def conn_ecs(region):
    """
        Crea y retorna un cliente ECS de AWS usando boto3.

        Parámetros:
            region (str): Región de AWS donde se creará el cliente ECS.

        Returns:
            boto3.client: Cliente ECS configurado para la región especificada.

        Raises:
            Exception: Si ocurre un error durante la conexión con ECS.

        Ejemplo:
            ecs_client = conn_ecs("us-east-1")
    """
    try:
        return boto3.client('ecs',region_name= region)
    except Exception as e:
        raise Exception(f"Error al conectar con ECS: {e}")
    
  

