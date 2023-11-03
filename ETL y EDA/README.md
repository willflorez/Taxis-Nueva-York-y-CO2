## EXTRACCION TRANSFORMACION Y CARGA

<p align="center">
<img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F035b6d20-ddc4-450d-8684-e1c0c57d11ae_758x423.png"  height=300>
</p>

## INDICE 
<!-- TABLA DE CONTENIDO -->
<details>
  <summary>TABLA DE CONTENIDO</summary>
  <ol>  
    <li><a href="#PIPELINE">PIPELINE</a></li>
    <li><a href="#STACK-TECNOLOGICO">STACK TECNOLOGICON</a></li>
    <li><a href="#DATA-LAKE">DATA LAKE</a></li>
    <li><a href="#CLOUD-FUNCTIONS">CLOUD FUNCTIONS</a></li>
    <li><a href="#DATA-WAREHOUSE">DATA WAREHOUSE</a></li>
    <li><a href="#VIDEO">VIDEO</a></li>
  </ol>
</details>

## PIPELINE

Flujo de trabajo para la transformación de los conjuntos de datos en Google Cloud Plataform.

![Alt text](pipeline.png)

## STACK TECNOLOGICO

![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

## DATA LAKE

Se cargan los datos sin ningún tipo de transformación en Google Cloud Storage de manera manual, como el paso inicial para la creación del Data Lake del proyecto.

![Alt text](storage.png)

## CLOUD FUNCTIONS

El objetivo de esta etapa fundamental es que se reconozcan los cambios que ocurren en el Data Lake y que se puedan procesar esos cambios para luego almacenarlos en Data Warehouse.

![Alt text](functions.png)

## DATA WAREHOUSE

Hace aparición la herramienta de BigQuery útil como Data Warehouse y que entre otras cosas permite manipular los conjuntos de datos procesados después de ETL.

![Alt text](datawarehouse.png)

## VIDEO

## DICCIONARIO DE DATOS

# Diccionario de Datos [<a href="https://docs.google.com/spreadsheets/d/1gadlFJPPdkcMyuvO2AZLorkqomhDN8W7/edit#gid=1163311947" target="_blank">Link al Diccionario</a>]
