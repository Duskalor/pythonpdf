import pdf2image
import pytesseract
import time
import pandas as pd
import re
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

filenames = os.listdir("./datos")
print(filenames)

pdf = f"./datos/{filenames[1]}"

def corregir_fecha(fecha_incorrecta):
    # Usar una expresión regular para extraer los componentes de la fecha
    match = re.match(r'(\d{2})(\d{2})/(\d{4})\s*\|', fecha_incorrecta)
    
    if match:
        dia = match.group(1)
        mes = match.group(2)
        anio = match.group(3)
        
        # Formatear la fecha correcta
        fecha_correcta = f"{dia}/{mes}/{anio}"
        return fecha_correcta
    else:
        # Devolver la fecha original si no coincide con el patrón esperado
        return fecha_incorrecta



def pdfToText(pdf) : 
    input_pdf = pdf2image.convert_from_path(pdf, 900, first_page=1, last_page=1,poppler_path=r'C:\poppler-24.02.0\Library\bin')

    first_image = input_pdf[0]

    width, height = first_image.size

    top_half = (0, 0, width, height // 5)
    # bottom_half = (0, height // 2, width, height)

    top_image = first_image.crop(top_half)
    # bottom_image = first_image.crop(bottom_half)

    # top_image.save(f'page_1_top.jpg', 'JPEG')
    imagetext = pytesseract.image_to_string(top_image)
    # print(imagetext)
    text = imagetext.split("\n")
    # print(text)
    preActividad = [texto for texto in text if "ACTIVIDAD" in texto]
    preDescripcion = [texto for texto in text if "DESCRIPCION" in texto]
    both  = [texto for texto in text if "AREA DE TRABAJO:" in texto]

    regex_fecha  = r"FECHA:\s*(.*)"

    # Buscar todas las fechas en el texto
    matchFECHA = re.search(regex_fecha, both[0])
    if matchFECHA:
        fecha = matchFECHA.group(1)
        fecha = corregir_fecha(fecha)
       

    areaTrabajo = ""
    regexAREATRABAJO = r"AREA DE TRABAJO:\s*(.*)"
    matchAREATRABAJO = re.search(regexAREATRABAJO, both[0])
    if matchAREATRABAJO:
        areaTrabajo = matchAREATRABAJO.group(1)

    regexDescripcion = r"DESCRIPCION:\s*(.*)"
    matchdescripcion = re.search(regexDescripcion, preDescripcion[0])
    if matchdescripcion:
        descripcion = matchdescripcion.group(1)

    regexActividad = r"ACTIVIDAD:\s*(.*)"
    matchActividad = re.search(regexActividad, preActividad[0])
    if matchActividad:
        actividad = matchActividad.group(1)
    

    titulo = f'PROTOCOLO - AREA DE TRABAJO :{areaTrabajo.split("FECHA")[0]} - DESCRIPCIÓN : {descripcion} - ACTIVIDAD : {actividad}'

    comment = ""
    if(len(titulo) > 255) : 
        comment = titulo.split("ACTIVIDAD :").pop()
        titulo = titulo[:250]
        print(comment)
 
    

    fila = [f'{filenames[0].split(".")[0]}', 0, f'{titulo}', 'PROTOCOLO', 'EMITIDO PARA INFORMACIÓN', '', 'LP13692S - FIRENO Ferrobamba fase 5 infra', '0131 - Fuel & Lube Storage & Dispensing', 'N/A', 'N/A', 'CW2253271', 'SUPPLIER DOCS', '5200P-013692 - Pit FB Phase 7 Infrastructure', '', '', '', f'{fecha}', '', '', '', 'FIRENO S.A.C.', f'{comment}', '', '']

    
    df.loc[0] = fila
    


columnas = ['Nro de Documento', 'Revisión', 'Título', 'tipo', 'Status', 'Disciplina', 'Nombre del proyecto', 'Facilites Code Lb', 'Facilites Code CB', 'Área Funcional', 'Oc o Contrato', 'Deliverable Class', 'PPM Código', 'Atributo1', 'Archivo', 'Tamaño de impresión', 'Fecha de emisión', 'Fecha del hito', 'Fecha prevista de envio', 'Fecha de reporte Diario', 'Autor', 'Comentarios', 'N° Tag/Equipo', 'Sustituir']
df = pd.DataFrame(columns=columnas)

start_time = time.time()
pdfToText(pdf)
end_time = time.time()

df.to_excel("datos.xlsx", index=False)


elapsed_time = end_time - start_time
print(f'Tiempo de ejecución: {elapsed_time} segundos')


