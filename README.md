# fiuba_opiniones_de_curso

![badge](https://travis-ci.org/Arkenan/fiuba_opiniones_de_curso.svg?branch=master)

Sistema web para visualizar cómodamente las opiniones sobre cursos de la Facultad de Ingeniería de la UBA. Por el momento, utilizando como base las encuestas del Departamento de Computación.

## Prerrequisitos

Software de base:
- Linux (probado en ubuntu 18.04).
- Python (probado en python 3.6.8).
- Pip (probado con pip3).

## Instalación

Tanto para los tests como para el servidor se requieren paquetes de python tales como flask. Estos se encuentran listados en `requirements.txt`. Para instalarlos, ejecutar en bash:

```bash
sudo -H pip3 install -r requirements.txt
```

Para darle permisos a los scripts de ejecución de test y de servidor, ejecutar desde la raíz del proyecto:

```bash
chmod +x run
chmod +x test
```

## Levantar el servidor

Para levantar el servidor que expone la página web de opiniones de curso debe ejecutarse en bash:

```bash
./run
```

desde la raíz del proyecto. Este script exporta la raíz al `PYTHONPATH` y luego levanta el server de flask.

Para acceder al servidor, debe entrarse en el navegador a `http://localhost:5000`.

## Ejecutar tests locales:

Ejecutar el script

```bash
./test
```

que llama a `pytest` modificando el `PYTHONPATH` para incluir a la raíz del proyecto.
