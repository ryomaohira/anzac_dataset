import csv
class PersonManager:
    csv_files = []
    persons = []
    output = 'outputs/portraits.csv'

    def __init__(self, file_addresses):
        self.csv_file = file_addresses
        self.getPortraits('CSV/soldier_portraits_australasian_traveller.csv')
        self.persons = self.persons[1:]
        self.writeScraperData()
        return

    def writeScraperData(self):
        with open(self.output, mode='w') as f:
            data_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            data_writer.writerow(['rank', 'name', 'url'])

            for p in self.persons:
                data_writer.writerow([p['title'], p['name'], p['portraits'][0]])
            


    def getAdoptASolidier(self):
        return

    def getPortraits(self, c):
        with open(c) as f:
            reader = csv.reader(f, delimiter=',')
            c = 0
            for row in reader:
                data = {}

                temp = row[1].split(' ')
                temp = temp[2:]
                temp = " ".join(temp)

                data = self.getTitleName(temp)
                data['portraits'].append(row[-1])
                self.persons.append(data)
                if data['title'] is None:
                    print(data)

                # print(data)
                if(c == 2000):
                    exit()
                
                c += 1
    

    def getTitleName(self, name):
        data = {
            'title': None,
            'name': None,
            'portraits': []
        }
        # arr = name.split(' ')
        ranks = [
            'Trooper',
            'Corporal',
            'Sergeant',
            'Captain',
            'Private',
            'Gunner',
            'Lance-Corporal',
            'Lieutenant',
            'Sergeant-Major',
            'Paymaster',
            'Lieut.',
            'Brigadier-General',
            'Sapper', 
            'Midshipman', 
            'Signaller', 
            'Driver', 
            'Motor Despatch Rider',
            'Commander', 
            'Rifleman', 
            '2nd Lieutenant',
            '2nd Air-Mechanic',
            'Major',
            'Colonel'
        ]


        for r in ranks:
            if r in name:
                data['title'] = r
                name = name.replace(r, '')
        data['name'] = name

        return data