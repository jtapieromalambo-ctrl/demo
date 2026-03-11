"""Configuración principal para el proyecto de demo traductor de señas."""
from pathlib import Path
import os


RUTA_BASE = Path(__file__).resolve().parent.parent

CLAVE_SECRETA = os.getenv("DJANGO_SECRET_KEY", "demo-insegura-cambiar-en-produccion")
MODO_DEPURACION = os.getenv("DJANGO_DEBUG", "1") == "1"

HOSTS_PERMITIDOS = ["*"]

APLICACIONES_INSTALADAS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "reconocimiento",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "configuracion.urls"

PLANTILLAS = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "configuracion.wsgi.application"

BASES_DE_DATOS = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": RUTA_BASE / "db.sqlite3",
    }
}

VALIDADORES_CONTRASENA = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

CODIGO_IDIOMA = "es"
ZONA_HORARIA = "America/Mexico_City"
USAR_I18N = True
USAR_TZ = True

URL_ESTATICOS = "static/"
URL_MEDIA = "media/"
RAIZ_MEDIA = RUTA_BASE / "media"

CAMPO_AUTOMATICO_DEFECTO = "django.db.models.BigAutoField"

API_KEY_OPENAI = os.getenv("OPENAI_API_KEY", "")
MODELO_VISION_OPENAI = os.getenv("OPENAI_MODELO_VISION", "gpt-4.1-mini")
MODELO_AUDIO_OPENAI = os.getenv("OPENAI_MODELO_AUDIO", "gpt-4o-mini-tts")
