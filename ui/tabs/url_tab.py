"""
Pestaña/Formulario para QR tipo URL (Sitio Web)
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class URLTab(QWidget):
    """
    Formulario para crear QR de tipo URL/Sitio Web
    """
    
    # Señal que se emite cuando el usuario quiere generar el QR
    generate_qr_requested = pyqtSignal(str)  # Emite la URL
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Inicializar interfaz"""
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # Título del tipo de QR
        title = QLabel("🌐 Sitio Web / URL")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Descripción
        description = QLabel(
            "Genera un código QR que redirige directamente a una URL.\n"
            "Perfecto para sitios web, redes sociales, portfolios, etc."
        )
        description.setStyleSheet("color: #666; padding: 5px;")
        description.setWordWrap(True)
        layout.addWidget(description)
        
        # Separador
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)
        
        # Label del campo
        url_label = QLabel("URL del sitio web:")
        url_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(url_label)
        
        # Input de la URL
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://www.ejemplo.com")
        self.url_input.setMinimumHeight(35)
        self.url_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50;
            }
        """)
        
        # Conectar evento de cambio de texto
        self.url_input.textChanged.connect(self.on_url_changed)
        
        layout.addWidget(self.url_input)
        
        # Mensaje de ayuda
        help_text = QLabel("💡 Tip: Incluye el protocolo (https://) para mejor compatibilidad")
        help_text.setStyleSheet("color: #888; font-size: 11px; padding: 5px;")
        help_text.setWordWrap(True)
        layout.addWidget(help_text)
        
        # Estado de validación
        self.validation_label = QLabel("")
        self.validation_label.setStyleSheet("padding: 5px;")
        layout.addWidget(self.validation_label)
        
        # Botón de generar
        self.generate_button = QPushButton("🎨 Generar QR")
        self.generate_button.setMinimumHeight(40)
        self.generate_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.generate_button.clicked.connect(self.on_generate_clicked)
        self.generate_button.setEnabled(False)  # Deshabilitado inicialmente
        
        layout.addWidget(self.generate_button)
        
        # Separador
        line2 = QFrame()
        line2.setFrameShape(QFrame.Shape.HLine)
        line2.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line2)
        
        # Información adicional
        info_title = QLabel("ℹ️ Información")
        info_title.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(info_title)
        
        info_text = QLabel(
            "• Tipo: QR Estático\n"
            "• El QR contiene la URL directamente\n"
            "• No requiere conexión a servidor\n"
            "• Ideal para enlaces permanentes"
        )
        info_text.setStyleSheet("color: #666; font-size: 12px; padding-left: 10px;")
        layout.addWidget(info_text)
        
        # Espaciador al final
        layout.addStretch()
        
    def on_url_changed(self, text):
        """Evento cuando cambia el texto de la URL"""
        # Validar URL
        is_valid = self.validate_url(text)
        
        if not text:
            self.validation_label.setText("")
            self.generate_button.setEnabled(False)
        elif is_valid:
            self.validation_label.setText("✅ URL válida")
            self.validation_label.setStyleSheet("color: green; padding: 5px;")
            self.generate_button.setEnabled(True)
        else:
            self.validation_label.setText("⚠️ URL inválida - Debe incluir http:// o https://")
            self.validation_label.setStyleSheet("color: orange; padding: 5px;")
            self.generate_button.setEnabled(False)
    
    def validate_url(self, url):
        """
        Validar que la URL tenga formato correcto
        
        Args:
            url: URL a validar
            
        Returns:
            bool: True si es válida
        """
        if not url:
            return False
        
        url = url.strip()
        
        # Debe empezar con http:// o https://
        if not (url.startswith('http://') or url.startswith('https://')):
            return False
        
        # Debe tener al menos un punto después del protocolo
        url_without_protocol = url.split('://', 1)[1] if '://' in url else url
        if '.' not in url_without_protocol:
            return False
        
        return True
    
    def on_generate_clicked(self):
        """Cuando se hace clic en generar QR"""
        url = self.url_input.text().strip()
        
        if self.validate_url(url):
            print(f"📝 Generando QR para URL: {url}")
            # Emitir señal con la URL
            self.generate_qr_requested.emit(url)
        
    def get_qr_content(self):
        """
        Obtener el contenido del QR
        
        Returns:
            str: URL ingresada
        """
        return self.url_input.text().strip()
    
    def clear(self):
        """Limpiar el formulario"""
        self.url_input.clear()
        self.validation_label.setText("")
        self.generate_button.setEnabled(False)