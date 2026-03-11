# Demo Django: reconocimiento de lengua de señas a voz

Proyecto **pequeño** en Django que:
1. Recibe una imagen de una seña.
2. Usa un modelo multimodal de OpenAI para inferir el texto en español.
3. Convierte ese texto a voz MP3 con OpenAI TTS.

## Requisitos
- Python 3.10+
- Una API key de OpenAI

## Instalación rápida
```bash
cd traductor_senas
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Variables de entorno
```bash
export OPENAI_API_KEY="tu_api_key"
export DJANGO_DEBUG="1"
```

Opcionales:
- `OPENAI_MODELO_VISION` (default: `gpt-4.1-mini`)
- `OPENAI_MODELO_AUDIO` (default: `gpt-4o-mini-tts`)

## Ejecutar
```bash
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`.

## Notas de demo
- Todas las variables del código se nombraron en español.
- Si no defines `OPENAI_API_KEY`, se mostrará un texto de ejemplo y no se generará audio real.
