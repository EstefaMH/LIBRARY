import sys

def list_ecs_clusters(ecs_client):

    try:
        print("Listar clusters de ECS\n")  
        clusters = ecs_client.list_clusters()
        print("Clusters:", clusters)
        
        cluster_arns = clusters.get('clusterArns', [])
        print("clusterArns:", cluster_arns)
        if not cluster_arns:
            print("No se encontraron clusters de ECS.")
            return [] 

        print(f"Se encontraron {len(cluster_arns)} clusters. Detalle:")
        for i in range(0, len(cluster_arns), 1):
            batch_arns = cluster_arns[i:i + 1]
            
            detail_response = ecs_client.describe_clusters(
                clusters=batch_arns
            )

            
            for cluster in detail_response.get('clusters', []):
                arn = cluster.get('clusterArn')
                name = cluster.get('clusterName')
                status = cluster.get('status')
                
                print(f"ARN: {arn}")
                print(f"Nombre: {name}")
                print(f"Estado: {status}")
                

        return clusters

    except Exception as e:
        print(f"Error al listar los clusters de ECS: {e}", file=sys.stderr)
        return False


def describe_single_ecs_cluster(ecs_client, cluster_name):
    
    try:

        print(f"\nBuscando detalles para el cluster: {cluster_name}...")

        response = ecs_client.describe_clusters(
            clusters=[cluster_name], 
            include=['ATTACHMENTS', 'SETTINGS', 'STATISTICS', 'TAGS', 'CONFIGURATIONS'] 
        )

        
        clusters = response.get('clusters', [])

        if not clusters:
            print(f"Error: Cluster '{cluster_name}' no encontrado.")
            return 

        cluster_detail = clusters[0]
        
        print("-" * 50)
        print(f"Detalles del Cluster: {cluster_detail.get('clusterName')}")
        print(f"ARN: {cluster_detail.get('clusterArn')}")
        print(f"Estado: {cluster_detail.get('status')}")
        print(f"Servicios Activos: {cluster_detail.get('activeServicesCount')}")
        print(f"Instancias de Contenedor: {cluster_detail.get('registeredContainerInstancesCount')}")
        print("-" * 50)

        return cluster_detail
    
    except Exception as e:
        print(f"Error al describir el cluster: {e}", file=sys.stderr)
        raise Exception(f"Error al describir el cluster: {e}")