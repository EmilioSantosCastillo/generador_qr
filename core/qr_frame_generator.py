"""
Generador de Marcos para Códigos QR
Módulo para agregar marcos decorativos alrededor de los códigos QR
"""

from PIL import Image, ImageDraw, ImageFont
import os


class QRFrameGenerator:
    """
    Clase para agregar marcos decorativos a códigos QR
    """
    
    def __init__(self):
        """Inicializar generador de marcos"""
        pass
    
    def add_frame(self, qr_image, frame_style='none', primary_color='#000000'):
        """
        Agregar marco decorativo a un código QR
        
        Args:
            qr_image: PIL.Image del QR original
            frame_style: Estilo del marco ('none', 'scan_me_top', etc.)
            primary_color: Color principal del marco (hex)
            
        Returns:
            PIL.Image: Imagen del QR con marco
        """
        if frame_style == 'none':
            return qr_image
        
        # Convertir color hex a RGB
        frame_color = self._hex_to_rgb(primary_color)
        
        # Delegar a métodos específicos según el tipo de marco
        if frame_style == 'scan_me_top':
            return self._add_scan_me_top(qr_image, frame_color)
        elif frame_style == 'scan_me_bottom':
            return self._add_scan_me_bottom(qr_image, frame_color)
        elif frame_style == 'simple_border':
            return self._add_simple_border(qr_image, frame_color)
        elif frame_style == 'rounded_border':
            return self._add_rounded_border(qr_image, frame_color)
        elif frame_style == 'camera_icon':
            return self._add_camera_icon(qr_image, frame_color)
        elif frame_style == 'smartphone_icon':
            return self._add_smartphone_icon(qr_image, frame_color)
        elif frame_style == 'elegant':
            return self._add_elegant_frame(qr_image, frame_color)
        else:
            return qr_image
    
    def _hex_to_rgb(self, hex_color):
        """Convierte color hexadecimal a tupla RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _add_scan_me_top(self, qr_image, color):
        """Marco con texto 'SCAN ME' en la parte superior"""
        qr_width, qr_height = qr_image.size
        
        # Tamaño del marco superior
        top_margin = 80
        side_margin = 20
        
        # Crear nueva imagen con espacio para el marco
        new_width = qr_width + (side_margin * 2)
        new_height = qr_height + top_margin + side_margin
        
        new_image = Image.new('RGB', (new_width, new_height), 'white')
        draw = ImageDraw.Draw(new_image)
        
        # Dibujar texto "SCAN ME"
        text = "SCAN ME"
        try:
            # Intentar usar una fuente grande
            font = ImageFont.truetype("arial.ttf", 36)
        except:
            font = ImageFont.load_default()
        
        # Calcular posición del texto (centrado)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (new_width - text_width) // 2
        text_y = 20
        
        draw.text((text_x, text_y), text, fill=color, font=font)
        
        # Pegar el QR debajo del texto
        new_image.paste(qr_image, (side_margin, top_margin))
        
        return new_image
    
    def _add_scan_me_bottom(self, qr_image, color):
        """Marco con texto 'SCAN ME' en la parte inferior"""
        qr_width, qr_height = qr_image.size
        
        # Tamaño del marco
        bottom_margin = 80
        side_margin = 20
        
        # Crear nueva imagen
        new_width = qr_width + (side_margin * 2)
        new_height = qr_height + bottom_margin + side_margin
        
        new_image = Image.new('RGB', (new_width, new_height), 'white')
        draw = ImageDraw.Draw(new_image)
        
        # Pegar el QR primero
        new_image.paste(qr_image, (side_margin, side_margin))
        
        # Dibujar texto "SCAN ME" abajo
        text = "SCAN ME"
        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (new_width - text_width) // 2
        text_y = qr_height + side_margin + 20
        
        draw.text((text_x, text_y), text, fill=color, font=font)
        
        return new_image
    
    def _add_simple_border(self, qr_image, color):
        """Marco con borde simple alrededor"""
        qr_width, qr_height = qr_image.size
        
        border_width = 10  # ← CAMBIAR de 20 a 10
        
        # Crear nueva imagen con borde
        new_width = qr_width + (border_width * 2)
        new_height = qr_height + (border_width * 2)
        
        new_image = Image.new('RGB', (new_width, new_height), color)
        
        # Pegar el QR en el centro
        new_image.paste(qr_image, (border_width, border_width))
        
        return new_image
    
    def _add_rounded_border(self, qr_image, color):
        """Marco con borde redondeado"""
        qr_width, qr_height = qr_image.size
        
        border_width = 15  # ← CAMBIAR de 20 a 15
        corner_radius = 20  # ← CAMBIAR de 30 a 20
        
        # Crear nueva imagen
        new_width = qr_width + (border_width * 2)
        new_height = qr_height + (border_width * 2)
        
        new_image = Image.new('RGB', (new_width, new_height), 'white')
        draw = ImageDraw.Draw(new_image)
        
        # Dibujar rectángulo redondeado
        draw.rounded_rectangle(
            [(0, 0), (new_width, new_height)],
            radius=corner_radius,
            fill=color
        )
        
        # Pegar el QR en el centro
        new_image.paste(qr_image, (border_width, border_width))
        
        return new_image

    def _add_camera_icon(self, qr_image, color):
        """Marco con ícono de cámara"""
        qr_width, qr_height = qr_image.size
        
        top_margin = 100
        side_margin = 20
        
        new_width = qr_width + (side_margin * 2)
        new_height = qr_height + top_margin + side_margin
        
        new_image = Image.new('RGB', (new_width, new_height), 'white')
        draw = ImageDraw.Draw(new_image)
        
        # Dibujar ícono de cámara simple (círculo + rectángulo)
        center_x = new_width // 2
        camera_y = 30
        
        # Lente de la cámara (círculo)
        draw.ellipse(
            [center_x - 25, camera_y, center_x + 25, camera_y + 50],
            fill=color
        )
        
        # Texto "SCAN ME"
        text = "SCAN ME"
        try:
            font = ImageFont.truetype("arial.ttf", 28)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (new_width - text_width) // 2
        
        draw.text((text_x, camera_y + 60), text, fill=color, font=font)
        
        # Pegar el QR
        new_image.paste(qr_image, (side_margin, top_margin))
        
        return new_image
    
    def _add_smartphone_icon(self, qr_image, color):
        """Marco con ícono de smartphone"""
        qr_width, qr_height = qr_image.size
        
        top_margin = 100
        side_margin = 20
        
        new_width = qr_width + (side_margin * 2)
        new_height = qr_height + top_margin + side_margin
        
        new_image = Image.new('RGB', (new_width, new_height), 'white')
        draw = ImageDraw.Draw(new_image)
        
        # Dibujar smartphone simple
        center_x = new_width // 2
        phone_y = 20
        phone_width = 40
        phone_height = 60
        
        # Rectángulo del teléfono
        draw.rounded_rectangle(
            [center_x - phone_width//2, phone_y, 
             center_x + phone_width//2, phone_y + phone_height],
            radius=8,
            outline=color,
            width=3
        )
        
        # Texto
        text = "SCAN ME"
        try:
            font = ImageFont.truetype("arial.ttf", 28)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (new_width - text_width) // 2
        
        draw.text((text_x, phone_y + phone_height + 10), text, fill=color, font=font)
        
        # Pegar el QR
        new_image.paste(qr_image, (side_margin, top_margin))
        
        return new_image
    
    def _add_elegant_frame(self, qr_image, color):
        """Marco elegante con decoraciones en las esquinas"""
        qr_width, qr_height = qr_image.size
        
        border_width = 30
        
        new_width = qr_width + (border_width * 2)
        new_height = qr_height + (border_width * 2)
        
        new_image = Image.new('RGB', (new_width, new_height), 'white')
        draw = ImageDraw.Draw(new_image)
        
        # Dibujar borde doble
        # Borde exterior
        draw.rectangle(
            [(5, 5), (new_width - 5, new_height - 5)],
            outline=color,
            width=3
        )
        
        # Borde interior
        draw.rectangle(
            [(border_width - 5, border_width - 5), 
             (new_width - border_width + 5, new_height - border_width + 5)],
            outline=color,
            width=2
        )
        
        # Decoraciones en las esquinas
        corner_size = 15
        corners = [
            (10, 10),  # Superior izquierda
            (new_width - 10 - corner_size, 10),  # Superior derecha
            (10, new_height - 10 - corner_size),  # Inferior izquierda
            (new_width - 10 - corner_size, new_height - 10 - corner_size)  # Inferior derecha
        ]
        
        for x, y in corners:
            draw.rectangle([x, y, x + corner_size, y + corner_size], fill=color)
        
        # Pegar el QR
        new_image.paste(qr_image, (border_width, border_width))
        
        return new_image


def test_frame_generator():
    """Función de prueba del generador de marcos"""
    print("🧪 Probando generador de marcos...\n")
    
    # Crear un QR de prueba
    from core.qr_generator import QRGenerator
    
    generator = QRGenerator()
    qr_image = generator.generate("https://www.example.com", scale=10)
    
    frame_gen = QRFrameGenerator()
    
    # Probar cada tipo de marco
    frames = [
        'scan_me_top',
        'scan_me_bottom',
        'simple_border',
        'rounded_border',
        'camera_icon',
        'smartphone_icon',
        'elegant'
    ]
    
    for frame_style in frames:
        print(f"✅ Probando marco: {frame_style}")
        framed_qr = frame_gen.add_frame(qr_image, frame_style, '#3498db')
        print(f"   Tamaño con marco: {framed_qr.size}")
    
    print("\n🎉 Todos los marcos funcionan correctamente!")


if __name__ == "__main__":
    test_frame_generator()