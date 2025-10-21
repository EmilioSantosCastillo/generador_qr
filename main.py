"""
Generador de Códigos QR Personalizados
Punto de entrada principal de la aplicación

Autor: Tu Nombre
Versión: 1.0.0
"""

import sys
import signal
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt, QTimer

# Importar configuración
import config


def signal_handler(sig, frame):
    """Maneja la señal de interrupción (Ctrl+C)"""
    print("\n\n👋 Aplicación cerrada por el usuario")
    QApplication.quit()
    sys.exit(0)


def main():
    """
    Función principal que inicia la aplicación
    """
    # Configurar manejo de Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Crear la aplicación Qt
    app = QApplication(sys.argv)
    
    # Configurar propiedades de la aplicación
    app.setApplicationName(config.APP_NAME)
    app.setApplicationVersion(config.APP_VERSION)
    app.setOrganizationName(config.APP_ORGANIZATION)
    
    # Habilitar high DPI scaling (para pantallas de alta resolución)
    try:
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
    except AttributeError:
        pass  # No disponible en esta versión
    
    # Por ahora, solo mostramos un mensaje
    print("=" * 60)
    print(f"🚀 {config.APP_NAME} v{config.APP_VERSION}")
    print("=" * 60)
    print()
    print("✅ Aplicación iniciada correctamente")
    print(f"📁 Directorio base: {config.BASE_DIR}")
    print(f"🎨 Tipos de QR disponibles: {len(config.QR_TYPES)}")
    print()
    print("⚠️  La interfaz gráfica aún no está implementada")
    print("   Presiona Ctrl+C para salir o cierra esta ventana")
    print()
    
    # Timer para procesar eventos (permite que Ctrl+C funcione)
    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)
    
    # TODO: Aquí irá la ventana principal cuando la creemos
    # from ui.main_window import MainWindow
    # window = MainWindow()
    # window.show()
    
    # Ejecutar la aplicación
    return app.exec()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n👋 Aplicación cerrada por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)