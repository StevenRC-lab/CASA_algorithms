# auto tclean for dirty cube
import sys # for exit() method
import time

inputfiles = { # source = "x": i = [x,y,z] # Ahora para C18O 
        "HOPS-17":  ['HOPS-17_12m_13CO2-1_ms_contsub'], # 'HOPS_17_7m_C18O_2-1.ms'],
        "HOPS-18":  ['HOPS-18_12m_13CO2-1_ms_contsub'], # 'HOPS_18_7m_C18O_2-1.ms'],
        "HOPS-29":  ['HOPS-29_12m_13CO2-1_ms_contsub'], # cambiar lo demas por esto, ignora linea del CO
        "HOPS-30":  ['HOPS-30_12m_13CO2-1_ms_contsub'],
        "HOPS-43":  ['HOPS-43_12m_13CO2-1_ms_contsub'],
        "HOPS-71":  ['HOPS-71_12m_13CO2-1_ms_contsub'],
        "HOPS-133": ['HOPS-133_12m_13CO2-1_ms_contsub'],
        "HOPS-139": ['HOPS-139_12m_13CO2-1_ms_contsub'],
        "HOPS-140": ['HOPS-140_12m_13CO2-1_ms_contsub'],
        "HOPS-145": ['HOPS-145_12m_13CO2-1_ms_contsub'],
        "HOPS-156": ['HOPS-156_12m_13CO2-1_ms_contsub'],
        "HOPS-160": ['HOPS-160_12m_13CO2-1_ms_contsub'],
        "HOPS-163": ['HOPS-163_12m_13CO2-1_ms_contsub'],
        "HOPS-189": ['HOPS-189_12m_13CO2-1_ms_contsub'],
        "HOPS-193": ['HOPS-193_12m_13CO2-1_ms_contsub']
        #"HOPS-17":  ['HOPS-17_12m_C18O_ms_contsub'], # 'HOPS_17_7m_C18O_2-1.ms'],
        #"HOPS-18":  ['HOPS-18_12m_C18O_ms_contsub'], # 'HOPS_18_7m_C18O_2-1.ms'],
        #"HOPS-29":  ['HOPS-29_12m_C18O_ms_contsub'], # cambiar lo demas por esto, ignora linea del CO
        #"HOPS-30":  ['HOPS-30_12m_C18O_ms_contsub'],
        #"HOPS-43":  ['HOPS-43_12m_C18O_ms_contsub'],
        #"HOPS-71":  ['HOPS-71_12m_C18O_ms_contsub'],
        #"HOPS-133": ['HOPS-133_12m_C18O_ms_contsub'],
        #"HOPS-139": ['HOPS-139_12m_C18O_ms_contsub'],
        #"HOPS-140": ['HOPS-140_12m_C18O_ms_contsub'],
        #"HOPS-145": ['HOPS-145_12m_C18O_ms_contsub'],
        #"HOPS-156": ['HOPS-156_12m_C18O_ms_contsub'],
        #"HOPS-160": ['HOPS-160_12m_C18O_ms_contsub'],
        #"HOPS-163": ['HOPS-163_12m_C18O_ms_contsub'],
        #"HOPS-189": ['HOPS-189_12m_C18O_ms_contsub'],
        #"HOPS-193": ['HOPS-193_12m_C18O_ms_contsub']
        #"HOPS-17":  ['HOPS-17_12m_CO2-1_contsub'], # 'HOPS_17_7m_C18O_2-1.ms'],
        #"HOPS-18":  ['HOPS-18_12m_CO2-1_contsub'], # 'HOPS_18_7m_C18O_2-1.ms'],
        #"HOPS-29":  ['HOPS-29_12m_CO2-1_contsub'], # cambiar lo demas por esto, ignora linea del CO
        #"HOPS-30":  ['HOPS-30_12m_CO2-1_contsub'],
        #"HOPS-43":  ['HOPS-43_12m_CO2-1_contsub'],
        #"HOPS-71":  ['HOPS-71_12m_CO2-1_contsub'],
        #"HOPS-133": ['HOPS-133_12m_CO2-1_contsub'],
        #"HOPS-139": ['HOPS-139_12m_CO2-1_contsub'],
        #"HOPS-140": ['HOPS-140_12m_CO2-1_contsub'],
        #"HOPS-145": ['HOPS-145_12m_CO2-1_contsub'],
        #"HOPS-156": ['HOPS-156_12m_CO2-1_contsub'],
        #"HOPS-160": ['HOPS-163_12m_CO2-1_contsub'],
        #"HOPS-163": ['HOPS-163_12m_CO2-1_contsub'],
        #"HOPS-189": ['HOPS-189_12m_CO2-1_contsub'],
        #"HOPS-193": ['HOPS-193_12m_CO2-1_contsub']
      
}
# source_names = ['name', 'of', 'the', 'source', 'parallel', 'to', 'inputfiles', ...] # Format HOPS-xyz

spws = { # for 7m array, abnormal spws in [1]
        "13CO" : ['0~6,8~21', '0~21'],
        "C18O" : ['0~6,8~21', '0~21'],
        "CO"   : ['0~6,8~21', '0~21']
}

restfrq_dictionary = { # GHz, 
        "13CO" : '220.3986842GHz',
        "C18O" : '219.560358GHz',
        "CO"   : '230.538000GHz'
}
coordinate_dictionary = { # LSRK
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



def wait_completion(): # checks that the task is completed before going to the next source or line, usa readline
    log_file=casalog.logfile()
    with open(log_file, 'r') as f:
        log_content=f.read() # O(n)

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
        phasecenter= 'ICRS ' + coordinates
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

other_parameters = { # para toda fuente en este diccionario, cada subindice representa: [0] = start, [1] = vmin, [2] = width
        "13CO" : ['50km/s', '34km/s', '-0.08225km/s'],
        "C180" : ['42.5km/s', '42.5km/s', '-0.08225km/s']

}
def dirty_tclean(line):
        minpb = 0.2
        cell = '0.17arcsec'
        imsize = 432
        nchan =  -1 # 1016
        start =  '' # other_parameters[line][0] # ''
        width =  '' # other_parameters[line][2] # ''

        for source, i in inputfiles.items(): #source tiene el key (el nombre de la lista) en ese momento, i contiene el valor de los elementos (las listas en si)
                restfreq = restfrq_dictionary[line]

                for ms in i:
                        vis = ms
                        dir = auto_mkdir(source) + "_12m_" + line
                        phasecenter = get_coordinate(source)
                        spw = '0~8' # get_spw(source, line)
                        prename = dir + '/' + source + '_12m_' + line + 'auto_contsub_cube'
                        tclean(vis=vis,imagename=prename + '_dirty',gridder='mosaic',deconvolver='hogbom',pbmask=minpb,imsize=imsize,cell=cell,spw=spw,weighting='briggsbwtaper',
                               robust=0.5,phasecenter=phasecenter,specmode='cube',width=width,start=start,nchan=nchan,restfreq=restfreq,outframe='LSRK',veltype='radio',restoringbeam='common',mask='',
                               niter=0,interactive=False)
                        wait_completion()

line = str(input("Enter line: "))

dirty_tclean(line)
