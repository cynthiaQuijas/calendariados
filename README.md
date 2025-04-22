# (CLOUD COMPUTING) ACTIVIDAD DE EVALUACIÓN: Despliegue de un servicio entrenado a partir de una base de datos SQL
## Equipo Insight Engineers
Integrantes: 
- Yuu Ricardo Akachi Tanaka | A01351969
- Viviana Alanis Fraige | A01236316
- Cynthia Cristal Quijas Flores | A01655996
- David Fernando Armendáriz Torres | A01570813
- Luis Maximiliano López Ramírez | A00833321
- Kevin Antonio González Díaz | A01338316

## Instrucciones de uso
### 1. Clonar repositorio
```bash
git clone https://github.com/cynthiaQuijas/calendariados.git
cd calendariados
```

### 2. Extraer los datos
Ejecuta el notebook `db_connection.ipynb` el cual se conecta con la base de datos de SQL de Azure y extrae los datos para la actividad como `data.csv`. Guarda el archivo que te genera en la misma carpeta del proyecto.

### 3. Limpieza de datos
Teniendo el archivo `data.csv`, ejecuta el notebook `limpieza_datos.ipynb` el cual va a realizar una limpieza básica de los datos. Este archivo va a generar la base de datos, `data_limpio.csv`, que se utilizará en el modelo y se deberá guardar en la misma carpeta del proyecto.

### 4. Generación del modelo
Teniendo el archivo `data_limpio.csv`, ejecuta el notebook `model.ipynb` el cual va a generar un modelo de Machine Learning para predecir el número de días que transcurrieron entre la fecha más antigua y la fecha del propio registro dada la información de una persona. Este notebook genera `modelo_regresion.sav` que es donde se guarda el modelo.

### 5. Despliegue
Teniendo el archivo `modelo_regresion.sav`, ejecuta el notebook `Deployer.ipynb` el cual va a desplegar el modelo a la nube de Azure. Este notebook generará una URI para poder utilizarlo en una API posteriormente.

### 6. Uso del modelo
Ejecuta el archivo `API.ipynb` para hacer predicciones de los datos que se quieran.

## Qué se necesita
1. Se recomienda una conexión de internet estable
2. Sistema operativo: Windows, macOS o Linux
