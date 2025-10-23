"""
Pestaña WiFi - Formulario para generar códigos QR de conexión WiFi
"""
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit, 
                             QComboBox, QCheckBox, QPushButton, QLabel)
from PyQt6.QtCore import pyqtSignal, Qt


class WiFiTab(QWidget):
    """Formulario para crear QR de WiFi"""
    
    generate_qr_requested = pyqtSignal(str, str)  # (content, qr_type)
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_signals()
        
    def setup_ui(self):
        """Configurar interfaz del formulario"""
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Título
        title = QLabel("📶 Generar QR de WiFi")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # Descripción
        description = QLabel(
            "Crea un código QR para conectarse automáticamente a una red WiFi.\n"
            "Al escanear, el dispositivo se conectará sin necesidad de escribir la contraseña."
        )
        description.setWordWrap(True)
        description.setStyleSheet("color: #7f8c8d; margin-bottom: 10px;")
        layout.addWidget(description)
        
        # Formulario
        form_layout = QFormLayout()
        form_layout.setSpacing(10)
        
        # Campo: SSID (Nombre de red)
        self.ssid_input = QLineEdit()
        self.ssid_input.setPlaceholderText("Ej: MiRedWiFi")
        self.ssid_input.setMinimumHeight(35)
        form_layout.addRow("Nombre de red (SSID): *", self.ssid_input)
        
        # Campo: Tipo de cifrado
        self.encryption_combo = QComboBox()
        self.encryption_combo.addItems([
            "WPA/WPA2 (Recomendado)",
            "WEP (Obsoleto)",
            "Sin contraseña (Red abierta)"
        ])
        self.encryption_combo.setMinimumHeight(35)
        form_layout.addRow("Tipo de seguridad:", self.encryption_combo)
        
        # Campo: Contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Ej: MiContraseña123")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMinimumHeight(35)
        self.password_label = form_layout.addRow("Contraseña: *", self.password_input)
        
        # Checkbox: Mostrar contraseña
        self.show_password_check = QCheckBox("Mostrar contraseña")
        form_layout.addRow("", self.show_password_check)
        
        # Checkbox: Red oculta
        self.hidden_check = QCheckBox("Esta es una red oculta")
        self.hidden_check.setToolTip("Marcar si la red no transmite su SSID públicamente")
        form_layout.addRow("", self.hidden_check)
        
        layout.addLayout(form_layout)
        
        # Nota de seguridad
        security_note = QLabel(
            "⚠️ Nota de seguridad: La contraseña estará visible en el código QR. "
            "Usa solo para redes que se comparten públicamente (invitados, eventos, etc.)."
        )
        security_note.setWordWrap(True)
        security_note.setStyleSheet(
            "background-color: #fff3cd; "
            "border-left: 4px solid #ffc107; "
            "padding: 10px; "
            "color: #856404; "
            "margin: 10px 0;"
        )
        layout.addWidget(security_note)
        
        # Etiqueta de validación
        self.validation_label = QLabel()
        self.validation_label.setWordWrap(True)
        layout.addWidget(self.validation_label)
        
        # Botón generar
        self.generate_btn = QPushButton("📱 Generar QR WiFi")
        self.generate_btn.setMinimumHeight(45)
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
            }
        """)
        self.generate_btn.setEnabled(False)
        layout.addWidget(self.generate_btn)
        
        layout.addStretch()
        self.setLayout(layout)
        
    def connect_signals(self):
        """Conectar señales de los widgets"""
        self.ssid_input.textChanged.connect(self.validate_form)
        self.password_input.textChanged.connect(self.validate_form)
        self.encryption_combo.currentIndexChanged.connect(self.on_encryption_changed)
        self.show_password_check.stateChanged.connect(self.toggle_password_visibility)
        self.generate_btn.clicked.connect(self.generate_qr)
        
        # Validar al inicio
        self.validate_form()
        
    def on_encryption_changed(self):
        """Manejar cambio de tipo de cifrado"""
        encryption_type = self.encryption_combo.currentIndex()
        
        # Si es "Sin contraseña", deshabilitar campo de contraseña
        if encryption_type == 2:  # Sin contraseña
            self.password_input.setEnabled(False)
            self.password_input.clear()
            self.show_password_check.setEnabled(False)
            self.password_input.setPlaceholderText("(No requiere contraseña)")
        else:
            self.password_input.setEnabled(True)
            self.show_password_check.setEnabled(True)
            self.password_input.setPlaceholderText("Ej: MiContraseña123")
        
        self.validate_form()
        
    def toggle_password_visibility(self, state):
        """Alternar visibilidad de la contraseña"""
        if state == Qt.CheckState.Checked.value:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            
    def validate_form(self):
        """Validar el formulario en tiempo real"""
        ssid = self.ssid_input.text().strip()
        password = self.password_input.text()
        encryption_type = self.encryption_combo.currentIndex()
        
        # Lista de errores
        errors = []
        
        # Validar SSID
        if not ssid:
            errors.append("El nombre de red (SSID) es obligatorio")
        elif len(ssid) > 32:
            errors.append("El SSID no puede tener más de 32 caracteres")
            
        # Validar contraseña (si aplica)
        if encryption_type != 2:  # No es "Sin contraseña"
            if not password:
                errors.append("La contraseña es obligatoria para redes protegidas")
            elif encryption_type == 0 and len(password) < 8:  # WPA/WPA2
                errors.append("La contraseña WPA/WPA2 debe tener al menos 8 caracteres")
            elif encryption_type == 1 and len(password) not in [5, 13]:  # WEP
                errors.append("La contraseña WEP debe tener 5 o 13 caracteres")
        
        # Mostrar errores o éxito
        if errors:
            self.validation_label.setText("❌ " + " | ".join(errors))
            self.validation_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
            self.generate_btn.setEnabled(False)
        else:
            self.validation_label.setText("✅ Formulario válido - Listo para generar")
            self.validation_label.setStyleSheet("color: #27ae60; font-weight: bold;")
            self.generate_btn.setEnabled(True)
            
    def generate_qr(self):
        """Generar el código QR WiFi"""
        ssid = self.ssid_input.text().strip()
        password = self.password_input.text()
        encryption_type = self.encryption_combo.currentIndex()
        is_hidden = self.hidden_check.isChecked()
        
        # Mapear tipo de cifrado
        encryption_map = {
            0: "WPA",      # WPA/WPA2
            1: "WEP",      # WEP
            2: "nopass"    # Sin contraseña
        }
        encryption = encryption_map[encryption_type]
        
        # Si es red sin contraseña, vaciar password
        if encryption == "nopass":
            password = ""
        
        # Construir formato WiFi QR
        # Formato: WIFI:T:{encryption};S:{ssid};P:{password};H:{hidden};;
        hidden_str = "true" if is_hidden else "false"
        
        wifi_string = f"WIFI:T:{encryption};S:{ssid};P:{password};H:{hidden_str};;"
        
        # Emitir señal para generar QR
        self.generate_qr_requested.emit(wifi_string, "wifi")
        
    def clear(self):
        """Limpiar el formulario"""
        self.ssid_input.clear()
        self.password_input.clear()
        self.encryption_combo.setCurrentIndex(0)
        self.hidden_check.setChecked(False)
        self.show_password_check.setChecked(False)
        self.validation_label.clear()
        self.generate_btn.setEnabled(False)