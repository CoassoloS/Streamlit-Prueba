FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema (opcional, para algunas librerías)
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la app
COPY . .

# Puerto expuesto (por defecto Streamlit usa 8501)
EXPOSE 8501

# Comando para iniciar la app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
