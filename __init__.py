"""
package_deneme - Python test paketi

Bu paket, Python kütüphanelerinin çalışıp çalışmadığını test etmek için basit fonksiyonlar içerir.
"""

# Test fonksiyonunu import et
from .test_package import test_connection

# Paket versiyonu
__version__ = "0.1.0"

# Paket bilgileri
__author__ = "Enes Atila"
__email__ = ""
__description__ = "Python test paketi"

# Public API - bu fonksiyonlar dışarıdan erişilebilir
__all__ = [
    "test_connection"
]