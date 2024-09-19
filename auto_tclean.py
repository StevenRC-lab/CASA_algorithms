# auto tclean for dirty cube
import sys # for exit() method

inputfiles = {
        "HOPS-17":  ['line.ms', 'line.ms', 'line.ms'],
        "HOPS-18":  ['line.ms', 'line.ms', 'line.ms'],
        "HOPS-29":  ['line.ms', 'line.ms', 'line.ms'], # cambiar lo demas por esto
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

spws = { # spw de ejemplo
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
        return 'CLEAN_H17'
    elif source_name == 'HOPS-18':
        return 'CLEAN_H18'
    elif source_name == 'HOPS-29':
        return 'CLEAN_H29'
    elif source_name == 'HOPS-30':
        return 'CLEAN_H30'
    elif source_name == 'HOPS-43':
        return 'CLEAN_H43'
    elif source_name == 'HOPS-71':
        return 'CLEAN_H71'
    elif source_name == 'HOPS-133':
        return 'CLEAN_H133'
    elif source_name == 'HOPS-139':
        return 'CLEAN_H139'
    elif source_name == 'HOPS-140':
        return 'CLEAN_H140'
    elif source_name == 'HOPS-145':
        return 'CLEAN_H145'
    elif source_name == 'HOPS-156':
        return 'CLEAN_H156'
    elif source_name == 'HOPS-160':
        return 'CLEAN_H160'
    elif source_name == 'HOPS-163':
        return 'CLEAR_H163'
    elif source_name == 'HOPS-189':
        return 'CLEAR_H189'
    elif source_name == 'HOPS-193':
        return 'CLEAR_H193'
    else:
        print(source_name + ' is not valid source, try checking the source_names list in the source code of this script with a text editor or IDE.')
        sys.exit()
      
def data_input():
    CELL = '1.00arcsec'
    NCHAN = 1024
    Vmax = # Vmax, use this variable for start parameter
    Vmin = # Vmin
    width = -((Vmax + Vmin)/nchan) # Vmin must be written in positive
    array = '7m'

for i in inputfiles:
    visibility = inputfiles[i][1] # numero corresponde al subindice de la lista de measurement sets de las fuentes del diccionario "inputfiles"
    tclean_output = auto_mkdir(i) + '/' + i + '_' + array + '_' + line + '_contsub_cube' + '_dirty'

