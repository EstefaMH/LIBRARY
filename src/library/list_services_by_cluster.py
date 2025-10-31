def list_services_by_cluster(ecs_client, list_clusters):
    """
    Lista y muestra los servicios de cada cluster ECS.

    Parámetros:
        ecs_client (boto3.client): Cliente ECS configurado.
        list_clusters (dict): Diccionario con los ARNs de los clusters.

    Returns:
        list: Lista de ARNs de servicios encontrados, o False si ocurre un error.

    Raises:
        Exception: Si ocurre un error al listar los servicios.

    Ejemplo:
        services = list_services_by_cluster(ecs_client, clusters)
    """
    if list_clusters and 'clusterArns' in list_clusters:
        for cluster_arn in list_clusters['clusterArns']:
            try:
                print(f"\nListando servicios para el cluster: {cluster_arn}...\n")

                services = []
                next_token = None

                while True:
                    if next_token:
                        response = ecs_client.list_services(
                            cluster=cluster_arn,
                            nextToken=next_token
                        )
                    else:
                        response = ecs_client.list_services(
                            cluster=cluster_arn
                        )

                    services.extend(response.get('serviceArns', []))
                    next_token = response.get('nextToken')

                    if not next_token:
                        break

                if not services:
                    print(f"No se encontraron servicios en el cluster {cluster_arn}.")
                    continue
                
                return services

               
            except Exception as e:
                print(f"Error al listar los servicios del cluster {cluster_arn}: {e}")
                raise Exception(f"Error al listar los servicios del cluster {cluster_arn}: {e}")