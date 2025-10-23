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
        # Variables para almacenar el QR actual
        self.current_qr_content = None
        self.current_qr_type = None
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
        from PyQt6.QtWidgets import QTabWidget
        
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Título
        title = QLabel("📝 Tipo de QR")
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)
        
        # TabWidget para los diferentes tipos de QR
        self.qr_tabs = QTabWidget()
        self.qr_tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QTabBar::tab {
                background: #f0f0f0;
                padding: 8px 15px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: #4CAF50;
                color: white;
            }
            QTabBar::tab:hover {
                background: #e0e0e0;
            }
        """)
        
        # Importar y agregar formularios
        from ui.tabs.url_tab import URLTab
        from ui.tabs.whatsapp_tab import WhatsAppTab
        from ui.tabs.wifi_tab import WiFiTab
        
        
        # Pestaña URL
        self.url_tab = URLTab()
        self.url_tab.generate_qr_requested.connect(self.generate_qr_from_url)
        self.qr_tabs.addTab(self.url_tab, "🌐 URL")
        
        # Pestaña WhatsApp
        self.whatsapp_tab = WhatsAppTab()
        self.whatsapp_tab.generate_qr_requested.connect(self.generate_qr_from_whatsapp)
        self.qr_tabs.addTab(self.whatsapp_tab, "💬 WhatsApp")

        # Pestaña WiFi
        self.wifi_tab = WiFiTab()
        self.wifi_tab.generate_qr_requested.connect(self.generate_qr_from_wifi)
        self.qr_tabs.addTab(self.wifi_tab, "📶 WiFi")
        
        layout.addWidget(self.qr_tabs)
        
        return panel
        
    def create_center_panel(self):
        """Crear panel central - Preview"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Título
        title = QLabel("👁️ Preview")
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)
        
        # Widget de preview (importar aquí)
        from ui.preview_widget import PreviewWidget
        self.preview_widget = PreviewWidget()
        layout.addWidget(self.preview_widget, stretch=1)
        
        # Botón de prueba
        test_button = QPushButton("🎨 Generar QR de Prueba")
        test_button.clicked.connect(self.test_qr_generation)
        layout.addWidget(test_button)
        
        # Botón exportar
        export_button = QPushButton("💾 Exportar QR")
        export_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-weight: bold;")
        export_button.clicked.connect(self.export_qr)
        layout.addWidget(export_button)
        
        return panel
        
    def create_right_panel(self):
        """Panel derecho - Personalización del QR"""
        from ui.customization_panel import CustomizationPanel

        panel = QWidget()
        panel.setMinimumWidth(350)
        panel.setMaximumWidth(400)
        panel.setStyleSheet("background-color: #f8f9fa; border-left: 1px solid #dee2e6;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Panel de personalización
        self.customization_panel = CustomizationPanel()
        self.customization_panel.customization_changed.connect(self.on_customization_changed)
        
        layout.addWidget(self.customization_panel)
        panel.setLayout(layout)
        
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
        print("🎨 Generando QR de prueba...")
        
        # Importar el generador
        from core.qr_generator import QRGenerator
        
        # Crear generador
        generator = QRGenerator()
        
        # Generar QR de ejemplo
        qr_image = generator.generate_url("https://www.example.com", scale=10)
        
        # Mostrar en el preview
        self.preview_widget.update_qr(qr_image)
        
        self.statusBar().showMessage("✅ QR generado correctamente", 3000)
        print("✅ QR generado y mostrado en preview")
        
    def export_qr(self):
        """Exportar QR"""
        from PyQt6.QtWidgets import QFileDialog, QMessageBox
        from core.qr_exporter import QRExporter
        
        # Verificar que hay un QR para exportar
        current_image = self.preview_widget.get_current_image()
        if current_image is None:
            QMessageBox.warning(
                self,
                "Sin QR",
                "No hay ningún código QR para exportar.\nPrimero genera un QR."
            )
            return
        
        # Diálogo para elegir formato
        format_dialog = QMessageBox()
        format_dialog.setWindowTitle("Formato de Exportación")
        format_dialog.setText("¿En qué formato deseas exportar el QR?")
        
        svg_button = format_dialog.addButton("📐 SVG (Vectorial)", QMessageBox.ButtonRole.AcceptRole)
        png_button = format_dialog.addButton("🖼️ PNG (Imagen)", QMessageBox.ButtonRole.AcceptRole)
        cancel_button = format_dialog.addButton("Cancelar", QMessageBox.ButtonRole.RejectRole)
        
        format_dialog.exec()
        
        clicked_button = format_dialog.clickedButton()
        
        if clicked_button == cancel_button:
            return
        
        # Determinar formato elegido
        if clicked_button == svg_button:
            file_format = "SVG"
            file_extension = "svg"
            file_filter = "Archivos SVG (*.svg)"
        else:  # PNG
            file_format = "PNG"
            file_extension = "png"
            file_filter = "Archivos PNG (*.png)"
        
        # Diálogo para elegir ubicación
        from core.qr_exporter import QRExporter
        exporter = QRExporter()
        default_filename = exporter.generate_filename('qr', file_extension)
        default_path = exporter.get_default_export_path(default_filename)
        
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            f"Guardar QR como {file_format}",
            str(default_path),
            file_filter
        )
        
        if not filepath:
            return  # Usuario canceló
        
        # Exportar
        self.statusBar().showMessage(f"💾 Exportando como {file_format}...", 2000)
        
        # Para este ejemplo, exportamos el contenido actual
        # TODO: En el futuro, guardaremos el contenido original del QR
       # Obtener el contenido y la configuración de colores
        if self.current_qr_content:
            test_content = self.current_qr_content
        else:
            test_content = "https://www.example.com"  # Fallback

        # Obtener colores personalizados del panel
        customization_config = self.customization_panel.get_config()
        dark_color = customization_config['pattern_color']
        light_color = customization_config['background_color']

        # Obtener patrón seleccionado
        # Obtener patrón y marco seleccionados
        pattern_style = customization_config['pattern_style']
        frame_style = customization_config['frame_style']  # ← AGREGAR

        success = False
        if file_format == "SVG":
            success = exporter.export_svg(
                test_content, 
                filepath, 
                scale=10,
                dark_color=dark_color,
                light_color=light_color,
                pattern_style=pattern_style,
                frame_style=frame_style  # ← AGREGAR
            )
        else:  # PNG
            success = exporter.export_png(
                test_content, 
                filepath, 
                scale=10,
                dark_color=dark_color,
                light_color=light_color,
                pattern_style=pattern_style,
                frame_style=frame_style  # ← AGREGAR
            )
        
        if success:
            QMessageBox.information(
                self,
                "Exportación Exitosa",
                f"✅ QR exportado correctamente como {file_format}\n\n📁 {filepath}"
            )
            self.statusBar().showMessage(f"✅ QR exportado como {file_format}", 5000)
        else:
            QMessageBox.critical(
                self,
                "Error",
                f"❌ Error al exportar el QR como {file_format}"
            )
            self.statusBar().showMessage("❌ Error al exportar", 5000)
    def generate_qr_from_url(self, url):
        """
        Generar QR desde el formulario URL
        
        Args:
            url: URL para generar el QR
        """
        self.statusBar().showMessage(f"🎨 Generando QR para: {url}", 3000)
        print(f"🎨 Generando QR para: {url}")
        
        try:
            # Importar el generador
            from core.qr_generator import QRGenerator
            
            # Crear generador
            generator = QRGenerator()
            
            # Generar QR
            qr_image = generator.generate_url(url, scale=10)
            
            # Mostrar en el preview
            self.preview_widget.update_qr(qr_image)
            
            # Guardar el contenido actual para exportación
            self.current_qr_content = url
            self.current_qr_type = 'url'
            
            self.statusBar().showMessage("✅ QR generado correctamente", 3000)
            print("✅ QR generado y mostrado en preview")
            
        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(
                self,
                "Error",
                f"❌ Error al generar QR:\n{str(e)}"
            )
            print(f"❌ Error: {e}")
    def generate_qr_from_whatsapp(self, phone, message):
        """
        Generar QR desde el formulario WhatsApp
        
        Args:
            phone: Número de teléfono completo (con código de país)
            message: Mensaje opcional
        """
        self.statusBar().showMessage(f"🎨 Generando QR para WhatsApp: +{phone}", 3000)
        print(f"🎨 Generando QR para WhatsApp: +{phone}")
        
        try:
            # Importar el generador
            from core.qr_generator import QRGenerator
            
            # Crear generador
            generator = QRGenerator()
            
            # Generar QR
            qr_image = generator.generate_whatsapp(phone, message, scale=10)
            
            # Mostrar en el preview
            self.preview_widget.update_qr(qr_image)
            
            # Guardar el contenido para exportación
            # Construir la URL de WhatsApp
            import urllib.parse
            if message:
                message_encoded = urllib.parse.quote(message)
                whatsapp_url = f"https://wa.me/{phone}?text={message_encoded}"
            else:
                whatsapp_url = f"https://wa.me/{phone}"
            
            self.current_qr_content = whatsapp_url
            self.current_qr_type = 'whatsapp'
            
            self.statusBar().showMessage("✅ QR de WhatsApp generado correctamente", 3000)
            print("✅ QR generado y mostrado en preview")
            
        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(
                self,
                "Error",
                f"❌ Error al generar QR de WhatsApp:\n{str(e)}"
            )
            print(f"❌ Error: {e}")

    def generate_qr_from_wifi(self, wifi_string, qr_type):
        """Generar QR desde la pestaña WiFi"""
        self.statusBar().showMessage(f"🎨 Generando QR para WiFi", 3000)
        print(f"🎨 Generando QR para WiFi: {wifi_string[:50]}...")
        
        try:
            # Importar el generador
            from core.qr_generator import QRGenerator
            
            # Crear generador
            generator = QRGenerator()
            
            # Generar QR
            qr_image = generator.generate(wifi_string, scale=10)
            
            # Mostrar en el preview
            self.preview_widget.update_qr(qr_image)
            
            # Guardar el contenido para exportación
            self.current_qr_content = wifi_string
            self.current_qr_type = 'wifi'
            
            self.statusBar().showMessage("✅ QR de WiFi generado correctamente", 3000)
            print("✅ QR generado y mostrado en preview")
            
        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(
                self,
                "Error",
                f"❌ Error al generar QR de WiFi:\n{str(e)}"
            )
            print(f"❌ Error: {e}")

    def on_customization_changed(self, config):
        """
        Manejar cambios en la personalización del QR
        
        Args:
            config: Diccionario con la configuración de personalización
        """
        print(f"🎨 Personalización actualizada: {config}")
        
        # Si hay un QR activo, regenerarlo con los nuevos colores
        if self.current_qr_content:
            self.regenerate_qr_with_customization(config)
    def regenerate_qr_with_customization(self, config):
        """
        Regenerar el QR actual con la personalización aplicada
        
        Args:
            config: Configuración de personalización
        """
        try:
            from core.qr_generator import QRGenerator
            
            # Crear generador con colores personalizados
            generator = QRGenerator()
            
            # Generar QR con colores
            qr_image = generator.generate(
                self.current_qr_content,
                scale=10,
                dark_color=config['pattern_color'],
                light_color=config['background_color'],
                pattern_style=config['pattern_style'],  # ← AGREGAR ESTA LÍNEA
                frame_style=config['frame_style']  # ← AGREGAR ESTA LÍNEA
            )
            
            # Actualizar preview
            self.preview_widget.update_qr(qr_image)
            
            self.statusBar().showMessage("✅ QR actualizado con personalización", 2000)
            print("✅ QR regenerado con personalización")
            
        except Exception as e:
            print(f"⚠️ Error al regenerar QR: {e}")