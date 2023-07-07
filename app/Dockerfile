FROM python:3.10
# versión en la que va a ejecutar el archivo

WORKDIR /app
# espacio de trabajo cualquier nombre, aquí es app

COPY requirements.txt /app/requirements.txt
# Copiando el archivo local al container, el lado izquierdo es el local y el derecho es del contenedor

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Aquí dejamos listas las dependencias:
# pip: No se indica pip3 porque ya ejecutaremos python
# install -r /app/requirements.txt: Se instalan las dependencias
# --no-cache-dir: que no aplique el caché
# --upgrade: para que considere cualquier actualización del gestor de paquetes

COPY . /app
# Copiamos todo el código (por eso el "." = todo) mismo principio que el COPY anterior

CMD bash -c "while true; do sleep 1; done"
# para mantener en ejecución constante el contenedor, es decir siempre encendido