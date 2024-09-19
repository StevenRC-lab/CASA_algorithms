# Modo de uso:

# - Para customizar: field son las fuentes a las que quieres hacerle split, modifica la lista para que coincida con tus fuentes -> dentro del diccionario, cambia los nombres de las moleculas para que coincida con tus datos, esto solo va a afectar el nombre del outputvis, no afecta el procesamiento de los datos.

# - Busca el directorio con los ms -> Crea un archivo llamado <autosplit.py> con vi o nano -> copia el codigo fuente a ese archivo -> guarda y sal con :wq -> Entra a CASA -> entra <execfile('autosplit.py')>.

# Sientete libre de ignorar los comentarios de esta linea en adelante.

import time

field=['HOPS-30', 'HOPS-43', 'HOPS-71', 'HOPS-133', 'HOPS-139'] # lista de fuentes

spw_dictionary = {
        "shift-H2CO_9-9": '16,52,88,124,160,196,232,268,304,340,376,412,448,484,520,556,592,628,664,700,736,772',
        "shift-H2CO_3-2": '18,54,90,126,162,198,234,270,306,342,378,414,450,486,522,558,594,630,666,702,738,774',
        "CH3OH_5-4": '20,56,92,128,164,200,236,272,308,344,380,416,452,488,524,560,596,632,668,704,740,776',
        "H2CO_3-2": '22,58,94,130,166,202,238,274,310,346,382,418,454,490,526,562,598,634,670,706,742,778',
        "C18O_2-1": '24,60,96,132,168,204,240,276,312,348,384,420,456,492,528,564,600,636,672,708,744,780',
        "13CO_2-1": '26,62,98,134,170,206,242,278,314,350,386,422,458,494,530,566,602,638,674,710,746,782',
        "CH3OH_3-4": '28,64,100,136,172,208,244,280,316,352,388,424,460,496,532,568,604,640,676,712,748,784',
        "CO_2-1": '30,66,102,138,174,210,246,282,318,354,390,426,462,498,534,570,606,642,678,714,750,786',
        "N2Dplus_3-2": '32,68,104,140,176,212,248,284,320,356,392,428,464,500,536,572,608,644,680,716,752,788',
        "continuum": '34,70,106,142,178,214,250,286,322,358,394,430,466,502,538,574,610,646,682,718,754,790'
} # dentro de este diccionario estan las listas de cada linea molecular, por como CASA tiene hecho el parametro de spw, el argumento debe ser la lista completa como un string

inputfile='7m_calibrated_substracted_concatenation.ms'
outputvis='0' 

def wait_completion(): # definicion de la funcion wait_completion, no se ejecuta hasta que se invoca
    log_file=casalog.logfile()
    with open(log_file, 'r') as f:
        log_content=f.read()

    while f'End Task: split' not in log_content:
        time.sleep(10) # 15 secs
        with open(log_file,'r') as f:
            log_content = f.read()

for i in field: # Por cada elemento en la lista field, por cada molecula (line) en el diccionario (spw_dictionary), usa la sublista correspodiente a cada molecula (lists) 
    for line, lists in spw_dictionary.items():
        outputfile=str(i + '_7m_' + line + '_autosplitv2.ms') # concatena y luego convierte en string
        split(vis=inputfile, outputvis=outputfile, spw=lists, field=i, datacolumn='data', keepflags=False)
        wait_completion() # invocacion de la funcion
