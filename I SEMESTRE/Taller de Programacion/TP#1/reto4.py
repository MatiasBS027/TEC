import csv
import re


def calcularEstado(notas):
    """
    Función: calcula si el estudiante está aprobado, reprobado o en reposición
    Entradas:
    - notas(tupla) = son las tres notas de las evaluaciones y su resultado
    Salidas:
    - devuelve el estado del estudiante
    """
    if float(notas[-5:-1]) > 70:
        return "Aprobado"
    elif float(notas[-5:-1]) > 60:
        return "Reposición"
    else:
        return "Reprobado"


def calcularAnno(carne):
    """
    Función: calcula si el estudiante el año de ingreso del estudiante
    Entradas:
    - carne(str) = es el carné estudiantil del que se saca el año
    Salidas:
    - anno(str) = el el año de ingreso del estudiante
    """
    anno = carne[:4]
    print(anno)
    return anno


def calcularNotas(notas):
    """
    Función: saca las notas de la tupla notas
    Entradas:
    - notas(tupla) = son las tres notas de las evaluaciones y su resultado
    Salidas:
    - n(str) = son las notas extraídas de la tupla
    """
    n = ""
    for j in notas:
        if re.match("\d|,|\s|\.", j):
            n += f"{j}"
    return n


def respaldarXML():
    """
    Función: genera el respaldo de la base de datos en formato XML
    Entradas: n/a
    Salidas:
    - reporte.xml(archivo xml) = es el archivo reporte en formato xml de la base de datos
    """
    with open(
        "BDDinamica.csv", "r", newline="", encoding="utf-8"
    ) as archivoAbierto:  # abre y lee la base de datos
        lector = csv.reader(archivoAbierto)
        filas = list(lector)

    xml = "<Estudiantes>\n\t"  # crea el xml
    c2021 = "<Generacion anno=2021>\n\t\t"
    c2022 = "<Generacion anno=2022>\n\t\t"
    c2023 = "<Generacion anno=2023>\n\t\t"
    c2024 = "<Generacion anno=2024>\n\t\t"
    c2025 = "<Generacion anno=2025>\n\t\t"

    for i in filas:
        n, a1, a2, genero, carne, correo, notas = i
        estado = calcularEstado(notas)
        anno = calcularAnno(carne)

        match anno:  # acomoda los enstudiantes dependiendo el año
            case "2021":
                c2021 += f"\t<Estudiante carne={carne}>\n\t\t\t<nombre>{n} {a1} {a2}</nombre>\n\t\t\t<genero>{genero}</genero>\n\t\t\t<correo>{correo}</correo>\n\t\t\t<notas>{calcularNotas(notas)}</notas>\n\t\t\t<estado>{calcularEstado(notas)}</estado>\n\t\t</Estudiante>\n\t"
            case "2022":
                c2022 += f"\t<Estudiante carne={carne}>\n\t\t\t<nombre>{n} {a1} {a2}</nombre>\n\t\t\t<genero>{genero}</genero>\n\t\t\t<correo>{correo}</correo>\n\t\t\t<notas>{calcularNotas(notas)}</notas>\n\t\t\t<estado>{calcularEstado(notas)}</estado>\n\t\t</Estudiante>\n\t"
            case "2023":
                c2023 += f"\t<Estudiante carne={carne}>\n\t\t\t<nombre>{n} {a1} {a2}</nombre>\n\t\t\t<genero>{genero}</genero>\n\t\t\t<correo>{correo}</correo>\n\t\t\t<notas>{calcularNotas(notas)}</notas>\n\t\t\t<estado>{calcularEstado(notas)}</estado>\n\t\t</Estudiante>\n\t"
            case "2024":
                c2024 += f"\t<Estudiante carne={carne}>\n\t\t\t<nombre>{n} {a1} {a2}</nombre>\n\t\t\t<genero>{genero}</genero>\n\t\t\t<correo>{correo}</correo>\n\t\t\t<notas>{calcularNotas(notas)}</notas>\n\t\t\t<estado>{calcularEstado(notas)}</estado>\n\t\t</Estudiante>\n\t"
            case "2025":
                c2025 += f"\t<Estudiante carne={carne}>\n\t\t\t<nombre>{n} {a1} {a2}</nombre>\n\t\t\t<genero>{genero}</genero>\n\t\t\t<correo>{correo}</correo>\n\t\t\t<notas>{calcularNotas(notas)}</notas>\n\t\t\t<estado>{calcularEstado(notas)}</estado>\n\t\t</Estudiante>\n\t"

    c2021 += "</Generacion>\n\t"
    c2022 += "</Generacion>\n\t"
    c2023 += "</Generacion>\n\t"
    c2024 += "</Generacion>\n\t"
    c2025 += "</Generacion>\n"
    xml += f"{c2021}{c2022}{c2023}{c2024}{c2025}</Estudiantes>"  # mete todo al xml
    print(xml)
    with open("reporte.xml", "w") as archivoXml:  # crea el archivo y lo mete todo
        archivoXml.write(xml)


respaldarXML()
