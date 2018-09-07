import csv

class WW1Photographs:
    csv_file = "CSV/wwi_photographs.csv"
    buckets = {
        'ship':[],
        'person':[],
        'place':[],
        'event':[],
        'other':[]
    }
    keywords = {
        'ship':[' ship ','H.M.A.S', 'HMAS', 'HMS', 'H.M.S'],
        'person':['Gen','Sir', 'Matron', 'Lady', 'Capt', 'Lt', 'Major', 'Private'],
        'place':['Cove', 'Villa', 'Gallipoli', 'camp', 'memorial', 'Hospital'],
        'event':['Australia Day', 'march', 'inspection', 'presentation']
    }

    def __init__(self):
        return

    def compile(self):
        with open(self.csv_file) as f:
            reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in reader:
                if any(x in row[7] for x in self.keywords['ship']):
                    self.buckets['ship'].append(row)
        for i in self.buckets['ship']:
            print(i[7])
        return

    def search(self, keyword):
        results = []
        with open(self.csv_file) as f:
            reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in reader:
                #print(row[0])
                data = "".join(row)
                if(keyword in data):
                    results.append(row)
        return results

    def searchPerson(self, name):
        results = []
        with open(self.csv_file) as f:
            reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in reader:
                #print(row[0])
                if(name in row[3]):
                    results.append(row)
        return results

    def searchLocation(self, location):
        results = []
        with open(self.csv_file) as f:
            reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in reader:
                #print(row[0])
                if(name in row[3]):
                    results.append(row)
        return results


    