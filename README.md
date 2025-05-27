# FARMI-UJAT

Sistema de gestión farmacológica desarrollado con **Flet** para la Universidad Juárez Autónoma de Tabasco.

## 📋 Descripción

FARMI-UJAT es una aplicación que permite la consulta y gestión de información farmacológica, incluyendo fármacos, medicamentos, interacciones y clasificaciones terapéuticas.

## 🚀 Deployment

Ejemplo del *deployment* de una aplicación en **Flet**.

## 🗄️ Base de Datos

Este proyecto incluye una base de datos SQLite (`farmacia_ujat2.db`) que contiene información completa sobre:

### Tablas principales:

#### 📊 Tabla `farmaco`
- **nombre**: Nombre del principio activo (clave primaria)
- **descripcion**: Descripción farmacológica detallada
- **categoria**: Clasificación terapéutica
- **interacciones**: Interacciones medicamentosas conocidas

#### 💊 Tabla `medicamento`
- **id**: Identificador único
- **clave**: Código de clasificación
- **descripcion**: Descripción del medicamento
- **presentacion**: Forma farmacéutica y presentación
- **clasificacion**: Área terapéutica
- **nivel_atencion**: Nivel de atención médica (1er, 2do, 3er nivel)
- **nombre_farmaco**: Referencia al principio activo

### 📈 Estadísticas de la base:
- **+150 fármacos** con información detallada
- **+390 medicamentos** catalogados
- **Múltiples clasificaciones**: Analgesia, Cardiología, Dermatología, Endocrinología, Infectología, Neurología, y más

## 🛠️ Tecnologías

- **Python**: Lenguaje principal
- **Flet**: Framework para aplicaciones multiplataforma
- **SQLite**: Base de datos local
- **DB Browser**: Herramienta de gestión de base de datos

## 📦 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/F4biam20/farmi-ujat.git
   cd farmi-ujat
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```

## 📚 Uso de la Base de Datos

### Con DB Browser for SQLite:
1. Abrir `farmacia_ujat2.db` con DB Browser
2. Explorar las tablas y ejecutar consultas SQL

### Con Python:
```python
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('farmacia_ujat2.db')
cursor = conn.cursor()

# Consultar fármacos por categoría
cursor.execute("SELECT * FROM farmaco WHERE categoria = 'Antibiótico'")
resultados = cursor.fetchall()

conn.close()
```

### Consultas útiles:
```sql
-- Buscar medicamentos por clasificación
SELECT * FROM medicamento WHERE clasificacion = 'Cardiología';

-- Fármacos con interacciones específicas
SELECT nombre, interacciones FROM farmaco WHERE interacciones IS NOT NULL;

-- Medicamentos de primer nivel
SELECT * FROM medicamento WHERE nivel_atencion = '1er Nivel';
```

## 🔍 Funcionalidades

- ✅ Consulta de fármacos por nombre o categoría
- ✅ Búsqueda de medicamentos por clasificación
- ✅ Información de interacciones medicamentosas
- ✅ Filtrado por nivel de atención médica
- ✅ Interfaz intuitiva multiplataforma

## 📱 Deployment

La aplicación está preparada para deployment en múltiples plataformas gracias a Flet:
- **Desktop**: Windows, macOS, Linux
- **Web**: Aplicación web responsiva
- **Mobile**: iOS y Android

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia Apache-2.0. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- **F4biam20** - *Desarrollo inicial* - [F4biam20](https://github.com/F4biam20)

## 🏥 Universidad Juárez Autónoma de Tabasco

Proyecto desarrollado para la gestión farmacológica en el ámbito académico y de investigación.

---

⭐ Si este proyecto te resulta útil, ¡no olvides darle una estrella!
