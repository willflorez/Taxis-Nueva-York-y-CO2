## Taxis Nueva York y Calidad del Aire

<p align="center">
<img src="https://img2.rtve.es/v/5427304?w=1600&preview=1572458814211.jpg"  height=300>
</p>


## INDICE 
<!-- TABLA DE CONTENIDO -->
<details>
  <summary>TABLA DE CONTENIDO</summary>
  <ol>  
    <li><a href="#EQUIPO-DE-TRABAJO-DATA-OK">EQUIPO DE TRABAJO DATA OK</a></li>
    <li><a href="#INTRODUCCION">INTRODUCCION</a></li>
    <li><a href="#DESCRIPCION-DEL-PROBLEMA">DESCRIPCION DEL PROBLEMA</a></li>
    <li><a href="#OBJETIVO-GENERAL">OBJETIVO GENERAL</a></li>
    <li><a href="#OBJETIVOS-ESPECIFICOS">OBJETIVOS ESPECIFICOS</a></li>
    <li><a href="#INDICADORES-DE-RENDIMIENTO-KPI'S">INDICADORES DE RENDIMIENTO KPI'S</a></li>
    <li><a href="#METODOLOGIA-DE-TRABAJO">METODOLOGIA DE TRABAJO</a></li>
    <li><a href="#STACK-TECNOLOGICO">STACK TECNOLOGICO</a></li>
    <li><a href="#DIAGRAMA-DE-GANTT">DIAGRAMA DE GANTT</a></li>
    <li><a href="#ANALISIS-PRELIMINAR-DE-DATOS">ANALISIS PRELIMINAR DE DATOS</a></li>
  </ol>
</details>

## EQUIPO DE TRABAJO DATA OK

El grupo 7 del proyecto final de Henry de la carrera de Data Science está conformado por las siguientes personas y según sus habilidades desempeñarán los roles a continuación:

1. Néstor Cardona - Data Engineer
2. Giovanny Muñoz - Data Analyst
3. Santiago Magris - Data Engineer
4. Ramiro Tejedor - Data Engineer
5. William Flórez - Data Analyst

## INTRODUCCION

El siguiente proyecto analiza varios conjuntos de datos que entregan información acerca del negocio de transporte en la ciudad de Nueva York, plataformas de viajes y taxis son los protagonistas principales, de la misma manera contamos con datos que informan la calidad del aire y la contaminación sonora en la ciudad. El equipo analizará estos datos para brindar un modelo de predicción de machine learning y desarrollará objetivos de investigación y propondrá KPI' s para medir el cumplimiento de esos objetivos. Con el fin de robustecer la fuente de información encontrará nuevos conjuntos de datos que emplíen el espectro de análisis. 

## DESCRIPCION DEL PROBLEMA

El servicio de transporte particular de pasajeros ha tenido un mayor incremento desde la aparición de empresas como uber, llegando a competir con el servicio tradicional de taxis. Esto implica una mayor circulación constante de vehículos en la ciudad de Nueva York, por lo tanto mayores emisiones de CO2 e incremento de la contaminación acústica. La empresa 'TransFast' estudia la posibilidad de invertir en el sector de transporte de pasajeros en automóviles con la visión de una ciudad menos contaminada, para esto pretente participar en este sector con una flota de vehículos eléctricos con la finalidad de contribuir al cuidado del medio ambiente y además evaluar la rentabilidad de la inversión.
La empresa 'TransFast' con la ayuda de la consultora 'dataok' desarrollará este proyecto para definir su viabilidad y suministrar las posibles oportunidades en el mercado.

## OBJETIVO GENERAL

Desarrollar un modelo de gestión eficiente para la empresa TRANSFAST, centrándonos en la optimización del retorno de inversión y la reducción significativa de la contaminación atmosférica y sonora, mediante la implementación de vehículos eléctricos.

## OBJETIVOS ESPECIFICOS

1. Identificar los distritos más contaminados, en términos de calidad de aire y exceso de ruido.
2. Definir la rentabilidad del negocio de transporte de pasajeros en automóviles por distritos.
3. Entregar una propuesta de inversión a TransFast que ayude a tomar la decisión de participar o no en el mercado.
4. Crear un modelo de machine learning que entregue al usuario, según un punto de partida y de destino y una hora de viaje, la predicción del costo del servicio.

## INDICADORES DE RENDIMIENTO KPI'S

1. Obtener la relación entre los niveles de emisión de gases nocivos en el aire y la CONTAMINACIÓN POR DISTRITO en la ciudad de Nueva York, durante el período de 2022 a 2023.
KPI: Porcentaje de reducción DEL 5% de las emisiones de gases nocivos por DISTRITO CON RESPECTO AL AÑO ANTERIOR
Este KPI mide la cantidad de emisiones de gases nocivos que se reducen por cada DISTRITO. Este KPI es útil para evaluar el impacto de las medidas que se tomen para reducir las emisiones de gases nocivos.

% reducción = (Emisiones iniciales - Emisiones finales) / Emisiones iniciales * 100

2. Determinar la participación del ruido en decibeles de los vehículos eléctricos en circulación en la ciudad de Nueva York, durante el período de 2022 a 2023, respecto a los decibeles de vehículos convencionales
KPI: reducir un 5% el ruido de motores en la ciudad de nueva york

Este KPI mide la cantidad de ruido que producen los vehículos eléctricos en circulación, en comparación con el ruido total producido por todos los vehículos en circulación. Este KPI es útil para evaluar el impacto de los vehículos eléctricos en la contaminación acústica.

% ruido = (Ruido de los vehículos eléctricos / Ruido total) * 100

3. Conocer el comportamiento del valor de los viajes por milla comparando cada uno de los distritos. 
KPI: Comparar el promedio del costo de viajes que paga el usuario de los diferentes distritos por milla permitiendo conocer el más rentable.
Este KPI se calcula promediando el valor de los viajes por milla en cada distrito y su cambio porcentual.
Ingresos totales / millas recorridas.

4. Conocer el comportamiento de los viajes en taxi en la ciudad de Nueva York.
KPI: Identificar la variación de la cantidad de viajes realizados en el año a comparación del anterior.
Este KPI se calcula restando el total de viajes del año actual menos el anterior divido entre la cantidad de viajes del año anterior.

KPI = (total de viajes del año actual - total de viajes año anterior) / total de viajes año anterior * 100

## ALCANCE DEL PROYECTO

El proyecto tiene dos objetivos principales:

1. Evaluar el Retorno de Inversión (ROI) de la implementación de vehículos eléctricos en la flota de la empresa de transporte de pasajeros.
2. Analizar la relación entre el uso de vehículos eléctricos y la calidad del aire y la contaminación sonora en la ciudad de Nueva York.


Alcance del Análisis de Retorno de Inversión (ROI):

1. Evaluación de los costos asociados a la adquisición y operación de vehículos eléctricos, incluyendo costos de mantenimiento y carga.
2. Cálculo del ROI proyectado considerando los factores anteriores y proyecciones de ingresos.
3. Identificación de posibles fuentes de financiamiento y oportunidades de incentivos fiscales para la adquisición de vehículos eléctricos.

Alcance del Análisis de Contaminación Ambiental y Sonora:

1. Recopilación de datos de calidad del aire en la ciudad de Nueva York, incluyendo la concentración de contaminantes atmosféricos relevantes.
2. Recopilación de datos de contaminación sonora en áreas urbanas y rutas de tráfico frecuentes.
3. Evaluación de la relación entre el uso de vehículos eléctricos y la reducción de emisiones contaminantes y ruido en comparación con vehículos convencionales.
4. Identificación de áreas críticas en la ciudad donde la implementación de vehículos eléctricos podría tener un impacto significativo en la calidad del aire y la contaminación sonora.

## METODOLOGIA DE TRABAJO

DATA OK escoge trabajar bajo la metodología de trabajo conocida como SCRUM, basada en sprints cortos usados para crear un ciclo de proyecto. Estos ciclos son ideales para el proyecto pues duran entre una y dos semanas con equipos de hasta diez personas. Este proyecto se adelanta con un equipo de 5 personas y tres semanas de plazo para la entrega completa, cada sprint es de cinco días hábiles. Los sprints se dividen en equipos pequeños y es un plan ideal para adelantar este proyecto.

SCRUM MASTER: Néstor Cardona, Data Engineer.

## STACK TECNOLOGICO


![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

## DIAGRAMA DE GANTT

A continuación las actividades a realizar en cada uno de los sprints a lo largo de las tres semanas de duración del proyecto, representados en un diagrama de Gantt.

![Alt text](gantt.png)

## ANALISIS PRELIMINAR DE DATOS

1. Dataset ElectricCarData_Norm

1. Verificar los valores NaN de las columnas en el archivo y se valida que no tiene valores NaN y el mapa de calor corrobora dicha información, pues como resultado es un mapa vacio.

2. Detectar y visualizar outliers en la columna 'precio'
Se visualiza una información sin outliers, pues los datos fuera de rango son perfectamente normales pues son vehiculos de alta gama
Lo cual es confirmado por el diagrama de caja

3. Verificar valores duplicados en el archivo
Se visualiza un archivo sin duplicados lo cual con el Histograma para contar filas duplicadas lo confirma, pues no se tienen filas duplicadas.


La información de Carros eléctricos está bastante depurada, sin outliers, ni NaN, ni campos vacíos, sin embargo hay información que no es necesaria para el alcance del proyecto, la siguiente es la que se considera relevante:

Efficiency (Eficiencia): La eficiencia es crucial para maximizar el rango de conducción por carga, lo que puede ayudar a reducir costos operativos y aumentar la productividad del taxi.

Range (Autonomía): Una mayor autonomía permite que el taxi eléctrico pueda realizar más viajes antes de necesitar recargarse, lo que es esencial en una ciudad como Nueva York, donde los taxis pueden estar en servicio continuamente.

FastCharge (Carga Rápida): La capacidad de carga rápida es importante para minimizar el tiempo de inactividad del taxi durante la recarga, lo que es crítico para mantener la operación eficiente.

Price (Precio): El precio del vehículo eléctrico es una consideración importante para los propietarios de flotas de taxis, ya que afecta directamente a la inversión inicial.

Brand y Model (Marca y Modelo): La reputación de la marca y el modelo del vehículo puede influir en la percepción de los clientes y la confiabilidad del vehículo y adicionalmente en el mantenimiento y respaldo en repuestos.

Por lo tanto se eliminan las siguientes columnas:
Accel (Aceleración) , TopSpeed (Velocidad Máxima), RapidCharge (Carga Rápida), PowerTrain (Tren de Potencia), PlugType (Tipo de Conector), Segment (Segmento) y Seats (Número de Asientos).

2. Dataset Alternative Fuel Vehicles

Del dataset Alternative Fuel Vehicles hicimos una limpieza para quedarnos solo con los automoviles electricos, ya que a donde va enfocado nuestro proyecto, eliminando asi las filas con datos de automoviles con otro tipo de combustible. Tambien eliminamos las columnas que contenian mas del 80% de sus datos nulos, como tambien columnas que hacian referencia a los autos con otro tipo de combustible alternativo.

3. Dataset Contaminación Sonora

Del dataset Contaminación Sonora hicimos una limpieza de datos profundo, pasando de 78 columnas a 12. Esto ya que el dataset contenia informacion de todo tipo de sonidos, desde sonidos de motores hasta ladridos de perros. Al terminar la limpieza dejamos solo las columnas que contenian datos de sonidos de motores.

4. Dataset Taxi+

El dataset taxi+_zone_lookup.csv  se cruza con un dataset extraído de  https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page llamado taxis_trips. El mismo contiene la informacion de todos los viajes en taxi del mes de junio del 2023, como pueden ser: Lugar de salida, lugar de llegada, costo del viaje, etc. Utilizamos las columnas PULocationId y DuLocationId para hacer un merge mediante la columna LocationId del dataset taxi+_zone_lookup.csv. Esto se pudo hacer ya que ambos datasets provienen de la misma pagina. Este cruce de datasets se hizo con el objetivo de especificar el distrito y la zona en donde se tomaron y dejaron a los pasajeros en sus respectivos viajes en taxi.

5. Dataset AirQuality

Este conjunto de datos aporta información acerca de la cantidad de emisiones de gases nocivos en la ciudad de Nueva York en los años comprendidos entre 2013 y 2021, cuenta con 12 columnas y 16122 filas, las columnas 'Message' y ´Time Period' se desestiman no aportan información para el análisis, la primera es una columna totalmente vacía y la segunda contiene datos redundantes de fechas, pues ya existe una columna con esa información. Este conjunto de datos es clave para desarrollar el KPI propuesto de calidad del aire, contiene columnas donde resalta la concentración en partes por billon y el lugar geográfico de la medición.

6. Datasets Light Duty Vehicles y Vehicle Fuel Economy Data

Luego de analizar la composición de los siguientes datasets y teniendo en cuenta los objetivos y alcance del la actual propuesta se ha decido que no se consideraran dichos datasets debido a que no aportan información relevante que contribuya a la obtención de conclusiones precisas y alineadas con el enfoque del proyecto.
