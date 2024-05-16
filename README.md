
# Dependencias

![PyQt6](https://img.shields.io/badge/PyQt6-6.7.0-blue)
![PyQt6-Qt6](https://img.shields.io/badge/PyQt6--Qt6-6.7.0-blue)
![PyQt6-sip](https://img.shields.io/badge/PyQt6--sip-13.6.0-blue)
![pyserial](https://img.shields.io/badge/pyserial-3.5-blue)

# Instalación de Dependencias

Para instalar todas las dependencias necesarias para este proyecto, puedes utilizar el archivo `requirements.txt`. Primero, asegúrate de tener Python y pip instalados en tu sistema. Luego, sigue estos pasos:

1. Abre una terminal o línea de comandos en el directorio de tu proyecto.

2. Ejecuta el siguiente comando para instalar las dependencias desde el archivo `requirements.txt`:

`pip install -r requirements.txt`

# Uso del script leer_censor.py

<!-- Introducción -->
Para usar el script `leer_censor.py` en Arduino como ejemplo, primero necesitas generar datos simulados del sensor para enviarlos por el puerto serie. Puedes hacerlo con el siguiente código en Arduino:

    void setup() {
      Serial.begin(9600); // Inicializar la comunicación serial a 9600 baudios
    }
    
    void loop() {
      // Generar datos aleatorios de temperatura y humedad
      float temperatura = random(10, 40); // Temperatura entre 10°C y 40°C
      float humedad = random(30, 70);     // Humedad entre 30% y 70%
    
      // Enviar los datos por el puerto serie
      Serial.print(temperatura);
      Serial.print(",");
      Serial.println(humedad);
    
      // Esperar un breve periodo antes de volver a enviar los datos
      delay(2000);
    }
Se recomienda usar el siguiente código en Arduino para leer datos del sensor DHT11:

    #include <DHT.h>
    
    #define DHTPIN 2      // Pin donde está conectado el sensor DHT11
    #define DHTTYPE DHT11 // Tipo de sensor DHT que estás utilizando
    
    DHT dht(DHTPIN, DHTTYPE);
    
    void setup() {
      Serial.begin(9600); // Inicializar la comunicación serial a 9600 baudios
      dht.begin();        // Inicializar el sensor DHT11
    }
    
    void loop() {
      // Leer la temperatura y humedad del sensor
      float temperatura = dht.readTemperature();
      float humedad = dht.readHumidity();
    
      // Enviar los datos por el puerto serie
      Serial.print(temperatura);
      Serial.print(",");
      Serial.println(humedad);
    
      // Esperar un breve periodo antes de volver a leer los datos
      delay(2000);
    }
    

# Explicacion

Este código simula la lectura de un sensor generando datos aleatorios de temperatura y humedad y enviándolos por el puerto serie a una velocidad de 9600 baudios.
#Reemplazo de datos reales

Para simular datos reales del sensor en lugar de datos aleatorios, deberás reemplazar este código con el código necesario para leer los datos del sensor real y enviarlos por el puerto serie.

Una vez que hayas configurado Arduino para enviar datos por el puerto serie, puedes utilizar el script leer_censor.py para leer y procesar estos datos en tu computadora.

[========]

## Uso de leer_csv.py o leer_json.py

Para utilizar los scripts `leer_csv.py` o `leer_json.py`, en el directorio `data` se encuentran ejemplos de archivos que puedes utilizar para leer los datos. 
Puedes usar la ruta  absoluta o local.


