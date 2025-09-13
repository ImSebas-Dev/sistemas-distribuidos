import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL objetivo
url = "https://www.inducascos.com/cascos/integrales"

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
names, links, prices_now, prices_old, discounts = [], [], [], [], []

for quote_block in soup.find_all("section", class_="vtex-product-summary-2-x-container"):
    try:
        text = quote_block.find("div", class_="vtex-product-summary-2-x-nameContainer").text.strip()
        link = quote_block.find("a", class_="vtex-product-summary-2-x-clearLink")["href"].strip()
        price = quote_block.find("span", class_="vtex-product-price-1-x-sellingPrice").text.strip()
        price_old = quote_block.find("span", class_="vtex-product-price-1-x-listPrice")
        discount = quote_block.find("div", class_="vtex-store-components-3-x-discountInsideContainer")

        # Manejo de valores faltantes
        price_old = price_old.text.strip() if price_old else "N/A"
        discount = discount.text.strip() if discount else "N/A"

        names.append(text)
        links.append(link)
        prices_now.append(price)
        prices_old.append(price_old)
        discounts.append(discount)

    except AttributeError as e:
        print(f"⚠️ Error extrayendo un producto: {e}")
        continue

# Verificar si se extrajo algo
if not names:
    print("⚠️ No se encontraron productos en la página.")
    exit()

# Crear DataFrame
try:
    df = pd.DataFrame({
        "Nombre": names,
        "Link": links,
        "Precio": prices_now,
        "Precio Anterior": prices_old,
        "Descuento": discounts
    })
except Exception as e:
    print(f"❌ Error al crear el DataFrame: {e}")
    exit()

# Guardar en Excel
try:
    df.to_excel("resultados.xlsx", index=False)
    print("✅ Datos exportados a resultados.xlsx")
except Exception as e:
    print(f"❌ Error al guardar el archivo Excel: {e}")