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

1. Obtener la relación entre los niveles de emisión de gases nocivos en el aire y la circulación de vehículos en la ciudad de Nueva York, durante el período de 2022 a 2023.
KPI: Porcentaje de reducción o ampliación de las emisiones de gases nocivos por unidad de circulación de vehículos.
Este KPI mide la cantidad de emisiones de gases nocivos que se reducen por cada unidad de circulación de vehículos. Este KPI es útil para evaluar el impacto de las medidas que se tomen para reducir las emisiones de gases nocivos.

% reducción = (Emisiones iniciales - Emisiones finales) / Emisiones iniciales * 100

2. Determinar la participación del ruido en decibeles de los vehículos eléctricos en circulación en la ciudad de Nueva York, durante el período de 2022 a 2023, respecto a los decibeles permitidos.
KPI: Porcentaje de ruido de los vehículos eléctricos en circulación respecto al ruido total.

Este KPI mide la cantidad de ruido que producen los vehículos eléctricos en circulación, en comparación con el ruido total producido por todos los vehículos en circulación. Este KPI es útil para evaluar el impacto de los vehículos eléctricos en la contaminación acústica.

% ruido = (Ruido de los vehículos eléctricos / Ruido total) * 100

3. Identificar los vehículos eléctricos que tienen un costo total por kilómetro inferior a 0,5 euros.
KPI: Costo total por kilómetro

Este KPI se calcula dividiendo el costo total del vehículo por el número de kilómetros que puede recorrer. El costo total del vehículo incluye el costo de adquisición, el costo de mantenimiento y el costo de carga.

Costo total por kilómetro = (Costo de adquisición + Costo de mantenimiento + Costo de carga) / Número de kilómetros

4. Identificar los vehículos eléctricos que tienen un ROI superior al 5 %.
KPI: Tasa de retorno de la inversión (ROI)
Este KPI se calcula dividiendo el ahorro en costos por el costo total del vehículo. El ahorro en costos se calcula comparando los costos de un vehículo eléctrico con los costos de un vehículo de combustión interna.

ROI = (Ahorro en costos) / Costo total del vehículo

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

## DIAGRAMA DE GANTT

A continuación las actividades a realizar en cada uno de los sprints a lo largo de las tres semanas de duración del proyecto, representados en un diagrama de Gantt.

![Alt text](gantt.png)

## ANALISIS PRELIMINAR DE DATOS
