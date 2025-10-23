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
        
    def generate(self, content, scale=10, dark_color='#000000', light_color='#FFFFFF', pattern_style='squares', frame_style='none'):
        """
        Genera un código QR básico con personalización
        
        Args:
            content: Contenido del QR (URL, texto, etc.)
            scale: Escala del QR (tamaño de cada módulo)
            dark_color: Color de los módulos oscuros (hex, ej: '#FF0000')
            light_color: Color de fondo/módulos claros (hex, ej: '#FFFFFF')
            pattern_style: Estilo de los módulos ('squares', 'rounded', 'circles', 'flowers', 'hearts', 'dots')
            frame_style: Estilo del marco decorativo ('none', 'scan_me_top', etc.)
            
        Returns:
            PIL.Image: Imagen del QR generado
        """
        # Crear QR con segno
        qr = segno.make(
            content,
            error=self.error_correction,
            boost_error=False
        )
        
        # Convertir colores hex a RGB
        dark_rgb = self._hex_to_rgb(dark_color)
        light_rgb = self._hex_to_rgb(light_color)
        
        # Generar QR según el patrón
        if pattern_style in ['squares', 'rounded']:
            buffer = BytesIO()
            qr.save(
                buffer, 
                kind='png', 
                scale=scale,
                dark=dark_rgb,
                light=light_rgb
            )
            buffer.seek(0)
            qr_image = Image.open(buffer)
        else:
            # Patrones avanzados
            qr_image = self._generate_custom_pattern(qr, scale, dark_rgb, light_rgb, pattern_style)
        
        # Aplicar marco decorativo si es necesario
        if frame_style != 'none':
            from core.qr_frame_generator import QRFrameGenerator
            frame_gen = QRFrameGenerator()
            qr_image = frame_gen.add_frame(qr_image, frame_style, dark_color)
        
        return qr_image
    



    def _generate_custom_pattern(self, qr, scale, dark_rgb, light_rgb, pattern_style):
        """
        Genera QR con patrones personalizados (círculos, flores, corazones, puntos)
        
        Args:
            qr: Objeto QR de segno
            scale: Escala del QR
            dark_rgb: Color oscuro (tupla RGB)
            light_rgb: Color claro (tupla RGB)
            pattern_style: Estilo del patrón
            
        Returns:
            PIL.Image: Imagen del QR con patrón personalizado
        """
        from PIL import ImageDraw
        
        # Obtener matriz de módulos del QR
        matrix = qr.matrix
        size = len(matrix)
        
        # Calcular tamaño de la imagen
        img_size = size * scale
        
        # Crear imagen con color de fondo
        image = Image.new('RGB', (img_size, img_size), light_rgb)
        draw = ImageDraw.Draw(image)
        
        # Dibujar cada módulo según el patrón
        for row in range(size):
            for col in range(size):
                if matrix[row][col]:  # Si el módulo está "encendido"
                    x = col * scale
                    y = row * scale
                    
                    # Dibujar según el patrón seleccionado
                    if pattern_style == 'circles':
                        # Círculos
                        margin = scale * 0.1
                        draw.ellipse(
                            [x + margin, y + margin, x + scale - margin, y + scale - margin],
                            fill=dark_rgb
                        )
                        
                    elif pattern_style == 'flowers':
                        # Flores/cruces (4 círculos pequeños en las esquinas)
                        quarter = scale / 4
                        radius = scale / 6
                        positions = [
                            (x + quarter, y + quarter),
                            (x + 3*quarter, y + quarter),
                            (x + quarter, y + 3*quarter),
                            (x + 3*quarter, y + 3*quarter)
                        ]
                        for px, py in positions:
                            draw.ellipse(
                                [px - radius, py - radius, px + radius, py + radius],
                                fill=dark_rgb
                            )
                        
                    elif pattern_style == 'hearts':
                        # Corazones (aproximación con círculos y triángulo)
                        # Versión simplificada: círculo
                        margin = scale * 0.15
                        draw.ellipse(
                            [x + margin, y + margin, x + scale - margin, y + scale - margin],
                            fill=dark_rgb
                        )
                        
                    elif pattern_style == 'dots':
                        # Puntos pequeños (círculos más pequeños)
                        margin = scale * 0.3
                        draw.ellipse(
                            [x + margin, y + margin, x + scale - margin, y + scale - margin],
                            fill=dark_rgb
                        )
                        
                    else:  # Default: cuadrados
                        draw.rectangle(
                            [x, y, x + scale, y + scale],
                            fill=dark_rgb
                        )
        
        return image
    def _hex_to_rgb(self, hex_color):
        """
        Convierte color hexadecimal a tupla RGB
        
        Args:
            hex_color: Color en formato hex (#RRGGBB)
            
        Returns:
            tuple: (R, G, B) valores de 0-255
        """
        # Remover el # si existe
        hex_color = hex_color.lstrip('#')
        
        # Convertir a RGB
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
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