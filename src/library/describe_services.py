def describe_services(ecs_client, list_clusters, list_services):
    info_services = []
    
    for cluster_arn in list_clusters['clusterArns']:
        
        print(f"Se encontraron {len(list_services)} servicios en el cluster {cluster_arn}. Detalle:")
        
        for i in range(0, len(list_services), 1):
            batch_arns = list_services[i:i + 1]
            detail_response = ecs_client.describe_services(
                cluster=cluster_arn,
                services=batch_arns
            )

            for service in detail_response.get('services', []):
                arn = service.get('serviceArn')
                name = service.get('serviceName')
                status = service.get('status')
                desired_count = service.get('desiredCount')
                running_count = service.get('runningCount')
                pending_count = service.get('pendingCount')
                
                task_definition = service.get('taskDefinition')
                container_definitions = ecs_client.describe_task_definition(taskDefinition=task_definition)['taskDefinition']['containerDefinitions']
                
                
                
                for container in container_definitions:
                    
                    info_services.append({
                        "clusterArn": cluster_arn,
                        #"serviceArn": arn,
                        "serviceName": name,
                        #"status": status,
                        "desiredCount": desired_count,
                        #"runningCount": running_count,
                        #"pendingCount": pending_count,
                        "taskDefinition": task_definition,
                        
                        "cpu": container.get('cpu'),
                        "memory": container.get('memory'),
                        "image": container.get('image'), 
                        #"containerName": container.get('name')   
                    })
                   
                    
                    print(f"ARN: {arn}")
                    print(f"Nombre: {name}")
                    print(f"Estado: {status}")
                    print(f"Desired Count: {desired_count}")
                    print(f"Running Count: {running_count}")
                    print(f"Pending Count: {pending_count}")
                    print(f"Task Definition: {task_definition}")
                   
                
                
                
        print("inforamcion",info_services)
        print("longitud",len(info_services))
        print("-" * 60)
        
    return info_services