#Jose Fidencio Vanegas Viera
#Angel Ivan Celaya Garcia
#Julio Cesar Bonilla Hernandez

import argparse
import requests
import os
from lxml import html
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def decode_GPSInfo(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        Nsec = exif['GPSInfo'][2][2]
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        lon = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : lat, "Lon" : lon}

def get_exif(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_GPSInfo(ret)
    return ret

def Metadata_Guardar():
    ruta = "Imagenes"
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print("Metadata para: %s " %(name))
            try:
                exifData = {}
                exif = get_exif(name)
                for metadata in exif: 
                    file = open(str(name)+"Metadata.txt","a")
                    file.write(str(metadata) + ":" + str(exif[metadata]))
                    file.close()
            except:
                import sys, traceback
                traceback.print_exc(file = sys.stdout)

def Imagenes():
    url = a
    print("Extraccion de imagenes")
    print("Obteniendo imagenes de: "+ url)
    
    try:
        response = requests.get(url)  
        parsed_body = html.fromstring(response.text)

        images = parsed_body.xpath('//img/@src')

        print ('Se encontraron %s imagenes' % len(images))
    
        os.system("mkdir Imagenes")
    
        for image in images:
            if image.startswith("http") == False:
                download = url + image
            else:
                download = image
            print(download)
            r = requests.get(download)
            f = open('Imagenes/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()
                
    except Exception as e:
            print(e)
            print ("No se pudo acceder a " + url)
            print ("Intente con otra url")
            pass

description = "Metadata de imagenes extraidas en la web, ingrese en la terminal python (nombre del .py) -link (url)"

parser = argparse.ArgumentParser(description='Scrap y Metadata',

                                 epilog=description,

                                 formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-link", metavar='link', dest='link', help="link de ayuda",

                    required=True)

params = parser.parse_args()

a = (params.link)

Imagenes()
Metadata_Guardar()
