"""
Exportador de Códigos QR
Módulo para exportar QR en diferentes formatos (SVG, PNG, PDF)
"""

import segno
from io import BytesIO
from pathlib import Path
from datetime import datetime

import config


class QRExporter:
    """
    Clase para exportar códigos QR en diferentes formatos
    """
    
    def __init__(self):
        """Inicializar exportador"""
        pass
    
    def export_svg(self, qr_content, filepath, scale=10, error_correction='Q'):
        """
        Exportar QR como SVG (vectorial)
        
        Args:
            qr_content: Contenido del QR (URL, texto, etc.)
            filepath: Ruta donde guardar el archivo
            scale: Escala del QR
            error_correction: Nivel de corrección (L, M, Q, H)
            
        Returns:
            bool: True si se exportó correctamente
        """
        try:
            # Asegurar extensión .svg
            filepath = Path(filepath)
            if filepath.suffix.lower() != '.svg':
                filepath = filepath.with_suffix('.svg')
            
            # Crear QR
            qr = segno.make(qr_content, error=error_correction)
            
            # Guardar como SVG
            qr.save(
                str(filepath),
                kind='svg',
                scale=scale,
                border=1  # Borde mínimo
            )
            
            print(f"✅ QR exportado como SVG: {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Error al exportar SVG: {e}")
            return False
    
    def export_png(self, qr_content, filepath, scale=10, error_correction='Q'):
        """
        Exportar QR como PNG (rasterizado)
        
        Args:
            qr_content: Contenido del QR
            filepath: Ruta donde guardar
            scale: Escala del QR (tamaño de cada módulo en píxeles)
            error_correction: Nivel de corrección
            
        Returns:
            bool: True si se exportó correctamente
        """
        try:
            # Asegurar extensión .png
            filepath = Path(filepath)
            if filepath.suffix.lower() != '.png':
                filepath = filepath.with_suffix('.png')
            
            # Crear QR
            qr = segno.make(qr_content, error=error_correction)
            
            # Guardar como PNG
            qr.save(
                str(filepath),
                kind='png',
                scale=scale,
                border=1
            )
            
            print(f"✅ QR exportado como PNG: {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Error al exportar PNG: {e}")
            return False
    
    def export_from_pil(self, pil_image, filepath, format='PNG'):
        """
        Exportar desde una imagen PIL ya generada
        
        Args:
            pil_image: Imagen PIL del QR
            filepath: Ruta donde guardar
            format: Formato (PNG, JPEG, etc.)
            
        Returns:
            bool: True si se exportó correctamente
        """
        try:
            filepath = Path(filepath)
            
            # Guardar la imagen
            pil_image.save(str(filepath), format=format)
            
            print(f"✅ QR exportado como {format}: {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Error al exportar desde PIL: {e}")
            return False
    
    def generate_filename(self, qr_type='qr', extension='png'):
        """
        Generar un nombre de archivo único
        
        Args:
            qr_type: Tipo de QR (url, wifi, etc.)
            extension: Extensión del archivo
            
        Returns:
            str: Nombre de archivo generado
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"qr_{qr_type}_{timestamp}.{extension}"
        return filename
    
    def get_default_export_path(self, filename):
        """
        Obtener ruta por defecto para exportación
        
        Args:
            filename: Nombre del archivo
            
        Returns:
            Path: Ruta completa
        """
        export_dir = config.EXPORTS_DIR
        export_dir.mkdir(parents=True, exist_ok=True)
        return export_dir / filename


def test_exporter():
    """Función de prueba del exportador"""
    print("🧪 Probando exportador de QR...\n")
    
    exporter = QRExporter()
    
    # Contenido de prueba
    test_content = "https://www.example.com"
    
    # Test 1: Exportar SVG
    print("✅ Test 1: Exportando como SVG")
    svg_filename = exporter.generate_filename('test', 'svg')
    svg_path = exporter.get_default_export_path(svg_filename)
    success = exporter.export_svg(test_content, svg_path, scale=10)
    print(f"   Resultado: {'✅ Éxito' if success else '❌ Falló'}")
    print(f"   Archivo: {svg_path}\n")
    
    # Test 2: Exportar PNG
    print("✅ Test 2: Exportando como PNG")
    png_filename = exporter.generate_filename('test', 'png')
    png_path = exporter.get_default_export_path(png_filename)
    success = exporter.export_png(test_content, png_path, scale=10)
    print(f"   Resultado: {'✅ Éxito' if success else '❌ Falló'}")
    print(f"   Archivo: {png_path}\n")
    
    # Test 3: Verificar que los archivos existen
    print("✅ Test 3: Verificando archivos creados")
    if svg_path.exists():
        print(f"   ✅ SVG existe: {svg_path.stat().st_size} bytes")
    else:
        print(f"   ❌ SVG no existe")
    
    if png_path.exists():
        print(f"   ✅ PNG existe: {png_path.stat().st_size} bytes")
    else:
        print(f"   ❌ PNG no existe")
    
    print("\n🎉 Tests completados!")
    print(f"\n📁 Los archivos se guardaron en: {config.EXPORTS_DIR}")


if __name__ == "__main__":
    test_exporter()