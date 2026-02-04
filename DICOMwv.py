import pydicom # lee , modifica y analiza archivos DICOM
import matplotlib.pyplot as plt #permite  mostrar la imagen en pantalla 
from pydicom.data import get_testdata_file


# para cargar el archivo DICOM
dicom_path = get_testdata_file("CT_small.dcm")  # cambia la ruta
ds = pydicom.dcmread(dicom_path) # lee el archivo ,abre el archivo binario, parsea la estructura y devuelve un objeto Dataset

# para mostrar informacion básica
print(ds)

# para mostrar imagenes 
plt.imshow(ds.pixel_array, cmap="gray")  # extrae el tag y lo convierte en un array NumPy, imshow lo dibuja cmap lo vuelve escala de grises 
plt.title("DICOM Viewer") # titulo
plt.axis("off") # oculta los ejes
plt.show() # abre la ventana 


