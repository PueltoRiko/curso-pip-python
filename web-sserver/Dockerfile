FROM python:3.10

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
# lista de instrucciones:
# lanzar el servidor uvicorn es quien mantiene encendido el servidor en FastAPI
# ingresa a la aplicación main:app
# ponemos el host que es el 0.0.0.0
# indicamos el puerto en el que va a correr (80 usualmente)