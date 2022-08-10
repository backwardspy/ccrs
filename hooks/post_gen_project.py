import os

REMOVE_PATHS = [
    '{% if cookiecutter.project_type != "bin" %}src/main.rs{% endif %}',
    '{% if cookiecutter.project_type != "lib" %}src/lib.rs{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
