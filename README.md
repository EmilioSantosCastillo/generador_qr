# 🎨 Generador de Códigos QR Personalizados

Sistema completo de generación de códigos QR con personalización avanzada, diseñado para negocio de llaveros 3D personalizados.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![PyQt6](https://img.shields.io/badge/PyQt6-6.4%2B-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-en%20desarrollo-yellow)

---

## 📋 Descripción

Aplicación de escritorio que permite generar **15 tipos diferentes de códigos QR** (estáticos y dinámicos) con personalización visual avanzada. Incluye backend completo para landing pages multimedia.

### ✨ Características Principales

- 🎯 **15 Tipos de QR**: Desde simples URLs hasta menús de restaurantes complejos
- 🎨 **Personalización Avanzada**: 
  - 16+ marcos decorativos
  - 6 estilos de patrones (cuadrados, círculos, corazones, etc.)
  - Colores sólidos y degradados
  - Personalización de esquinas
  - Logos en el centro
- 📤 **Exportación Múltiple**: SVG vectorial, PNG de alta resolución, PDF
- 🌐 **Landing Pages**: Sistema completo de páginas web responsivas
- 📊 **Historial**: Registro de todos los QR generados
- 👁️ **Preview en Tiempo Real**: Visualización instantánea de cambios

---

## 🔧 Tipos de QR Soportados

### ⚡ Estáticos (sin servidor)
| Tipo | Descripción | Complejidad |
|------|-------------|-------------|
| 🌐 **Sitio Web** | Redirección directa a URL | ⭐ Baja |
| 💬 **WhatsApp** | Mensaje precargado | ⭐ Baja |
| 📶 **Wi-Fi** | Conexión automática a red | ⭐ Baja |

### 🌐 Dinámicos (con landing page)
| Tipo | Descripción | Complejidad |
|------|-------------|-------------|
| 📄 **PDF** | Visor de PDF embebido | ⭐⭐ Media |
| 🔗 **Lista de Enlaces** | Estilo Linktree | ⭐⭐⭐ Alta |
| 👤 **vCard** | Tarjeta de contacto digital | ⭐⭐⭐ Alta |
| 🏢 **Empresa** | Perfil completo de negocio | ⭐⭐⭐⭐ Muy Alta |
| 🎬 **Video** | YouTube, Vimeo o archivo propio | ⭐⭐ Media |
| 🖼️ **Galería de Imágenes** | Múltiples fotos con lightbox | ⭐⭐ Media |
| 📘 **Facebook** | Redirección con diseño temático | ⭐⭐ Media |
| 📷 **Instagram** | Perfil de Instagram | ⭐ Baja |
| 🌐 **Redes Sociales** | Múltiples plataformas (40+) | ⭐⭐ Media |
| 🎵 **MP3/Audio** | Reproductor de audio | ⭐⭐ Media |
| 🍽️ **Menú Restaurante** | Menú por secciones con alérgenos | ⭐⭐⭐⭐ Muy Alta |
| 🎟️ **Cupón** | Descuentos con código de barras | ⭐⭐ Media |

---

## 🏗️ Arquitectura
```
┌─────────────────────────────────────┐
│   Aplicación Desktop (PyQt6)        │
│   - Interfaz gráfica                │
│   - Generación local de QR          │
│   - Personalización visual          │
│   - Exportación de archivos         │
└──────────────┬──────────────────────┘
               │ HTTP REST API
┌──────────────▼──────────────────────┐
│   Backend API (Flask)               │
│   - Gestión de QR dinámicos         │
│   - Procesamiento de archivos       │
│   - Landing pages                   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Base de Datos (MySQL/PostgreSQL)  │
│   - Configuraciones de QR           │
│   - Metadata de archivos            │
│   - Estadísticas de escaneos        │
└─────────────────────────────────────┘
```

---

## 🚀 Stack Tecnológico

### Desktop Application
- **Python** 3.10+
- **PyQt6** 6.4+ - Framework GUI
- **Segno** 1.5+ - Generación de QR
- **Pillow** 9.5+ - Procesamiento de imágenes
- **Requests** 2.31+ - Cliente HTTP
- **ReportLab** 4.0+ - Exportación PDF

### Backend
- **Flask** 2.3+ - Framework web
- **SQLAlchemy** 2.0+ - ORM
- **MySQL/PostgreSQL** - Base de datos
- **Nginx/Gunicorn** - Servidor de producción

### Frontend (Landing Pages)
- **HTML5 / CSS3 / JavaScript**
- **Bootstrap 5** o **Tailwind CSS**
- Responsive design

---

## 📦 Instalación

### Requisitos Previos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/qr-generator.git
cd qr-generator
```

### Paso 2: Crear Entorno Virtual
```bash
python -m venv venv
```

### Paso 3: Activar Entorno Virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Paso 4: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 5: Configurar Variables de Entorno
```bash
copy .env.example .env
# Editar .env con tus configuraciones
```

### Paso 6: Ejecutar la Aplicación
```bash
python main.py
```

---

## 🎨 Personalización del QR

### Marcos Decorativos
- Sin marco
- "Scan Me" (superior, inferior, completo)
- Esquinas redondeadas
- Con iconos (cámara, smartphone, email)
- Y 10+ estilos adicionales

### Patrones de Módulos
- Cuadrados estándar
- Cuadrados redondeados
- Círculos grandes
- Flores/cruces
- Corazones ❤️
- Puntos pixelados

### Colores
- **Colores sólidos**: Cualquier color hexadecimal
- **Degradados lineales**: Dos colores con dirección configurable
- **Fondo transparente**: Para impresión sobre superficies de color

### Esquinas Personalizadas
- **Marco exterior**: 6 estilos (círculo, cuadrado, outline, etc.)
- **Punto central**: 7 estilos (puntos y cuadrados de diferentes tamaños)
- Colores independientes para cada elemento

### Logo en el Centro
- Sube tu logo (JPG, PNG, SVG)
- Tamaño automático optimizado
- Ajuste automático de nivel de corrección de errores

---

## 📁 Estructura del Proyecto
```
qr-generator/
├── main.py                 # Punto de entrada
├── requirements.txt        # Dependencias
├── config.py              # Configuraciones
├── .env                   # Variables de entorno
│
├── ui/                    # Interfaz gráfica
│   ├── main_window.py
│   ├── tab_manager.py
│   ├── preview_widget.py
│   ├── customization_panel.py
│   └── tabs/             # Pestañas por tipo de QR
│       ├── url_tab.py
│       ├── pdf_tab.py
│       └── ...
│
├── core/                  # Lógica de negocio
│   ├── qr_generator.py
│   ├── qr_customizer.py
│   ├── qr_exporter.py
│   └── types/            # Clases por tipo de QR
│       ├── base_qr_type.py
│       └── ...
│
├── api/                   # Cliente API
│   ├── api_client.py
│   └── endpoints.py
│
├── utils/                 # Utilidades
│   ├── validators.py
│   ├── formatters.py
│   └── image_processor.py
│
├── resources/             # Recursos estáticos
│   ├── icons/
│   ├── presets/
│   └── frames/
│
└── storage/              # Almacenamiento local
    ├── history.json
    └── exports/
```

---

## 🔌 API Backend

### Endpoints Principales

#### Crear QR Dinámico
```http
POST /api/qr/create
Content-Type: application/json

{
  "type": "pdf",
  "config": {
    "title": "Mi PDF",
    "description": "...",
    ...
  }
}
```

#### Subir Archivo
```http
POST /api/files/upload
Content-Type: multipart/form-data

file: [binary data]
type: "pdf" | "image" | "video" | "audio"
```

#### Ver Landing Page
```http
GET /qr/{slug}
```

Ver documentación completa de API en `/docs/API.md`

---

## 📊 Base de Datos

### Tablas Principales

**qr_codes**
- Almacena configuración de todos los QR
- Campo JSON para flexibilidad
- Estadísticas de escaneos

**files**
- Metadata de archivos multimedia
- Rutas y metadatos (tamaño, tipo, etc.)

**analytics** (opcional)
- Registro detallado de escaneos
- Geolocalización
- Información de dispositivo

---

## 🗺️ Roadmap

### ✅ Fase 1: Fundamentos (Semanas 1-2)
- [x] Estructura del proyecto
- [ ] QR estáticos (URL, WhatsApp, WiFi)
- [ ] Personalización básica
- [ ] Exportación SVG/PNG

### 🔄 Fase 2: Backend y QR Dinámicos Básicos (Semanas 3-4)
- [ ] Backend Flask
- [ ] Base de datos
- [ ] Tipos: PDF y Video
- [ ] Comunicación app ↔ backend

### ⏳ Fase 3: Más Tipos Dinámicos (Semanas 5-6)
- [ ] Lista Enlaces, vCard, Imágenes
- [ ] MP3, Facebook, Instagram, Redes Sociales
- [ ] Personalización avanzada

### ⏳ Fase 4: Tipos Complejos (Semanas 7-8)
- [ ] Menú, Empresa, Cupón
- [ ] Exportación PDF
- [ ] Optimizaciones

### ⏳ Fase 5: Pulido (Semanas 9-10)
- [ ] Historial
- [ ] Mejoras UI/UX
- [ ] Deployment
- [ ] Documentación

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 👤 Autor

**Tu Nombre**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: tu-email@ejemplo.com

---

## 🙏 Agradecimientos

- [Segno](https://github.com/heuer/segno) - Librería de generación de QR
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) - Framework GUI
- [Flask](https://flask.palletsprojects.com/) - Framework web

---

## 📸 Screenshots

*(Aquí irán capturas de pantalla cuando la aplicación esté desarrollada)*

### Interfaz Principal
![Interfaz Principal](screenshots/main-interface.png)

### Personalización del QR
![Personalización](screenshots/customization.png)

### Landing Page Ejemplo
![Landing Page](screenshots/landing-page.png)

---

**Versión:** 1.0.0  
**Estado:** 🚧 En desarrollo activo  
**Última actualización:** Octubre 2025
