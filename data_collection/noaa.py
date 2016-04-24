import requests
import os
import re
import glob
from os.path import basename
html = requests.get('http://www.afsc.noaa.gov/RACE/groundfish/survey_data/data.htm').text
os.system('mkdir noaa_zips')
files = re.findall('downloads/.*?\.zip', html)
#print files
for f in files:
    if not basename(f) in os.listdir('noaa_zips'):
        #print 'getting file'
        os.system('wget -O noaa_zips/%s http://www.afsc.noaa.gov/RACE/groundfish/survey_data/%s' % (basename(f), f))
        os.system('unzip noaa_zips/%s -d noaa_zips' % (basename(f)))
os.system('rm noaa_zips/one_big_file.csv')
# first file:
files = glob.glob('noaa_zips/*.csv')
lines = []
with open(files[0]) as f:
    lines = f.read().strip('\n').split('\n')
# now the rest:    
for filepath in files[1:]:
    with open(filepath, 'r') as f:
        lines.extend(f.read().strip().split('\n')[1:])
print len(lines)
print len([l.strip() for l in lines if l.strip()])
with open("noaa_zips/one_big_file.csv", 'w') as f:
    s = '\n'.join([l.strip() for l in lines if l.strip()]).strip()
    import re
    s = s.replace('\n,', ',')
    f.write(s)
