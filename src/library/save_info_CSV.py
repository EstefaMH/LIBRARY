def save_info_CSV(data, filename):
    headers = ["clusters", "service", "desiredCount", "taskDefinition", "CPU", "Memory", "scaling_min", "scaling_max"]
    import csv
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(headers)
            for item in data:
                writer.writerow(item.values())
    except Exception as e:
        print(f"Error al guardar los datos en CSV: {e}")