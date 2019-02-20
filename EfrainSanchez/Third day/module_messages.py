def message(year):
    etapa = ""
    if year<=12:etapa="NIÑO"
    elif(year>=13 and year <=17): etapa="ADOLESCENTE"
    elif(year>=18 and year<=29):etapa="JOVEN"
    else:etapa="ADULTO"
    return etapa