from locations import POIS

def load_data(redis_client):
    redis_client.delete("poi:locations", "poi:info")

    for poi in POIS:
        redis_client.geoadd("poi:locations", (poi["lon"], poi["lat"], poi["id"]))

        redis_client.hset("poi:info", poi["id"], poi["name"])
    print(f"Datos cargados: {len(POIS)} ubicaciones procesadas.")
    