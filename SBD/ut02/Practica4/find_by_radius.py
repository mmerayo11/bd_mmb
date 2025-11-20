def find_at_location(redis_client, lat, lon, distance=2000):
    print(f"\n--- Buscando en radio de {distance}m desde {lat}, {lon} ---")
    
    resultados = redis_client.geosearch(
        name="poi:locations",
        longitude=lon,
        latitude=lat,
        radius=distance,
        unit="m",
        withdist=True,
        sort="ASC"
    )
    
    if not resultados:
        print("No se encontraron lugares cercanos.")
        return

    print(f"Encontrados {len(resultados)} POIs:")
    for poi_id, dist in resultados:
        nombre = redis_client.hget("poi:info", poi_id)
        print(f" -> {nombre} ({poi_id}) | a {int(dist)} metros")