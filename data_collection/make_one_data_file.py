import csv
import glob
data = []
i = 0
all_keys = []
for j, filename in enumerate(glob.glob('fish_data/*.csv')):
    with open(filename, 'rU') as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            d = {k.lower().replace(' ', '_'): v for k, v in row.items()}
            d.update({'filename': filename})
            #try:
            #    r.db('fish').table('fish').insert(d).run(durability='soft', noreply=True)
            #except:
            #    pass
            i += 1
            print i
        for k in d:
            if k not in all_keys:
                all_keys.append(k)
        print j, len(glob.glob('fish_data/*.csv')), filename
        print i
print "getting all keys"
#all_keys = sorted(set().union(*(d.keys() for d in data if d)))
all_keys = sorted(all_keys)
f = open('big_fish_data.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( all_keys )
    for j, filename in enumerate(glob.glob('fish_data/*.csv')):
        with open(filename, 'rU') as f2:
            for row in csv.DictReader(f2, skipinitialspace=True):
                d = {k.lower().replace(' ', '_'): v for k, v in row.items()}
                d.update({'filename': filename})
                rowl = []
                for col in all_keys:
                    rowl.append(d.get(col))
                try:
                    writer.writerow( rowl )
                except:
                    pass
    
finally:
    f.close()
