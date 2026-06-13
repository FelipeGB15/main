curso = 180000
certificado = 12000
Asistencia = float(input("Ingrese Asistencia: "))
Tramo = input("ingrese Tramo (A-B-C-D): ").upper()
desc_curso = 0
desc_certificado = 0
if Asistencia >= 90:
    if Tramo == "A" or Tramo == "B":
        desc_curso = 0.24
    elif Tramo == "C" or Tramo == "D":
        desc_curso = 0.16
if 75 <= Asistencia < 90:
    if Tramo == "A" or Tramo == "B":
        desc_curso = 0.14
    elif Tramo == "C" or Tramo == "D":
        desc_curso = 0.10
if Tramo == "A" or Tramo == "B":
    desc_certificado = 0.10
if Asistencia >= 85:
    desc_certificado += 0.05
Total_curso = curso * (1 - desc_curso)
Total_certificado = certificado * (1 - desc_certificado)
print(f"EL TOTAL DEL CURSO ES: {int(Total_curso)}")
print(f"EL TOTAL DEL CERTIFICADO ES: {int(Total_certificado)}")
print("GRACIAS POR OCUPAR EL PROGRAMA")
