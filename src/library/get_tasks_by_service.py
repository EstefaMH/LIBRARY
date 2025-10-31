def get_tasks_by_service(ecs_client, list_cluster, list_services):
    tasks_info = []
    
    for cluster_arn in list_cluster['clusterArns']:
        print(f"Obteniendo tareas para el cluster: {cluster_arn}...")
        
        for service_arn in list_services:
            print(f"  Servicio: {service_arn}")
            try:
                tasks = []
                next_token = None
                
                while True:
                    if next_token:
                        response = ecs_client.list_tasks(
                            cluster=cluster_arn,
                            serviceName=service_arn,
                            nextToken=next_token
                        )
                    else:
                        response = ecs_client.list_tasks(
                            cluster=cluster_arn,
                            serviceName=service_arn
                        )
                    
                    tasks.extend(response.get('taskArns', []))
                    next_token = response.get('nextToken')
                    
                    if not next_token:
                        break
                
                if not tasks:
                    print(f"    No se encontraron tareas para el servicio {service_arn}.")
                    continue
                
                print(f"    Se encontraron {len(tasks)} tareas para el servicio {service_arn}.")
                
                for task_arn in tasks:
                    task_response = ecs_client.describe_tasks(
                        cluster=cluster_arn,
                        tasks=[task_arn]
                    )
                    
                    for task in task_response.get('tasks', []):
                        task_id = task.get('taskArn')
                        last_status = task.get('lastStatus')
                        desired_status = task.get('desiredStatus')
                        launch_type = task.get('launchType')
                        
                        tasks_info.append({
                            "clusterArn": cluster_arn,
                            "serviceArn": service_arn,
                            "taskArn": task_id,
                            "lastStatus": last_status,
                            "desiredStatus": desired_status,
                            "launchType": launch_type
                        })
                        
                        print(f"      Task ARN: {task_id}")
                        print(f"      Last Status: {last_status}")
                        print(f"      Desired Status: {desired_status}")
                        print(f"      Launch Type: {launch_type}")
                        print("-" * 30)
            
            except Exception as e:
                print(f"    Error al obtener tareas para el servicio {service_arn}: {e}")
                raise Exception(f"Error al obtener tareas para el servicio {service_arn}: {e}")
    
    return tasks_info
    