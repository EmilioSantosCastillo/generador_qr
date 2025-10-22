"""
Generador de Códigos QR
Módulo principal para la generación de códigos QR con segno
"""

import segno
from io import BytesIO
from PIL import Image

import config


class QRGenerator:
    """
    Clase para generar códigos QR con diferentes configuraciones
    """
    
    def __init__(self, error_correction='Q'):
        """
        Inicializar el generador
        
        Args:
            error_correction: Nivel de corrección de errores (L, M, Q, H)
        """
        self.error_correction = error_correction
        
    def generate(self, content, scale=10):
        """
        Genera un código QR básico
        
        Args:
            content: Contenido del QR (URL, texto, etc.)
            scale: Escala del QR (tamaño de cada módulo)
            
        Returns:
            PIL.Image: Imagen del QR generado
        """
        # Crear QR con segno
        qr = segno.make(
            content,
            error=self.error_correction,
            boost_error=False
        )
        
        # Convertir a imagen PIL
        buffer = BytesIO()
        qr.save(buffer, kind='png', scale=scale)
        buffer.seek(0)
        
        image = Image.open(buffer)
        
        return image
    
    def generate_url(self, url, scale=10):
        """
        Genera un QR para una URL
        
        Args:
            url: URL destino
            scale: Escala del QR
            
        Returns:
            PIL.Image: Imagen del QR
        """
        return self.generate(url, scale)
    
    def generate_wifi(self, ssid, password, encryption='WPA', hidden=False, scale=10):
        """
        Genera un QR para conexión WiFi
        
        Args:
            ssid: Nombre de la red
            password: Contraseña
            encryption: Tipo de cifrado (WPA, WEP, nopass)
            hidden: Si la red está oculta
            scale: Escala del QR
            
        Returns:
            PIL.Image: Imagen del QR
        """
        # Formato WiFi QR
        hidden_str = "true" if hidden else "false"
        
        if encryption == "nopass":
            wifi_string = f"WIFI:T:nopass;S:{ssid};P:;H:{hidden_str};;"
        else:
            wifi_string = f"WIFI:T:{encryption};S:{ssid};P:{password};H:{hidden_str};;"
        
        return self.generate(wifi_string, scale)
    
    def generate_whatsapp(self, phone, message="", scale=10):
        """
        Genera un QR para WhatsApp
        
        Args:
            phone: Número de teléfono (con código de país, sin +)
            message: Mensaje precargado (opcional)
            scale: Escala del QR
            
        Returns:
            PIL.Image: Imagen del QR
        """
        # Formato WhatsApp
        if message:
            # URL encode del mensaje
            import urllib.parse
            message_encoded = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{phone}?text={message_encoded}"
        else:
            whatsapp_url = f"https://wa.me/{phone}"
        
        return self.generate(whatsapp_url, scale)
    
    def get_qr_info(self, content):
        """
        Obtiene información sobre un QR sin generarlo
        
        Args:
            content: Contenido del QR
            
        Returns:
            dict: Información del QR (versión, módulos, etc.)
        """
        qr = segno.make(content, error=self.error_correction)
        
        return {
            'version': qr.version,
            'error_correction': self.error_correction,
            'mode': qr.mode,
            'modules': qr.symbol_size()[0]  # Tamaño en módulos (ancho = alto)
        }


def test_generator():
    """Función de prueba del generador"""
    print("🧪 Probando generador de QR...\n")
    
    generator = QRGenerator()
    
    # Test 1: URL simple
    print("✅ Test 1: Generando QR de URL")
    qr_image = generator.generate_url("https://www.example.com")
    print(f"   Tamaño: {qr_image.size}")
    
    # Test 2: WiFi
    print("✅ Test 2: Generando QR de WiFi")
    qr_wifi = generator.generate_wifi("MiRedWiFi", "micontraseña123", "WPA")
    print(f"   Tamaño: {qr_wifi.size}")
    
    # Test 3: WhatsApp
    print("✅ Test 3: Generando QR de WhatsApp")
    qr_whatsapp = generator.generate_whatsapp("56912345678", "Hola, quiero más información")
    print(f"   Tamaño: {qr_whatsapp.size}")
    
    # Test 4: Información del QR
    print("✅ Test 4: Obteniendo información del QR")
    info = generator.get_qr_info("https://www.example.com")
    print(f"   Versión: {info['version']}")
    print(f"   Corrección: {info['error_correction']}")
    print(f"   Módulos: {info['modules']}x{info['modules']}")
    
    print("\n🎉 Todos los tests pasaron correctamente!")


if __name__ == "__main__":
    test_generator()