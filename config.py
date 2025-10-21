"""
Configuración global de la aplicación Generador de QR
"""

import os
from pathlib import Path

# ============================================================================
# RUTAS DEL PROYECTO
# ============================================================================

# Directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Directorios principales
UI_DIR = BASE_DIR / "ui"
CORE_DIR = BASE_DIR / "core"
API_DIR = BASE_DIR / "api"
UTILS_DIR = BASE_DIR / "utils"
RESOURCES_DIR = BASE_DIR / "resources"
STORAGE_DIR = BASE_DIR / "storage"

# Subdirectorios de resources
ICONS_DIR = RESOURCES_DIR / "icons"
PRESETS_DIR = RESOURCES_DIR / "presets"
FRAMES_DIR = RESOURCES_DIR / "frames"
SOCIAL_ICONS_DIR = RESOURCES_DIR / "social_icons"

# Subdirectorios de storage
CACHE_DIR = STORAGE_DIR / "cache"
EXPORTS_DIR = STORAGE_DIR / "exports"
HISTORY_FILE = STORAGE_DIR / "history.json"

# ============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ============================================================================

APP_NAME = "Generador de Códigos QR"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Tu Nombre"
APP_ORGANIZATION = "Tu Organización"

# Dimensiones de la ventana principal
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 700

# ============================================================================
# CONFIGURACIÓN DE QR
# ============================================================================

# Niveles de corrección de errores
ERROR_CORRECTION_LEVELS = {
    "L": "Low (7%)",      # Recupera hasta 7% de datos dañados
    "M": "Medium (15%)",  # Recupera hasta 15% de datos dañados
    "Q": "Quartile (25%)",  # Recupera hasta 25% de datos dañados (recomendado con logo)
    "H": "High (30%)"     # Recupera hasta 30% de datos dañados
}

DEFAULT_ERROR_CORRECTION = "Q"

# Tamaños de exportación (escala)
EXPORT_SCALES = {
    "small": 5,
    "medium": 10,
    "large": 15,
    "xlarge": 20
}

DEFAULT_EXPORT_SCALE = 10

# DPI para exportación PNG
EXPORT_DPI = 300

# ============================================================================
# TIPOS DE QR SOPORTADOS
# ============================================================================

QR_TYPES = {
    "url": {
        "name": "Sitio Web / URL",
        "icon": "🌐",
        "static": True,
        "complexity": 1
    },
    "whatsapp": {
        "name": "WhatsApp",
        "icon": "💬",
        "static": True,
        "complexity": 1
    },
    "wifi": {
        "name": "Wi-Fi",
        "icon": "📶",
        "static": True,
        "complexity": 1
    },
    "pdf": {
        "name": "PDF",
        "icon": "📄",
        "static": False,
        "complexity": 2
    },
    "link_list": {
        "name": "Lista de Enlaces",
        "icon": "🔗",
        "static": False,
        "complexity": 3
    },
    "vcard": {
        "name": "vCard (Contacto)",
        "icon": "👤",
        "static": False,
        "complexity": 3
    },
    "business": {
        "name": "Empresa",
        "icon": "🏢",
        "static": False,
        "complexity": 4
    },
    "video": {
        "name": "Video",
        "icon": "🎬",
        "static": False,
        "complexity": 2
    },
    "images": {
        "name": "Galería de Imágenes",
        "icon": "🖼️",
        "static": False,
        "complexity": 2
    },
    "facebook": {
        "name": "Facebook",
        "icon": "📘",
        "static": False,
        "complexity": 2
    },
    "instagram": {
        "name": "Instagram",
        "icon": "📷",
        "static": False,
        "complexity": 1
    },
    "social": {
        "name": "Redes Sociales",
        "icon": "🌐",
        "static": False,
        "complexity": 2
    },
    "mp3": {
        "name": "MP3 / Audio",
        "icon": "🎵",
        "static": False,
        "complexity": 2
    },
    "menu": {
        "name": "Menú de Restaurante",
        "icon": "🍽️",
        "static": False,
        "complexity": 4
    },
    "coupon": {
        "name": "Cupón",
        "icon": "🎟️",
        "static": False,
        "complexity": 2
    }
}

# ============================================================================
# PERSONALIZACIÓN DEL QR
# ============================================================================

# Patrones de módulos disponibles
QR_PATTERNS = [
    "cuadrados",        # Cuadrados estándar
    "redondeados",      # Cuadrados con bordes redondeados
    "circulos",         # Círculos grandes
    "flores",           # Patrón de flores/cruces
    "corazones",        # Corazones
    "puntos"            # Puntos pequeños
]

DEFAULT_QR_PATTERN = "cuadrados"

# Estilos de marcos de esquinas
CORNER_FRAME_STYLES = [
    "none",                 # Sin forma especial
    "circle",               # Círculo
    "square_outline",       # Cuadrado con borde
    "square_solid",         # Cuadrado relleno
    "small_square_outline", # Cuadrado pequeño con borde
    "small_square_solid"    # Cuadrado pequeño relleno
]

# Estilos de puntos centrales de esquinas
CORNER_DOT_STYLES = [
    "none",           # Sin forma especial
    "dot_small",      # Punto pequeño
    "square_small",   # Cuadrado pequeño
    "square_medium",  # Cuadrado mediano
    "diamond",        # Rombo/diamante
    "dot_medium",     # Punto mediano
    "dot_large"       # Punto grande
]

# Colores predefinidos
DEFAULT_QR_COLOR = "#000000"  # Negro
DEFAULT_BG_COLOR = "#FFFFFF"  # Blanco

# ============================================================================
# PALETAS DE COLORES PREDEFINIDAS
# ============================================================================

COLOR_PALETTES = {
    "classic": {
        "name": "Clásico",
        "primary": "#000000",
        "secondary": "#FFFFFF"
    },
    "ocean": {
        "name": "Océano",
        "primary": "#006994",
        "secondary": "#00D4FF"
    },
    "forest": {
        "name": "Bosque",
        "primary": "#2D5016",
        "secondary": "#7EC09F"
    },
    "sunset": {
        "name": "Atardecer",
        "primary": "#FF6B35",
        "secondary": "#F7F052"
    },
    "lavender": {
        "name": "Lavanda",
        "primary": "#667eea",
        "secondary": "#764ba2"
    },
    "fire": {
        "name": "Fuego",
        "primary": "#ED213A",
        "secondary": "#93291E"
    },
    "mint": {
        "name": "Menta",
        "primary": "#00b09b",
        "secondary": "#96c93d"
    },
    "royal": {
        "name": "Real",
        "primary": "#141E30",
        "secondary": "#243B55"
    },
    "cherry": {
        "name": "Cereza",
        "primary": "#EB3349",
        "secondary": "#F45C43"
    }
}

# ============================================================================
# CONFIGURACIÓN DE API (Backend)
# ============================================================================

# URL del backend (cambiar en producción)
API_BASE_URL = "http://localhost:5000"

# Endpoints
API_ENDPOINTS = {
    "create_qr": "/api/qr/create",
    "upload_file": "/api/files/upload",
    "get_qr": "/api/qr/{slug}",
    "update_qr": "/api/qr/{slug}",
    "delete_qr": "/api/qr/{slug}",
    "list_qr": "/api/qr/list"
}

# Timeout para peticiones HTTP (segundos)
API_TIMEOUT = 30

# ============================================================================
# LÍMITES DE ARCHIVOS
# ============================================================================

FILE_SIZE_LIMITS = {
    "pdf": 100 * 1024 * 1024,      # 100 MB
    "image": 10 * 1024 * 1024,     # 10 MB
    "video": 250 * 1024 * 1024,    # 250 MB
    "audio": 25 * 1024 * 1024,     # 25 MB
    "logo": 1 * 1024 * 1024        # 1 MB
}

# Formatos permitidos
ALLOWED_FORMATS = {
    "pdf": [".pdf"],
    "image": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "video": [".mp4", ".webm", ".mov", ".avi"],
    "audio": [".mp3", ".wav", ".m4a", ".ogg"],
    "logo": [".jpg", ".jpeg", ".png", ".svg"]
}

# ============================================================================
# CONFIGURACIÓN DE REDES SOCIALES
# ============================================================================

# Plataformas de redes sociales soportadas (40+)
SOCIAL_NETWORKS = [
    "instagram", "facebook", "twitter", "linkedin", "tiktok",
    "youtube", "spotify", "soundcloud", "apple_music",
    "github", "dribbble", "behance",
    "whatsapp", "telegram", "messenger",
    "pinterest", "reddit", "tumblr", "flickr",
    "snapchat", "discord", "twitch",
    "patreon", "ko-fi", "paypal",
    "medium", "substack", "dev_to",
    "vimeo", "dailymotion",
    "etsy", "amazon", "ebay",
    "yelp", "tripadvisor",
    "slack", "teams",
    "clubhouse", "mastodon",
    "website", "email", "phone"
]

# ============================================================================
# CONFIGURACIÓN DE MENÚ (Restaurante)
# ============================================================================

# Alérgenos disponibles
ALLERGENS = {
    "gluten": {"name": "Gluten", "icon": "🌾"},
    "crustaceans": {"name": "Crustáceos", "icon": "🦐"},
    "eggs": {"name": "Huevos", "icon": "🥚"},
    "fish": {"name": "Pescado", "icon": "🐟"},
    "peanuts": {"name": "Cacahuetes", "icon": "🥜"},
    "soy": {"name": "Soja", "icon": "🫘"},
    "dairy": {"name": "Lácteos", "icon": "🥛"},
    "nuts": {"name": "Frutos secos", "icon": "🌰"},
    "celery": {"name": "Apio", "icon": "🥬"},
    "mustard": {"name": "Mostaza", "icon": "🟡"},
    "sesame": {"name": "Sésamo", "icon": "⚪"},
    "sulfites": {"name": "Sulfitos", "icon": "🍷"},
    "lupins": {"name": "Altramuces", "icon": "🫘"},
    "molluscs": {"name": "Moluscos", "icon": "🦪"},
    "spicy": {"name": "Picante", "icon": "🌶️"},
    "vegetarian": {"name": "Vegetariano", "icon": "🥬"},
    "vegan": {"name": "Vegano", "icon": "🌱"},
    "gluten_free": {"name": "Sin gluten", "icon": "🚫🌾"},
    "lactose_free": {"name": "Sin lactosa", "icon": "🚫🥛"}
}

# ============================================================================
# CONFIGURACIÓN DE DESARROLLO
# ============================================================================

# Modo de desarrollo
DEBUG_MODE = True

# Logging
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def get_qr_types_by_category():
    """Retorna tipos de QR agrupados por categoría (estáticos/dinámicos)"""
    static = {k: v for k, v in QR_TYPES.items() if v["static"]}
    dynamic = {k: v for k, v in QR_TYPES.items() if not v["static"]}
    return {"static": static, "dynamic": dynamic}


def get_file_size_limit_mb(file_type):
    """Retorna el límite de tamaño en MB para un tipo de archivo"""
    bytes_limit = FILE_SIZE_LIMITS.get(file_type, 0)
    return bytes_limit / (1024 * 1024)


def is_file_allowed(filename, file_type):
    """Verifica si un archivo tiene una extensión permitida"""
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_FORMATS.get(file_type, [])


def ensure_directories():
    """Crea todos los directorios necesarios si no existen"""
    directories = [
        UI_DIR, CORE_DIR, API_DIR, UTILS_DIR, RESOURCES_DIR, STORAGE_DIR,
        ICONS_DIR, PRESETS_DIR, FRAMES_DIR, SOCIAL_ICONS_DIR,
        CACHE_DIR, EXPORTS_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


# Crear directorios al importar el módulo
ensure_directories()


if __name__ == "__main__":
    # Test de configuración
    print(f"Aplicación: {APP_NAME} v{APP_VERSION}")
    print(f"Directorio base: {BASE_DIR}")
    print(f"\nTipos de QR disponibles: {len(QR_TYPES)}")
    
    categorized = get_qr_types_by_category()
    print(f"  - Estáticos: {len(categorized['static'])}")
    print(f"  - Dinámicos: {len(categorized['dynamic'])}")
    
    print(f"\nPaletas de colores: {len(COLOR_PALETTES)}")
    print(f"Redes sociales soportadas: {len(SOCIAL_NETWORKS)}")
    print(f"Alérgenos disponibles: {len(ALLERGENS)}")
    
    print("\nDirectorios creados correctamente ✓")