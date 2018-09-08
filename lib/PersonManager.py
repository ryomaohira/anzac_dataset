import csv
class PersonManager:
    csv_files = []
    persons = []

    def __init__(self, file_addresses):
        self.csv_file = file_addresses
        self.getPortraits('CSV/soldier_portraits_australasian_traveller.csv')
        return

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
                name.replace(r, '')
        data['name'] = name

        return data