# auto tclean for dirty cube
import sys # for exit() method

inputfiles = {
        "HOPS-17":  ['line.ms', 'line.ms', 'line.ms'],
        "HOPS-18":  ['line.ms', 'line.ms', 'line.ms'],
        "HOPS-29":  ['line.ms', 'line.ms', 'line.ms'], # cambiar lo demas por esto, ignora linea del CO
        "HOPS-30":  '05:34:44.0640 -05.41.25.800',
        "HOPS-43":  '05:35:04.5119 -05.35.14.279',
        "HOPS-71":  '05:35:25.6080 -05.07.57.360',
        "HOPS-133": '05:39:05.8319 -07.10.39.359',
        "HOPS-139": '05:38:49.6080 -07.01.17.760',
        "HOPS-140": '05:38:46.2720 -07.01.53.400',
        "HOPS-145": '05:38:43.8479 -07.01.13.079',
        "HOPS-156": '05:38:03.4080 -06.58.15.959',
        "HOPS-160": '05:37:51.0480 -06.47.20.399',
        "HOPS-163": '05:37:17.2799 -06.36.18.360',
        "HOPS-189": '05:35:30.8879 -06.26.31.919',
        "HOPS-193": '05:36:30.2639 -06.01.17.399'
}
source_names = ['name', 'of', 'the', 'source', 'parallel', 'to', 'inputfiles', ...] # Format HOPS-xyz

spws = { # for 7m array
        "13CO" = ['0~6,8~21', '0~21'],
        "C18O" = ['0~6,8~21', '0~21']
}

restfrq_dictionary = { # MHz
        "13CO" : '220398,6842',
        "C18O" : '219560,358',
        "CO"   : '230538'
}
coordiate_dictionary = { # LSRK
        "HOPS-17":  '05:35:07.1759 -05.52.05.879',
        "HOPS-18":  '05:35:05.4960 -05.51.54.359',
        "HOPS-29":  '05:34:49.0560 -05.41.42.000',
        "HOPS-30":  '05:34:44.0640 -05.41.25.800',
        "HOPS-43":  '05:35:04.5119 -05.35.14.279',
        "HOPS-71":  '05:35:25.6080 -05.07.57.360',
        "HOPS-133": '05:39:05.8319 -07.10.39.359',
        "HOPS-139": '05:38:49.6080 -07.01.17.760',
        "HOPS-140": '05:38:46.2720 -07.01.53.400',
        "HOPS-145": '05:38:43.8479 -07.01.13.079',
        "HOPS-156": '05:38:03.4080 -06.58.15.959',
        "HOPS-160": '05:37:51.0480 -06.47.20.399',
        "HOPS-163": '05:37:17.2799 -06.36.18.360',
        "HOPS-189": '05:35:30.8879 -06.26.31.919',
        "HOPS-193": '05:36:30.2639 -06.01.17.399'
}

def wait_completion(): # checks that the task is completed before going to the next source or line
    log_file=casalog.logfile()
    with open(log_file, 'r') as f:
        log_content=f.read()

    while f'End Task: tclean' not in log_content:
        time.sleep(10) # 10 secs
        with open(log_file,'r') as f:
            log_content = f.read()
def auto_mkdir(source_name): # helps with the imagename parameter automatization by formatting the name of the directory in which the tclean output will be placed.
    if   source_name == 'HOPS-17':
        return 'DIRTY_H17'
    elif source_name == 'HOPS-18':
        return 'DIRTY_H18'
    elif source_name == 'HOPS-29':
        return 'DIRTY_H29'
    elif source_name == 'HOPS-30':
        return 'DIRTY_H30'
    elif source_name == 'HOPS-43':
        return 'DIRTY_H43'
    elif source_name == 'HOPS-71':
        return 'DIRTY_H71'
    elif source_name == 'HOPS-133':
        return 'DIRTY_H133'
    elif source_name == 'HOPS-139':
        return 'DIRTY_H139'
    elif source_name == 'HOPS-140':
        return 'DIRTY_H140'
    elif source_name == 'HOPS-145':
        return 'DIRTY_H145'
    elif source_name == 'HOPS-156':
        return 'DIRTY_H156'
    elif source_name == 'HOPS-160':
        return 'DIRTY_H160'
    elif source_name == 'HOPS-163':
        return 'DIRTY_H163'
    elif source_name == 'HOPS-189':
        return 'DIRTY_H189'
    elif source_name == 'HOPS-193':
        return 'DIRTY_H193'
    else:
        print(source_name + ' is not valid source, try checking the source_names list in the source code of this script with a text editor or IDE.')
        sys.exit()

def get_coordinate(source):
        coordinates = coordinate_dictionary[source]
        phasecenter= "ICRS " + coordinates
        return str(phasecenter)
        
abnormal_spw = ["HOPS-30","HOPS-140","HOPS-156","HOPS-160","HOPS-163"]

def get_spw(source, line):
        if source not in abnormal_spw:
                return spws[line][0]
        else:
                return spws[line][1]
        
        
#def data_input():
 #   CELL = '1.00arcsec'
 #   NCHAN = 1024
 #   Vmax = # Vmax, use this variable for start parameter
 #   Vmin = # Vmin
 #   width = -((Vmax + Vmin)/nchan) # Vmin must be written in positive
 #   array = '7m'
def dirty_tclean(line)
        for source, i in inputfiles.items(): #source tiene el key (el nombre de la lista) en ese momento, i contiene el valor de los elementos (las listas en si)
                dir = auto_mkdir(source)
                phasecenter = get_coordinate(source)
                spw = get_spw(source, line)
                restfrq = restfrq_dictionary[source]
                tclean_output = dir + '/' + source + '_7m_' + line + '_contsub_cube'
                for ms in i:
                        vis = ms
                        
                
                
for i in inputfiles: 
    visibility = inputfiles[i][1] # numero corresponde al subindice de la lista de measurement sets de las fuentes del diccionario "inputfiles"
    tclean_output = auto_mkdir(i) + '/' + i + '_' + array + '_' + line + '_contsub_cube'

