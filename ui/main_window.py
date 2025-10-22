"""
Ventana Principal de la Aplicación
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QMenuBar, QMenu, QStatusBar,
    QSplitter
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon

import config


class MainWindow(QMainWindow):
    """
    Ventana principal de la aplicación
    """
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Inicializar la interfaz de usuario"""
        # Configurar la ventana
        self.setWindowTitle(config.APP_NAME)
        self.setMinimumSize(config.WINDOW_MIN_WIDTH, config.WINDOW_MIN_HEIGHT)
        self.resize(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        
        # Crear menú superior
        self.create_menu_bar()
        
        # Crear widget central
        self.create_central_widget()
        
        # Crear barra de estado
        self.create_status_bar()
        
        # Centrar ventana en la pantalla
        self.center_on_screen()
        
    def create_menu_bar(self):
        """Crear la barra de menú superior"""
        menubar = self.menuBar()
        
        # Menú Archivo
        file_menu = menubar.addMenu("&Archivo")
        
        new_action = QAction("&Nuevo QR", self)
        new_action.setShortcut("Ctrl+N")
        new_action.setStatusTip("Crear un nuevo código QR")
        new_action.triggered.connect(self.new_qr)
        file_menu.addAction(new_action)
        
        open_action = QAction("&Abrir...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Abrir un QR guardado")
        open_action.triggered.connect(self.open_qr)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("&Salir", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Salir de la aplicación")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Menú Editar
        edit_menu = menubar.addMenu("&Editar")
        
        preferences_action = QAction("&Preferencias", self)
        preferences_action.setStatusTip("Configuración de la aplicación")
        preferences_action.triggered.connect(self.show_preferences)
        edit_menu.addAction(preferences_action)
        
        # Menú Ayuda
        help_menu = menubar.addMenu("A&yuda")
        
        about_action = QAction("&Acerca de", self)
        about_action.setStatusTip("Información sobre la aplicación")
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def create_central_widget(self):
        """Crear el widget central con el layout principal"""
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal horizontal
        main_layout = QHBoxLayout(central_widget)
        
        # Splitter para dividir la ventana en secciones redimensionables
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # PANEL IZQUIERDO: Selector de tipo y formulario
        left_panel = self.create_left_panel()
        splitter.addWidget(left_panel)
        
        # PANEL CENTRAL: Preview del QR
        center_panel = self.create_center_panel()
        splitter.addWidget(center_panel)
        
        # PANEL DERECHO: Personalización
        right_panel = self.create_right_panel()
        splitter.addWidget(right_panel)
        
        # Proporciones iniciales de los paneles (30% - 40% - 30%)
        splitter.setSizes([400, 600, 400])
        
        main_layout.addWidget(splitter)
        
    def create_left_panel(self):
        """Crear panel izquierdo - Selector y Formulario"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Título
        title = QLabel("📝 Tipo de QR")
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)
        
        # Mensaje temporal
        temp_label = QLabel("Aquí irá:\n\n• Selector de tipo de QR\n• Formulario dinámico\n• Campos de entrada")
        temp_label.setStyleSheet("padding: 20px; color: #666;")
        temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(temp_label)
        
        layout.addStretch()
        
        return panel
        
    def create_center_panel(self):
        """Crear panel central - Preview"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Título
        title = QLabel("👁️ Preview")
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)
        
        # Mensaje temporal
        temp_label = QLabel("Aquí se mostrará:\n\n• Preview del QR en tiempo real\n• Zoom\n• Controles de visualización")
        temp_label.setStyleSheet("padding: 20px; color: #666;")
        temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(temp_label)
        
        # Botón de prueba
        test_button = QPushButton("🎨 Generar QR de Prueba")
        test_button.clicked.connect(self.test_qr_generation)
        layout.addWidget(test_button)
        
        # Botón exportar
        export_button = QPushButton("💾 Exportar QR")
        export_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-weight: bold;")
        export_button.clicked.connect(self.export_qr)
        layout.addWidget(export_button)
        
        layout.addStretch()
        
        return panel
        
    def create_right_panel(self):
        """Crear panel derecho - Personalización"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Título
        title = QLabel("🎨 Personalización")
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)
        
        # Mensaje temporal
        temp_label = QLabel("Aquí irá:\n\n• Marcos\n• Patrones\n• Colores\n• Esquinas\n• Logos")
        temp_label.setStyleSheet("padding: 20px; color: #666;")
        temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(temp_label)
        
        layout.addStretch()
        
        return panel
        
    def create_status_bar(self):
        """Crear barra de estado inferior"""
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("✅ Listo para crear códigos QR")
        
    def center_on_screen(self):
        """Centrar la ventana en la pantalla"""
        screen_geometry = self.screen().availableGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())
        
    # ========================================================================
    # SLOTS (Funciones que responden a eventos)
    # ========================================================================
    
    def new_qr(self):
        """Crear nuevo QR"""
        self.statusBar().showMessage("🆕 Nuevo QR", 3000)
        print("📝 Acción: Nuevo QR")
        
    def open_qr(self):
        """Abrir QR guardado"""
        self.statusBar().showMessage("📂 Abrir QR", 3000)
        print("📂 Acción: Abrir QR")
        
    def show_preferences(self):
        """Mostrar preferencias"""
        self.statusBar().showMessage("⚙️ Preferencias", 3000)
        print("⚙️ Acción: Preferencias")
        
    def show_about(self):
        """Mostrar información de la aplicación"""
        from PyQt6.QtWidgets import QMessageBox
        
        about_text = f"""
        <h2>{config.APP_NAME}</h2>
        <p><b>Versión:</b> {config.APP_VERSION}</p>
        <p><b>Autor:</b> {config.APP_AUTHOR}</p>
        <br>
        <p>Generador de códigos QR personalizados con 15 tipos diferentes.</p>
        <p>Desarrollado con PyQt6 y Python.</p>
        """
        
        QMessageBox.about(self, "Acerca de", about_text)
        
    def test_qr_generation(self):
        """Función de prueba para generar QR"""
        self.statusBar().showMessage("🎨 Generando QR de prueba...", 3000)
        print("🎨 Acción: Generar QR de prueba")
        
    def export_qr(self):
        """Exportar QR"""
        self.statusBar().showMessage("💾 Exportando QR...", 3000)
        print("💾 Acción: Exportar QR")