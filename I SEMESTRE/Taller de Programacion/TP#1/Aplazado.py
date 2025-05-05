import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def procesarCsv(nombreArchivo):
    """Procesa el CSV y filtra estudiantes con 2 o 3 aplazos usando listas"""
    estudiantes = []
    totalEstudiantes = 0
    aplazos2 = 0
    aplazos3 = 0
    notasAplazos = []
    
    with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if len(fila) < 7:
                continue
                
            totalEstudiantes += 1
            
            try:
                notasStr = fila[6].strip('()')
                partes = [p.strip() for p in notasStr.split(',')]
                nota1, nota2, nota3 = map(float, partes[:3])
            except:
                continue
                
            aplazos = sum(1 for nota in [nota1, nota2, nota3] if nota < 70)
            
            if aplazos >= 2:
                # Creamos una tupla con los datos del estudiante
                estudiante = (f"{fila[0]} {fila[1]} {fila[2]}",  # Nombre completo
                    fila[4],  # Carné
                    fila[5],  # Correo
                    (nota1, nota2, nota3),  # Notas como tupla
                    aplazos)  # Cantidad de aplazos
                if aplazos == 2: 
                    aplazos2 += 1
                else: 
                    aplazos3 += 1
                notasAplazos.extend([nota1, nota2, nota3])
                estudiantes.append(estudiante)
    
    # Calculamos mínimos y máximos
    nota_min = min(notasAplazos) if notasAplazos else 0
    nota_max = max(notasAplazos) if notasAplazos else 0
    
    return (estudiantes, totalEstudiantes, aplazos2, aplazos3, nota_min, nota_max)

def generarReportePdf(datos, nombreSalida):
    """Genera el PDF usando tuplas y listas"""
    doc = SimpleDocTemplate(nombreSalida, pagesize=letter)
    elementos = []
    estilos = getSampleStyleSheet()
    
    # Estilo para el título
    estiloTitulo = ParagraphStyle('Titulo',
        parent=estilos['Title'],
        fontSize=18,
        alignment=1,
        spaceAfter=20)
    elementos.append(Paragraph("Reporte de Estudiantes con 2 o más Aplazos", estiloTitulo))
    
    # Tabla de datos
    if datos[0]:  # datos[0] = lista de estudiantes
        encabezados = ['Nombre', 'Carné', 'Correo', 'Nota 1', 'Nota 2', 'Nota 3']
        tablaDatos = [encabezados]
        
        for estudiante in datos[0]:
            fila = [estudiante[0],  # Nombre
                estudiante[1],  # Carné
                estudiante[2],  # Correo
                f"{estudiante[3][0]:.1f}",  # Nota 1
                f"{estudiante[3][1]:.1f}",  # Nota 2
                f"{estudiante[3][2]:.1f}"]   # Nota 3
            tablaDatos.append(fila)
        
        tabla = Table(tablaDatos, colWidths=[1.8*inch, 1*inch, 2.2*inch, 0.7*inch, 0.7*inch, 0.7*inch])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#4B6C9E')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#E0EAF1')),
            ('GRID', (0,0), (-1,-1), 1, colors.black)]))
        elementos.append(tabla)
        elementos.append(Spacer(1, 0.5*inch))
    
    # Estadísticas finales
    estiloEstadisticas = ParagraphStyle(
        'Estadisticas',
        parent=estilos['Normal'],
        fontSize=12,
        leading=14,
        spaceBefore=20)
    
    textoEstadisticas = [
        f"Total de estudiantes en BD: {datos[1]}",
        f"Estudiantes con 2 aplazos: {datos[2]} ({(datos[2]/datos[1]*100):.1f}%)",
        f"Estudiantes con 3 aplazos: {datos[3]} ({(datos[3]/datos[1]*100):.1f}%)",
        f"Nota más baja en aplazos: {datos[4]:.1f}",
        f"Nota más alta en aplazos: {datos[5]:.1f}"]
    
    for texto in textoEstadisticas:
        elementos.append(Paragraph(texto, estiloEstadisticas))
    
    doc.build(elementos)

# Uso del código
datos = procesarCsv('BasedeDatos.csv')
generarReportePdf(datos, 'ReporteAplazados.pdf')