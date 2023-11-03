import pandas as pd
import gdown


'''
EXTRACCION DE DATOS DE GOOGLE DRIVE
'''
# Identificador del archivo en Google Drive
file_id = "1yWpl9nGxQkoylCU_SA0LFwCAENyftGH2"

# URL de descarga del archivo
file_url = f"https://drive.google.com/uc?id={file_id}"

# Nombre del archivo de destino
output_file = "ElectricCarData_Norm.csv"

# Descargar el archivo
gdown.download(file_url, output_file, quiet=False)

# Cargar el archivo CSV con Pandas
df_Elec_Car = pd.read_csv(output_file)

# Ahora se puede trabajar con el DataFrame "df_Elec_Car" 
# que contiene los datos del archivo CSV.


'''
TRANSFORMACION DE DATOS, TRANSFORMACION DE ElectricCarData_Norm
'''
# COLUMNAS A ELIMINAR DADO QUE NO HACEN PARTE DEL ALCANCE DEL PROYECTO

columns_to_drop = ["Accel", "TopSpeed", "RapidCharge", "PowerTrain","PlugType","Segment","Seats"]
df_Elec_Car = df_Elec_Car.drop(columns=columns_to_drop)

# Guardar el DataFrame en un archivo CSV
df_Elec_Car.to_csv("carros_electricos_limpio.csv", index=False)
