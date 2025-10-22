"""
Widget de Preview del QR
Muestra el código QR generado en tiempo real
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QImage
from PIL import Image


class PreviewWidget(QWidget):
    """
    Widget para mostrar el preview del código QR
    """
    
    def __init__(self):
        super().__init__()
        self.current_qr_image = None
        self.init_ui()
        
    def init_ui(self):
        """Inicializar interfaz"""
        layout = QVBoxLayout(self)
        
        # Label para mostrar el QR
        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.qr_label.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px dashed #ccc;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        self.qr_label.setMinimumSize(300, 300)
        
        # Texto inicial
        self.show_placeholder()
        
        layout.addWidget(self.qr_label)
        
    def show_placeholder(self):
        """Mostrar texto cuando no hay QR"""
        self.qr_label.setText("📱\n\nEl código QR\naparecerá aquí")
        self.qr_label.setStyleSheet("""
            QLabel {
                background-color: #f5f5f5;
                border: 2px dashed #ccc;
                border-radius: 10px;
                padding: 20px;
                color: #999;
                font-size: 16px;
            }
        """)
        
    def update_qr(self, pil_image):
        """
        Actualizar el QR mostrado
        
        Args:
            pil_image: Imagen PIL del QR
        """
        if pil_image is None:
            self.show_placeholder()
            return
            
        self.current_qr_image = pil_image
        
        # Convertir PIL Image a QPixmap
        qimage = self.pil_to_qimage(pil_image)
        pixmap = QPixmap.fromImage(qimage)
        
        # Escalar para que quepa en el widget manteniendo aspecto
        scaled_pixmap = pixmap.scaled(
            self.qr_label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        
        self.qr_label.setPixmap(scaled_pixmap)
        self.qr_label.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        
    def pil_to_qimage(self, pil_image):
        """
        Convertir imagen PIL a QImage
        
        Args:
            pil_image: Imagen PIL
            
        Returns:
            QImage
        """
        # Convertir a RGBA si es necesario
        if pil_image.mode != "RGBA":
            pil_image = pil_image.convert("RGBA")
        
        data = pil_image.tobytes("raw", "RGBA")
        
        qimage = QImage(
            data,
            pil_image.width,
            pil_image.height,
            QImage.Format.Format_RGBA8888
        )
        
        return qimage
    
    def get_current_image(self):
        """
        Obtener la imagen actual del QR
        
        Returns:
            PIL.Image o None
        """
        return self.current_qr_image
    
    def clear(self):
        """Limpiar el preview"""
        self.current_qr_image = None
        self.show_placeholder()