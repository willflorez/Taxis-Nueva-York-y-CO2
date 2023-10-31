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
SE CREA LA CLASE FUNCIONES EDA, PARA VERIFICAR LA INFORMACION
'''

class funciones_EDA:
    '''
    Autor: https://github.com/idaroga - Fecha: 16-sept-2023
    '''
    def __init__(self):
        # El método __init__ es el constructor de la clase
        pass

    def _1_view_df_info(self, df:pd.DataFrame):
        '''
        Obtener los tipos de datos, la cantidad por cada uno y el porcentaje de valores nulos para cada columna de un dataframe.
        Recibe como parámetro un dataframe.
        Autor: https://github.com/idaroga - Fecha: 16-sept-2023
        '''

        # Calcular el conteo duplicados por columna
        df_duplicados = df.apply(lambda col: col.duplicated().sum()).reset_index()     # duplicados por columna
        df_duplicados.rename(columns={"index": "Column", 0: "Duplicados"}, inplace=True) # renombrar columnas para union
        # df_merge = pd.merge(df_merge, df_3, on=columna_union, how='left')

        # Agregar columna con el conteo unicos por columna
        df_unicos = df.apply(lambda col: col.nunique()).reset_index()     # valores unicos por columna
        df_unicos.rename(columns={"index": "Column", 0: "Unicos"}, inplace=True) # renombrar columnas para union
        df_merge = pd.merge(df_duplicados, df_unicos, on="Column", how='left')

        # Agregar una columna con el conteno de nulos por columna
        df_nulos = df.isnull().sum()  # Hallamos los valores nulos y se almacenan en una serie
        df_nulos = df_nulos.reset_index()  # Convierte el índice en una columna
        df_nulos.columns = ['Column', 'Nulos']  # Asigna un nombre a la columna del índice si es necesario
        df_merge = pd.merge(df_merge, df_nulos, on="Column", how='left')

        # agregar columna de porcentaje nulos
        df_merge["%_nulos"] = round(df_merge["Nulos"] / df.shape[0] * 100, 2)  # Porcentaje total de registros nulos

        # Agregar columna con los tiposde datos y su conteo
        df_result = df.apply(lambda col: col.apply(type).value_counts())  # Aplicar la función a todas las columnas del DataFrame
        df_result = df_result.T.reset_index()  # Transponer el resultado y restablecer el índice
        df_result.columns = ["Column"] + df_result.columns[1:].tolist()  # Renombrar las columnas
        df_merge = pd.merge(df_merge, df_result, on="Column", how='left')

        print("total filas: ", df.shape[0])
        print("total columnas: ", df.shape[1])
        print("filas completamente nulas: ", df.isna().all(axis=1).sum())  # Filas que se encuentran totalmente en nulo
        print("filas totalmente duplicadas:", len(df[df.duplicated()]))
        print("-------------------------------------------------------------")

        # estadisticas generales
        print("\n", df.describe())
        print("-------------------------------------------------------------")

        return df_merge
    
    def _2_view_duplicates(self, df:pd.DataFrame, col:str, valor=""):
        '''
        Obtener los registros donde hay valores duplicados para una columna.
        Recibe como parámetro un dataframe, el nombre de una columna y si quiere el valor duplicado encontrado.
        Autor: https://github.com/idaroga - Fecha: 16-sept-2023
        '''
        valor = str(valor)
        if valor == "":
            filtro = df[df.duplicated(subset=[col], keep=False)]
        else:
            filtro = df[df[col].astype(str) == valor]
        return filtro
 
    def _3_view_data_by_types(self, df:pd.DataFrame, columna=""):
    
        '''
        Obtener el tipo de datos que maneja cada columna e imprimir los valores unicos de cada tipo.
        Recibe como parámetro un dataframe y si quiere una columna en particular.
        Autor: https://github.com/idaroga - Fecha: 16-sept-2023
        '''
        lista_columnas = df.columns.tolist()
        if columna == "":
            for indice in range (0, len(lista_columnas)):
                print("NOMBRE COLUMNA: ", df.columns[indice])
                self.__view_data__(df, df.columns[indice])
                print("-------------------------------------------------------------")
        else:
            indice = lista_columnas.index(columna)
            self.__view_data__(df, df.columns[indice])

    def _4_view_order_values(self, df:pd.DataFrame, col:str):
        '''
        Retornar una lista de valores únicos de tipo str de una columna ordenados alfabéticamente.
        Se utiliza para revisar la sintaxis, estructura y formato de los datos de una columna.
        Recibe como parámetro un dataframe y el nombre de la columna.
        Autor: https://github.com/idaroga - Fecha: 16-sept-2023
        '''
        # Obtener los valores únicos de la columna
        valores_unicos = df[col].unique()

        # Filtrar y ordenar alfabéticamente los valores únicos de tipo str
        valores_str_ordenados = sorted([valor for valor in valores_unicos if isinstance(valor, str)])

        return valores_str_ordenados

    def _5_view_unique_value_percent(self, df:pd.DataFrame, columna=""):
        '''
        Obtener el porcentaje que representa cada valor unico en una columna.
        Recibe como parámetro un dataframe y si quiere una columna en particular.
        Autor: https://github.com/idaroga - Fecha: 16-sept-2023
        '''
        if columna == "":
            lista_de_columnas = df.columns.tolist()
            for col in lista_de_columnas:
                columna = df[col]

                # Porcentaje que representa cada valor dato respecto a toda la columna
                conteo_datos = columna.value_counts()
                total_datos = len(columna)
                porcentaje_victimas = round((conteo_datos / total_datos) * 100, 2)

                # Combina los resultados en un nuevo DataFrame
                resultados = pd.DataFrame({"Cantidad": conteo_datos, "Porcentaje (%)": porcentaje_victimas})
                
                # y deseas ordenarlo de manera descendente según la columna "Cantidad"
                resultados = resultados.sort_values(by="Cantidad", ascending=False)

                print(resultados)
                print("-------------------------------------------------------------")
        else:
            columna = df[columna]

            # Porcentaje que representa cada valor dato respecto a toda la columna
            conteo_datos = columna.value_counts()
            total_datos = len(columna)
            porcentaje_victimas = round((conteo_datos / total_datos) * 100, 2)

            # Combina los resultados en un nuevo DataFrame
            resultados = pd.DataFrame({"Cantidad": conteo_datos, "Porcentaje (%)": porcentaje_victimas})
            
            # y deseas ordenarlo de manera descendente según la columna "Cantidad"
            resultados = resultados.sort_values(by="Cantidad", ascending=False)

            print(resultados)

    def __view_data__(self, df:pd.DataFrame, col:str):    
        '''
        Obtener el tipo de datos que maneja una columna e imprimir los valores unicos de cada tipo.
        Recibe como parámetro un dataframe y el nombre de la columna.
        Autor: https://github.com/idaroga - Fecha: 16-sept-2023
        '''
        columna = df[col]
        # Crear una lista para almacenar los resultados
        tipos_de_datos = columna.apply(type).unique()

        for tipo in tipos_de_datos:
            resultados = []
            filtro = columna.apply(lambda x: isinstance(x, tipo))
            total_valores = filtro.sum()
            valores_unicos = columna[filtro].unique()
            porcentaje_col = str(round(total_valores / len(columna) * 100, 2)) + "%"
            porcentaje_tipo = str(round(len(valores_unicos) / total_valores * 100, 2)) + "%"

            # Agregar los resultados a la lista
            resultados.append([tipo, total_valores, porcentaje_col, len(valores_unicos), porcentaje_tipo])

            # Crear un DataFrame con los resultados
            resultado_df = pd.DataFrame(resultados, columns=['Tipo Dato', 'Cant. Valores', '% en Columna', 'Cant. Val. Únicos', '% de únicos'])

            print(resultado_df.T)
            print()
            print(f'Valores únicos: {valores_unicos}')
            print('\n')

'''
FUNCIONES EDA PARA VERIFICAR DUPLICADOS, VALORES UNICOS
'''

eda = funciones_EDA()
info_df = eda._1_view_df_info(df_Elec_Car)
duplicates = eda._2_view_duplicates(df_Elec_Car, "Brand")
eda._3_view_data_by_types(df_Elec_Car)
unique_values = eda._4_view_order_values(df_Elec_Car, "Brand")
percentages = eda._5_view_unique_value_percent(df_Elec_Car, "Brand")

# COLUMNAS A ELIMINAR DADO QUE NO HACEN PARTE DEL ALCANCE DEL PROYECTO

columns_to_drop = ["Accel", "TopSpeed", "RapidCharge", "PowerTrain","PlugType","Segment","Seats"]
df_Elec_Car = df_Elec_Car.drop(columns=columns_to_drop)

# Guardar el DataFrame en un archivo CSV
df_Elec_Car.to_csv("carros_electricos_limpio.csv", index=False)
