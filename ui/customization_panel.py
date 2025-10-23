"""
Panel de personalización del código QR
Permite cambiar colores, patrones, marcos, etc.
"""
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                             QColorDialog, QHBoxLayout, QGroupBox, QScrollArea)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QColor


class CustomizationPanel(QWidget):
    """Panel lateral derecho para personalizar el QR"""
    
    # Señal emitida cuando cambia alguna configuración
    customization_changed = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        self.config = {
            'pattern_color': '#000000',  # Negro por defecto
            'background_color': '#FFFFFF',  # Blanco por defecto
            'pattern_style': 'squares',  # Estilo por defecto
            'frame_style': 'none',  # Sin marco por defecto
        }
        self.setup_ui()
        
    def setup_ui(self):
        """Configurar interfaz del panel"""
        # Layout principal con scroll
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Área scrolleable
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Widget de contenido
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        # Título
        title = QLabel("🎨 Personalización")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        content_layout.addWidget(title)
        
        # Sección: Colores
        colors_group = self.create_colors_section()
        content_layout.addWidget(colors_group)
        
        # Sección: Patrones (próximamente)
        patterns_group = self.create_patterns_section()
        content_layout.addWidget(patterns_group)
        
        # Sección: Marcos (próximamente)
        frames_group = self.create_frames_section()
        content_layout.addWidget(frames_group)
        
        # Botón resetear
        reset_btn = QPushButton("🔄 Restaurar valores por defecto")
        reset_btn.setMinimumHeight(40)
        reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        reset_btn.clicked.connect(self.reset_to_defaults)
        content_layout.addWidget(reset_btn)
        
        content_layout.addStretch()
        
        content_widget.setLayout(content_layout)
        scroll.setWidget(content_widget)
        
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)
        
    def create_colors_section(self):
        """Crear sección de selección de colores"""
        group = QGroupBox("Colores")
        group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #dee2e6;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Color del patrón (módulos oscuros)
        pattern_layout = QHBoxLayout()
        pattern_label = QLabel("Color del código:")
        pattern_layout.addWidget(pattern_label)
        
        self.pattern_color_preview = QLabel("███")
        self.pattern_color_preview.setStyleSheet(f"color: {self.config['pattern_color']}; font-size: 24px;")
        pattern_layout.addWidget(self.pattern_color_preview)
        
        self.pattern_color_btn = QPushButton("Seleccionar")
        self.pattern_color_btn.setMinimumHeight(35)
        self.pattern_color_btn.clicked.connect(self.select_pattern_color)
        pattern_layout.addWidget(self.pattern_color_btn)
        
        layout.addLayout(pattern_layout)
        
        # Color de fondo (módulos claros)
        background_layout = QHBoxLayout()
        background_label = QLabel("Color de fondo:")
        background_layout.addWidget(background_label)
        
        self.background_color_preview = QLabel("███")
        self.background_color_preview.setStyleSheet(f"color: {self.config['background_color']}; font-size: 24px;")
        background_layout.addWidget(self.background_color_preview)
        
        self.background_color_btn = QPushButton("Seleccionar")
        self.background_color_btn.setMinimumHeight(35)
        self.background_color_btn.clicked.connect(self.select_background_color)
        background_layout.addWidget(self.background_color_btn)
        
        layout.addLayout(background_layout)
        
        # Nota sobre contraste
        note = QLabel("💡 Tip: Usa colores con buen contraste para garantizar que el QR sea escaneable.")
        note.setWordWrap(True)
        note.setStyleSheet("color: #6c757d; font-size: 11px; font-weight: normal;")
        layout.addWidget(note)
        
        group.setLayout(layout)
        return group
        
    def create_patterns_section(self):
        """Crear sección de patrones del código"""
        group = QGroupBox("Patrones del código")
        group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #dee2e6;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Selector de patrón
        from PyQt6.QtWidgets import QComboBox
        
        pattern_label = QLabel("Estilo de módulos:")
        layout.addWidget(pattern_label)
        
        self.pattern_combo = QComboBox()
        self.pattern_combo.addItems([
            "▪ Cuadrados estándar",
            "◽ Cuadrados redondeados",
            "● Círculos grandes",
            "✦ Flores/cruces",
            "♥ Corazones",
            "· Puntos pequeños"
        ])
        self.pattern_combo.setMinimumHeight(35)
        self.pattern_combo.currentIndexChanged.connect(self.on_pattern_changed)
        layout.addWidget(self.pattern_combo)
        
        # Nota informativa
        note = QLabel("💡 Los patrones avanzados (círculos, flores, corazones) pueden tardar más en generarse.")
        note.setWordWrap(True)
        note.setStyleSheet("color: #6c757d; font-size: 11px; font-weight: normal; margin-top: 10px;")
        layout.addWidget(note)
        
        group.setLayout(layout)
        return group
        
    def create_frames_section(self):
        """Crear sección de marcos decorativos"""
        group = QGroupBox("Marcos decorativos")
        group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #dee2e6;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Selector de marco
        from PyQt6.QtWidgets import QComboBox
        
        frame_label = QLabel("Estilo de marco:")
        layout.addWidget(frame_label)
        
        self.frame_combo = QComboBox()
        self.frame_combo.addItems([
            "Sin marco",
            "📱 'Scan Me' - Superior",
            "📱 'Scan Me' - Inferior",
            "⬜ Borde simple",
            "⬜ Borde redondeado",
            "📷 Con ícono de cámara",
            "📱 Con ícono de smartphone",
            "✨ Marco elegante"
        ])
        self.frame_combo.setMinimumHeight(35)
        self.frame_combo.currentIndexChanged.connect(self.on_frame_changed)
        layout.addWidget(self.frame_combo)
        
        # Nota informativa
        note = QLabel("💡 Los marcos se agregan alrededor del código QR sin afectar su funcionalidad.")
        note.setWordWrap(True)
        note.setStyleSheet("color: #6c757d; font-size: 11px; font-weight: normal; margin-top: 10px;")
        layout.addWidget(note)
        
        group.setLayout(layout)
        return group
        
    def select_pattern_color(self):
        """Abrir diálogo para seleccionar color del patrón"""
        current_color = QColor(self.config['pattern_color'])
        color = QColorDialog.getColor(current_color, self, "Seleccionar color del código")
        
        if color.isValid():
            self.config['pattern_color'] = color.name()
            self.pattern_color_preview.setStyleSheet(f"color: {color.name()}; font-size: 24px;")
            self.emit_changes()
            
    def select_background_color(self):
        """Abrir diálogo para seleccionar color de fondo"""
        current_color = QColor(self.config['background_color'])
        color = QColorDialog.getColor(current_color, self, "Seleccionar color de fondo")
        
        if color.isValid():
            self.config['background_color'] = color.name()
            self.background_color_preview.setStyleSheet(f"color: {color.name()}; font-size: 24px;")
            self.emit_changes()

    def on_pattern_changed(self):
        """Manejar cambio de patrón"""
        pattern_index = self.pattern_combo.currentIndex()
        
        # Mapear índice a nombre de patrón
        patterns = ['squares', 'rounded', 'circles', 'flowers', 'hearts', 'dots']
        self.config['pattern_style'] = patterns[pattern_index]
        
        self.emit_changes() 
          
    def on_frame_changed(self):
        """Manejar cambio de marco"""
        frame_index = self.frame_combo.currentIndex()
        
        # Mapear índice a nombre de marco
        frames = [
            'none', 
            'scan_me_top', 
            'scan_me_bottom', 
            'simple_border', 
            'rounded_border',
            'camera_icon',
            'smartphone_icon',
            'elegant'
        ]
        self.config['frame_style'] = frames[frame_index]
        
        self.emit_changes()

    def reset_to_defaults(self):
        """Restaurar configuración por defecto"""
        self.config = {
            'pattern_color': '#000000',
            'background_color': '#FFFFFF',
            'pattern_style': 'squares',
            'frame_style': 'none',
        }
        
        # Actualizar previews
        self.pattern_color_preview.setStyleSheet(f"color: #000000; font-size: 24px;")
        self.background_color_preview.setStyleSheet(f"color: #FFFFFF; font-size: 24px;")
        
        # Resetear combos
        self.pattern_combo.setCurrentIndex(0)
        self.frame_combo.setCurrentIndex(0)  # ← AGREGAR ESTA LÍNEA
        
        self.emit_changes()
        
    def emit_changes(self):
        """Emitir señal con la configuración actual"""
        self.customization_changed.emit(self.config.copy())
        
    def get_config(self):
        """Obtener configuración actual"""
        return self.config.copy()