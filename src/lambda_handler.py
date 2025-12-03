from library.conn_ECS import conn_ecs
from library.list_clusters import list_ecs_clusters
from library.list_services_by_cluster import list_services_by_cluster
from library.save_info_CSV import save_info_CSV
from library.describe_services import describe_services


def lambda_handler(event, context=None):
    REGION = event.get("region", "us-east-1")
    
    fx_conn_ecs = conn_ecs(REGION)
    print("Conexion ECS: ",fx_conn_ecs)
    
    list_clusters = list_ecs_clusters(fx_conn_ecs)
    print("list_clusters:", list_clusters)
    
    services_by_cluster = list_services_by_cluster(fx_conn_ecs, list_clusters)
    print("list_services_by_cluster ejecutado: ", services_by_cluster)
    
    fx_describe_services = describe_services(fx_conn_ecs, list_clusters, services_by_cluster)
    print("fx_describe_services ejecutado: ", fx_describe_services) 
    
    save_info_CSV(fx_describe_services, "services.csv")
    print("Archivo services.csv guardado exitosamente.")
        
    
   
 