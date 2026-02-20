# DICOMvw
Un visor simple de imágenes médicas en formato DICOM, desarrollado en Python. Proyecto de aprendizaje en la intersección de la informática biomédica y la seguridad de sistemas de salud. 

¿Que es DICOM?
Es el estandar internacional para almacenamiento y transmisión de imagenes médicas (RX, CT, IGT)
cada archivo DICOM (.dcm) contiene datos de la imagen; como escala de grises  y metadatos clínicos , como nombre del paciente, modalidad, fecha , institución donde se realizo el examen , entro otros

Funcionalidades 
* Carga archivos .dcm locales o para probar
* Muestra metadatos clínicos
* Estandariza la imagen para su correcta visualización
* Identifica errores para archivos no encontrados o invalidos

Instalación 
* Python 3.8 o superior

Pasos
* bash
  #1. Clona el repositorio
  git clone https://github.com/tu-usuario/dicom-viewer.git
  cd dicom-viewer

  # 2. (Opcional) Crea un entorno virtual
  python -m venv venv
  source venv/bin/activate        # Linux/macOS
  venv\Scripts\activate           # Windows

  # 3. Instala las dependencias
  pip install -r requirements.txt




