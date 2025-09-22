import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL objetivo
url = "https://www.nihonfigures.com/c880420_figuras-articuladas.html"

try:
    # Obtener contenido HTML
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Lanza error si el código HTTP no es 200
except requests.exceptions.RequestException as e:
    print(f"❌ Error al hacer la petición: {e}")
    exit()

try:
    soup = BeautifulSoup(response.text, "html.parser")
except Exception as e:
    print(f"❌ Error al procesar el HTML: {e}")
    exit()

# Extraer datos
prices_now = []
prices_old = []
descriptions = []

for quote_block in soup.find_all("article", class_="panel"):
    try:
        price_now = quote_block.find("span", class_="precio-final")
        price_now = price_now.get_text().strip() if price_now else "N/A"

        price_old = quote_block.find("span", class_="strike")
        price_old = price_old.get_text().strip() if price_old else "N/A"

        description_block = quote_block.find("div", class_="product-description")
        if description_block:
            items = description_block.find_all("li")
            description = "\n".join([li.get_text(strip=True) for li in items])
        else:
            description = "N/A"

        prices_now.append(price_now)
        prices_old.append(price_old)
        descriptions.append(description)

    except AttributeError as e:
        print(f"⚠️ Error extrayendo un producto: {e}")
        continue

# Verificar si se extrajo algo
#if not names:
#    print("⚠️ No se encontraron productos en la página.")
#    exit()

# Crear DataFrame
try:
    df = pd.DataFrame({
        "Precio": prices_now,
        "Precio sin Descuento": prices_old,
        "Descripción": descriptions
    })
except Exception as e:
    print(f"❌ Error al crear el DataFrame: {e}")
    exit()

# Guardar en Excel
try:
    df.to_excel("prueba.xlsx", index=False)
    print("✅ Datos exportados a prueba.xlsx")
except Exception as e:
    print(f"❌ Error al guardar el archivo Excel: {e}")