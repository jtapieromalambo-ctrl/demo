#!/usr/bin/env python
"""Utilidad de Django para ejecutar tareas administrativas."""
import os
import sys


def main():
    """Configura el entorno de Django y ejecuta comandos administrativos."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configuracion.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as error_importacion:
        raise ImportError(
            "No se pudo importar Django. Verifica que esté instalado y activo en tu entorno virtual."
        ) from error_importacion
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
