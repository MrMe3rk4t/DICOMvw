import pydicom
import matplotlib.pyplot as plt
import numpy as np
from pydicom.data import get_testdata_file

def load_dicom(path):
  #Carga un archivo DICOM y maneja errores básicos.
    try:
        ds = pydicom.dcmread(path)
        return ds
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {path}")
        return None
    except pydicom.errors.InvalidDicomError:
        print("Error: El archivo no es un DICOM válido.")
        return None

def show_metadata(ds):
    #Muestra metadatos clínicos clave.
    tags = {
        "Paciente":       getattr(ds, "PatientName", "N/A"),
        "Modalidad":      getattr(ds, "Modality", "N/A"),
        "Fecha estudio":  getattr(ds, "StudyDate", "N/A"),
        "Institución":    getattr(ds, "InstitutionName", "N/A"),
        "Filas x Cols":   f"{getattr(ds, 'Rows', '?')} x {getattr(ds, 'Columns', '?')}",
    }
    print("\n=== Metadatos DICOM ===")
    for key, val in tags.items():
        print(f"  {key}: {val}")
    print("=" * 22)

def normalize_image(pixel_array):
    """Normaliza el array a rango 0-255 para visualización correcta."""
    pmin, pmax = pixel_array.min(), pixel_array.max()
    return ((pixel_array - pmin) / (pmax - pmin) * 255).astype(np.uint8)

def show_image(ds):
    """Muestra la imagen DICOM normalizada."""
    if not hasattr(ds, "PixelData"):
        print("Este archivo no contiene datos de imagen.")
        return
    
    image = normalize_image(ds.pixel_array)
    
    plt.figure(figsize=(6, 6))
    plt.imshow(image, cmap="gray")
    plt.title(f"DICOM Viewer — {getattr(ds, 'Modality', 'Desconocido')}")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

# --- Main ---
if __name__ == "__main__":
    dicom_path = get_testdata_file("CT_small.dcm")
    ds = load_dicom(dicom_path)
    
    if ds:
        show_metadata(ds)
        show_image(ds)


