import pandas as pd
import io
from google.cloud import storage
from google.cloud import bigquery

def main_etl(data, context):
    #Llamamos a las funciones aquí
    etl_alternative_fuel(data, context)
    etl_taxis(data, context)
    etl_air_quality(data, context)
    etl_contaminacion_sonora(data, context)
    etl_elctric_car(data, context)

    return "Proceso ETL completado"

def etl_alternative_fuel(data, context):
    # Parámetros
    bucket_name = 'datasets_originales2'
    file_name = 'Alternative Fuel Vehicles US.csv'
    
    # Leer datos desde Google Cloud Storage
    data_af = read_data_from_storage(bucket_name, file_name)
    
    # Realizar transformaciones
    data_af = transform_alternative_fuel(data_af)
    
    # Almacenar resultados en BigQuery
    store_data_in_bigquery(data_af, 'Prueba_1', 'tabla_alternative_fuel')

    return "Proceso ETL de Alternative Fuel Vehicles US completado"

def etl_taxis(data, context):
    # Parámetros
    bucket_name = 'datasets_originales2'
    file_name = 'taxis_trips.csv'
    
    # Leer datos desde Google Cloud Storage
    data_taxis = read_data_from_storage(bucket_name, file_name)
    
    # Realizar transformaciones
    data_taxis  = transform_taxis(data_taxis )
    
    # Almacenar resultados en BigQuery
    store_data_in_bigquery(data_taxis , 'Prueba_1', 'tabla_taxis_trips')

    return "Proceso ETL de taxis_trips completado"

def etl_air_quality(data, context):
    # Parámetros
    bucket_name = 'datasets_originales2'
    file_name = 'Air_Quality.csv'
    
    # Leer datos desde Google Cloud Storage
    data_aq = read_data_from_storage(bucket_name, file_name)
    
    # Realizar transformaciones
    data_aq = transform_air_quality(data_aq)
    
    # Almacenar resultados en BigQuery
    store_data_in_bigquery(data_aq, 'Prueba_1', 'tabla_air_quality')

    return "Proceso ETL de Air_Quality completado"

    
def etl_contaminacion_sonora(data, context):
    # Parámetros
    bucket_name = 'datasets_originales2'
    file_name = 'Contaminacion Sonora.csv'
    
    # Leer datos desde Google Cloud Storage
    data_cs = read_data_from_storage(bucket_name, file_name)
    
    # Realizar transformaciones
    data_cs = transform_contaminacion_sonora(data_cs)
    
    # Almacenar resultados en BigQuery
    store_data_in_bigquery(data_cs, 'Prueba_1', 'tabla_contaminacion_sonora')

    return "Proceso ETL de Contaminacion Sonora completado"

def etl_elctric_car(data, context):
    # Parámetros
    bucket_name = 'datasets_originales2'
    file_name = 'ElectricCarData_Norm.csv'
    
    # Leer datos desde Google Cloud Storage
    data_ec = read_data_from_storage(bucket_name, file_name)
    
    # Realizar transformaciones
    data_ec = transform_electric_car(data_ec)
    
    # Almacenar resultados en BigQuery
    store_data_in_bigquery(data_ec, 'Prueba_1', 'tabla_electric_car')

    return "Proceso ETL de electric_car completado"


def read_data_from_storage(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    data = blob.download_as_text()
    return data

def transform_alternative_fuel(data):
    # Realizar las transformaciones necesarias para Alternative Fuel Vehicles US
    alternative_fuel = pd.read_csv(io.StringIO(data))
    alternative_fuel.drop_duplicates(inplace=True)
    alternative_fuel.drop(['Number of Passengers', 'Notes', 'Drivetrain', 'Engine Cylinder Count', 
             'Heavy-Duty Power System', 'Transmission Make', 'Transmission Type', 
             'PHEV Total Range', 'Conventional Fuel Economy City', 
             'Conventional Fuel Economy Highway', 'Conventional Fuel Economy Combined'], 
            axis=1, inplace=True)
    alternative_fuel = alternative_fuel[alternative_fuel['Fuel'] == 'Electric']
    return alternative_fuel.to_csv(index=False)

def transform_taxis(data):
    # Realizar las transformaciones necesarias para taxis_trips
    taxis = pd.read_csv(io.StringIO(data))
    
    # Leer el archivo 'taxi+_zone_lookup.csv' desde Google Cloud Storage
    bucket_name = 'datasets_originales2'
    file_name = 'taxi+_zone_lookup.csv'
    zone_data = read_data_from_storage(bucket_name, file_name)
    zone = pd.read_csv(io.StringIO(zone_data))

    # Renombrar columnas en "zone" para que coincidan con las que deseas agregar
    zone = zone.rename(columns={'LocationID': 'PULocationID', 'Borough': 'PUBorough', 'Zone': 'PUZone'})

    # Realizar la fusión en "taxis" con respecto a PULocationID
    taxis = taxis.merge(zone[['PULocationID', 'PUBorough', 'PUZone']], on='PULocationID', how='left')

    # Renombrar nuevamente las columnas en "zone" para la fusión de DOLocationID
    zone = zone.rename(columns={'PULocationID': 'DOLocationID', 'PUBorough': 'DOBorough', 'PUZone': 'DOZone'})

    # Realizar la fusión en "taxis" con respecto a DOLocationID
    taxis = taxis.merge(zone[['DOLocationID', 'DOBorough', 'DOZone']], left_on='DOLocationID', right_on='DOLocationID', how='left')

    taxis = taxis[['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
                   'passenger_count', 'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
                   'PULocationID', 'PUBorough', 'PUZone', 'DOLocationID', 'DOBorough', 'DOZone', 'payment_type', 'fare_amount', 'extra',
                   'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
                   'total_amount', 'congestion_surcharge', 'Airport_fee']]
    return taxis.to_csv(index=False)

def transform_air_quality(data):
     # Realizar las transformaciones necesarias para Air Quality
    air = pd.read_csv(io.StringIO(data))
    air = air.drop('Message', axis = 1)
    air = air.drop('Time Period', axis = 1)

    Air_cont_vehi = air.loc[
        (air['Name'] == 'Nitrogen Dioxide (NO2)') |
        (air['Name'] == 'Fine Particulate Matter (PM2.5)') |
        (air['Name'] == 'Traffic Density- Annual Vehicle Miles Traveled') |
        (air['Name'] == 'Ozone (O3)') |
        (air['Name'] == 'Sulfur Dioxide (SO2)')
    ]

    Air_cont_vehi['Start_Date'] = pd.to_datetime(Air_cont_vehi['Start_Date'])

    Air_cont_vehi['Year'] = Air_cont_vehi['Start_Date'].dt.year

    borough_air = Air_cont_vehi.loc[Air_cont_vehi['Geo Type Name'] == 'Borough'].copy() 

    borough_air['Year'] = borough_air['Year'].fillna(2016.0)

    borough_air['Year'] = borough_air['Year'].astype(int)

    borough_air.drop(['Unique ID', 'Indicator ID','Measure','Measure Info','Geo Type Name','Start_Date'], axis=1, inplace=True)
    return borough_air.to_csv(index=False)


def transform_contaminacion_sonora(data):
    # Realizar las transformaciones necesarias para Contaminacion Sonora
    contaminacion_sonora = pd.read_csv(io.StringIO(data))
    contaminacion_sonora.drop('2-1_rock-drill_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('1-2_medium-sounding-engine_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('1-3_large-sounding-engine_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('1-X_engine-of-uncertain-size_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('2-1_rock-drill_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('2-2_jackhammer_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('2-3_hoe-ram_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('2-4_pile-driver_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('2-X_other-unknown-impact-machinery_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('3-1_non-machinery-impact_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('4-1_chainsaw_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('4-2_small-medium-rotating-saw_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('4-3_large-rotating-saw_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('4-X_other-unknown-powered-saw_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('5-1_car-horn_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('5-2_car-alarm_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('5-3_siren_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('5-4_reverse-beeper_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('5-X_other-unknown-alert-signal_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('6-1_stationary-music_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('6-2_mobile-music_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('6-3_ice-cream-truck_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('6-X_music-from-uncertain-source_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('7-1_person-or-small-group-talking_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('7-2_person-or-small-group-shouting_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('7-3_large-crowd_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('7-4_amplified-speech_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('7-X_other-unknown-human-voice_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('split', axis=1,inplace=True)
    contaminacion_sonora.drop('sensor_id', axis=1,inplace=True)
    contaminacion_sonora.drop('audio_filename', axis=1,inplace=True)
    contaminacion_sonora.drop('annotator_id', axis=1,inplace=True)
    contaminacion_sonora.drop('block', axis=1,inplace=True)
    contaminacion_sonora.drop('2-2_jackhammer_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('2-3_hoe-ram_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('2-4_pile-driver_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('2-X_other-unknown-impact-machinery_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('3-1_non-machinery-impact_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('4-1_chainsaw_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('4-2_small-medium-rotating-saw_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('4-3_large-rotating-saw_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('4-X_other-unknown-powered-saw_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('5-1_car-horn_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('5-2_car-alarm_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('5-3_siren_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('5-4_reverse-beeper_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('5-X_other-unknown-alert-signal_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('6-1_stationary-music_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('6-2_mobile-music_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('6-3_ice-cream-truck_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('6-X_music-from-uncertain-source_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('7-1_person-or-small-group-talking_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('7-2_person-or-small-group-shouting_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('7-3_large-crowd_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('7-4_amplified-speech_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('7-X_other-unknown-human-voice_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('8-1_dog-barking-whining_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('1-1_small-sounding-engine_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('8-1_dog-barking-whining_proximity', axis=1,inplace=True)
    contaminacion_sonora.drop('2_machinery-impact_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('3_non-machinery-impact_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('4_powered-saw_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('5_alert-signal_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('6_music_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('7_human-voice_presence', axis=1,inplace=True)
    contaminacion_sonora.drop('8_dog_presence', axis=1,inplace=True)

    return contaminacion_sonora.to_csv(index=False)

def transform_electric_car(data):
    # Realizar las transformaciones necesarias para Alternative Fuel Vehicles US
    electric_car = pd.read_csv(io.StringIO(data))
    
    # COLUMNAS A ELIMINAR DADO QUE NO HACEN PARTE DEL ALCANCE DEL PROYECTO

    columns_to_drop = ["Accel", "TopSpeed", "RapidCharge", "PowerTrain","PlugType","Segment","Seats"]
    electric_car = electric_car.drop(columns=columns_to_drop)

    return electric_car.to_csv(index=False)

def store_data_in_bigquery(data, dataset_id, table_id):
    # Inicializar el cliente de BigQuery
    client = bigquery.Client()

    # Crear una referencia a la tabla en BigQuery
    table_ref = client.dataset(dataset_id).table(table_id)

    # Cargar los datos en la tabla
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        write_disposition="WRITE_TRUNCATE"  # Esto reemplazará la tabla si ya existe
    )
    # Convertir los datos en un archivo de tipo StringIO
    data_io = io.StringIO(data)

    # Cargar los datos en BigQuery
    client.load_table_from_file(data_io, table_ref, job_config=job_config)
    
    return "Datos almacenados en BigQuery correctamente"