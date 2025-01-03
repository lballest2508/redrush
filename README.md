# ERP REDRUSH Backend

Este es un proyecto de backend para un sistema ERP (Enterprise Resource Planning). Actualmente, la aplicación incluye la gestión de personas, y se están desarrollando más módulos en el futuro.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Licencia](#licencia)

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- [Python](https://www.python.org/downloads/) (versión 3.10 o superior)
- [pip](https://pip.pypa.io/en/stable/) (gestor de paquetes de Python)
- [Git](https://git-scm.com/downloads) (para clonar el repositorio)

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clonar el Repositorio**

   Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

   ```bash
   git clone https://github.com/lballest2508/redrush.git

2. **Crear y Activar un Entorno Virtual**

    Navega al directorio del proyecto y crea un entorno virtual:

    ```bash
    cd redrush
    python -m venv venv
    ```

    Activa el entorno virtual:

    - En Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - En macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

3. **Instalar Dependencias**

    Con el entorno virtual activado, instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar la aplicación, asegúrate de tener el entorno virtual activado y ejecuta el siguiente comando:

```bash
python manage.py runserver
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.