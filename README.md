# 🏛️ Mythologia API

API REST desarrollada con **Flask** que permite consultar información sobre seres mitológicos del mundo. Incluye dioses, criaturas y héroes de más de 20 mitologías distintas.

---

## 📁 Estructura del proyecto

```
mythologia-api/
│
├── app.py                      # Punto de entrada de la aplicación
├── api_routes.py               # Blueprint con todos los endpoints
├── funciones.py                # Utilidades (normalización de texto)
├── requirements.txt            # Dependencias del proyecto
│
├── data/
│   └── seres_mitologicos.csv   # Dataset con 250 seres mitológicos
│
└── templates/
    └── index.html              # Documentación visual de la API
```

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/mythologia-api.git
cd mythologia-api
```

### 2. Crear entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

La API estará disponible en `http://localhost:5000`

---

## 📡 Endpoints

**Base URL:** `http://localhost:5000/api/v1`

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/all` | Retorna todos los seres mitológicos |
| `GET` | `/id/<id>` | Busca un ser por su ID |
| `GET` | `/mitologia/<mitologia>` | Filtra por mitología |
| `GET` | `/tipo/<tipo>` | Filtra por tipo de ser |
| `GET` | `/nombre/<nombre>` | Busca por nombre exacto |
| `GET` | `/origen/<origen>` | Filtra por región de origen |

### Ejemplos de uso

```bash
# Todos los seres
GET /api/v1/all

# Buscar por ID
GET /api/v1/id/1

# Filtrar por mitología
GET /api/v1/mitologia/griega
GET /api/v1/mitologia/nordica

# Filtrar por tipo
GET /api/v1/tipo/dios
GET /api/v1/tipo/criatura
GET /api/v1/tipo/heroe

# Buscar por nombre
GET /api/v1/nombre/zeus
GET /api/v1/nombre/thor

# Filtrar por origen
GET /api/v1/origen/mediterraneo
GET /api/v1/origen/escandinavia
GET /api/v1/origen/mesoamerica
```

---

## 📦 Estructura de la respuesta

Cada ser mitológico retorna un objeto JSON con los siguientes campos:

```json
[
  {
    "id": "1",
    "Nombre": "Zeus",
    "Origen": "Mediterráneo",
    "Mitologia": "Griega",
    "Tipo": "Dios",
    "Descripcion": "Rey del Olimpo y dios del cielo y el trueno",
    "Poderes": "Control del rayo y el trueno; control del clima; metamorfosis; inmortalidad",
    "Lore": "Zeus nació hijo de los titanes Cronos y Rea..."
  }
]
```

### Campos disponibles

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | Identificador único (1–250) |
| `Nombre` | string | Nombre del ser mitológico |
| `Origen` | string | Región geográfica de origen |
| `Mitologia` | string | Cultura o tradición mitológica |
| `Tipo` | string | Clasificación del ser |
| `Descripcion` | string | Descripción breve |
| `Poderes` | string | Poderes separados por `;` |
| `Lore` | string | Historia o lore detallado |

---

## 🔎 Normalización de texto

Todos los endpoints utilizan la función `normalice_text()` para comparar parámetros, lo que significa que las búsquedas **ignoran tildes y mayúsculas**.

```python
# Estos tres son equivalentes:
GET /api/v1/mitologia/Nórdica
GET /api/v1/mitologia/nordica
GET /api/v1/mitologia/NORDICA
```

---

## 🗂️ Valores disponibles por campo

### Mitologías
`Griega` · `Nórdica` · `Egipcia` · `Hindú` · `Japonesa` · `China` · `Azteca` · `Maya` · `Romana` · `Celta` · `Sumeria` · `Babilónica` · `Cananea` · `Yoruba` · `Africana` · `Polinesio` · `Hawaiana` · `Maorí` · `Judeo-cristiana` · `Árabe` · `Persa` · `Asiria` · `Filipina` · `Latinoamericana` · `Brasileña` · `Andina` · `Inca` · `Chilena` · `Amazónica` · `Universal`

### Tipos
`Dios` · `Diosa` · `Héroe` · `Criatura` · `Titán` · `Hechicera`

### Orígenes
`Mediterráneo` · `Escandinavia` · `Norte de África` · `Asia del Sur` · `Asia Oriental` · `Mesoamérica` · `América del Sur` · `América del Norte` · `América Latina` · `Medio Oriente` · `Oceanía` · `Europa` · `África Occidental` · `África del Sur`

---

## ⚠️ Manejo de errores

Si se accede a una ruta no definida la API responde con:

```json
{
  "error": "Ruta no encontrada"
}
```

**Código HTTP:** `404`

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Flask 3.1.3** — framework web
- **CSV** — almacenamiento de datos (librería estándar)
- **unicodedata** — normalización de texto (librería estándar)
- **Bootstrap 5** — interfaz de documentación

---

## 📋 Dependencias

```
Flask==3.1.3
blinker==1.9.0
click==8.3.1
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
Werkzeug==3.1.6
```

---

## 📊 Dataset

El archivo `data/seres_mitologicos.csv` contiene **250 seres mitológicos** de más de 20 culturas del mundo. No requiere base de datos: los datos se cargan en memoria al iniciar la aplicación.

---

## 📄 Licencia

Este proyecto es de uso libre con fines educativos y de práctica.
