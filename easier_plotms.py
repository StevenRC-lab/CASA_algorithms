# Modo de uso:
# Busca el directorio con los ms -> Crea un archivo llamado <easier_plotms.py> con vi o nano -> copia el codigo fuente en ese archivo -> guarda y sal con :wq -> Entra a CASA -> entra <execfile('easier_plotms.py')> -> entra tu ms.

def easier_plotms():
    ms = str(input('Enter measurement_set: '))
    plotms(vis=ms,xaxis='channel',yaxis='amp',avgspw=False,avgtime='1e9',avgscan=True,avgbaseline= True,showgui=True)

easier_plotms();
