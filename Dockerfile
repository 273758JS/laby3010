# Użyj oficjalnego obrazu z Pythonem
FROM python

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki aplikacji i wymagań
COPY app.py .
COPY requirements.txt .


# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Wystaw port
EXPOSE 3000

# Uruchom aplikację
CMD ["python", "app.py"]