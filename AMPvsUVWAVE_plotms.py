# Modo de uso:
# Busca el directorio con los ms -> Crea un archivo llamado <AMPvsUVWAVE_plotms.py> con vi o nano -> copia el codigo fuente en ese archivo -> guarda y sal con :wq -> Entra a CASA -> entra <execfile('easier_plotms.py')> -> entra tu ms.

def AMPvsUVWAVE_plotms():
    ms = str(input('Enter measurement_set: '))
    plotms(vis=ms,xaxis='uvwave',yaxis='amp', avgchannel='10000', avgspw=False,avgtime='1e9',avgscan=False,coloraxis='field',showgui=True)

AMPvsUVWAVE_plotms();
