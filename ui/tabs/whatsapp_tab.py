"""
Pestaña/Formulario para QR tipo WhatsApp
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QTextEdit, QComboBox, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class WhatsAppTab(QWidget):
    """
    Formulario para crear QR de tipo WhatsApp
    """
    
    # Señal que se emite cuando el usuario quiere generar el QR
    generate_qr_requested = pyqtSignal(str, str)  # Emite (phone, message)
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Inicializar interfaz"""
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # Título del tipo de QR
        title = QLabel("💬 WhatsApp")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Descripción
        description = QLabel(
            "Genera un código QR que abre WhatsApp con un número y mensaje precargado.\n"
            "El usuario solo necesita presionar 'Enviar'."
        )
        description.setStyleSheet("color: #666; padding: 5px;")
        description.setWordWrap(True)
        layout.addWidget(description)
        
        # Separador
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)
        
        # === CÓDIGO DE PAÍS ===
        country_label = QLabel("Código de país:")
        country_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(country_label)
        
        # Layout horizontal para código de país
        country_layout = QHBoxLayout()
        
        # ComboBox con códigos comunes
        self.country_code_combo = QComboBox()
        self.country_code_combo.addItems([
            "🇨🇱 +56 (Chile)",
            "🇦🇷 +54 (Argentina)",
            "🇲🇽 +52 (México)",
            "🇨🇴 +57 (Colombia)",
            "🇵🇪 +51 (Perú)",
            "🇺🇸 +1 (USA/Canadá)",
            "🇪🇸 +34 (España)",
            "🇧🇷 +55 (Brasil)",
            "🇻🇪 +58 (Venezuela)",
            "🇺🇾 +598 (Uruguay)",
            "🇵🇾 +595 (Paraguay)",
            "🇧🇴 +591 (Bolivia)",
            "🇪🇨 +593 (Ecuador)"
        ])
        self.country_code_combo.setMinimumHeight(35)
        self.country_code_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 13px;
            }
        """)
        country_layout.addWidget(self.country_code_combo)
        
        layout.addLayout(country_layout)
        
        # === NÚMERO DE TELÉFONO ===
        phone_label = QLabel("Número de teléfono:")
        phone_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(phone_label)
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("912345678 (sin el código de país)")
        self.phone_input.setMinimumHeight(35)
        self.phone_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #25D366;
            }
        """)
        self.phone_input.textChanged.connect(self.on_input_changed)
        layout.addWidget(self.phone_input)
        
        help_phone = QLabel("💡 Solo números, sin espacios ni guiones")
        help_phone.setStyleSheet("color: #888; font-size: 11px; padding: 5px;")
        layout.addWidget(help_phone)
        
        # === MENSAJE ===
        message_label = QLabel("Mensaje (opcional):")
        message_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(message_label)
        
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Hola, quisiera más información sobre...")
        self.message_input.setMinimumHeight(80)
        self.message_input.setMaximumHeight(150)
        self.message_input.setStyleSheet("""
            QTextEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 13px;
            }
            QTextEdit:focus {
                border: 2px solid #25D366;
            }
        """)
        self.message_input.textChanged.connect(self.on_input_changed)
        layout.addWidget(self.message_input)
        
        help_message = QLabel("💡 El mensaje aparecerá precargado en WhatsApp")
        help_message.setStyleSheet("color: #888; font-size: 11px; padding: 5px;")
        layout.addWidget(help_message)
        
        # Estado de validación
        self.validation_label = QLabel("")
        self.validation_label.setStyleSheet("padding: 5px;")
        layout.addWidget(self.validation_label)
        
        # Botón de generar
        self.generate_button = QPushButton("🎨 Generar QR")
        self.generate_button.setMinimumHeight(40)
        self.generate_button.setStyleSheet("""
            QPushButton {
                background-color: #25D366;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #20BA5A;
            }
            QPushButton:pressed {
                background-color: #1DA851;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.generate_button.clicked.connect(self.on_generate_clicked)
        self.generate_button.setEnabled(False)
        
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
            "• Abre WhatsApp automáticamente\n"
            "• Mensaje precargado (opcional)\n"
            "• Compatible con app móvil y WhatsApp Web"
        )
        info_text.setStyleSheet("color: #666; font-size: 12px; padding-left: 10px;")
        layout.addWidget(info_text)
        
        # Espaciador
        layout.addStretch()
        
    def on_input_changed(self):
        """Evento cuando cambia algún input"""
        phone = self.phone_input.text().strip()
        
        if not phone:
            self.validation_label.setText("")
            self.generate_button.setEnabled(False)
            return
        
        is_valid = self.validate_phone(phone)
        
        if is_valid:
            self.validation_label.setText("✅ Número válido")
            self.validation_label.setStyleSheet("color: green; padding: 5px;")
            self.generate_button.setEnabled(True)
        else:
            self.validation_label.setText("⚠️ Solo números, sin espacios ni caracteres especiales")
            self.validation_label.setStyleSheet("color: orange; padding: 5px;")
            self.generate_button.setEnabled(False)
    
    def validate_phone(self, phone):
        """
        Validar número de teléfono
        
        Args:
            phone: Número a validar
            
        Returns:
            bool: True si es válido
        """
        if not phone:
            return False
        
        # Solo debe contener números
        return phone.isdigit() and len(phone) >= 6
    
    def get_country_code(self):
        """Extraer código de país del combo box"""
        text = self.country_code_combo.currentText()
        # Extraer el número del texto (ej: "🇨🇱 +56 (Chile)" -> "56")
        code = text.split('+')[1].split(' ')[0]
        return code
    
    def on_generate_clicked(self):
        """Cuando se hace clic en generar QR"""
        phone = self.phone_input.text().strip()
        message = self.message_input.toPlainText().strip()
        
        if self.validate_phone(phone):
            # Construir número completo con código de país
            country_code = self.get_country_code()
            full_phone = f"{country_code}{phone}"
            
            print(f"📝 Generando QR para WhatsApp: +{full_phone}")
            if message:
                print(f"   Mensaje: {message[:50]}...")
            
            # Emitir señal con teléfono completo y mensaje
            self.generate_qr_requested.emit(full_phone, message)
    
    def get_qr_data(self):
        """
        Obtener los datos del QR
        
        Returns:
            dict: Datos del formulario
        """
        return {
            'phone': f"{self.get_country_code()}{self.phone_input.text().strip()}",
            'message': self.message_input.toPlainText().strip()
        }
    
    def clear(self):
        """Limpiar el formulario"""
        self.phone_input.clear()
        self.message_input.clear()
        self.validation_label.setText("")
        self.generate_button.setEnabled(False)