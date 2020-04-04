from csv import reader
import csv

user = {}
wahana = {}
pembelian_tiket = {}
kepemilikan_tiket = {}
penggunaan_tiket = {}
refund_tiket = {}
kritik_dan_saran = {}


def loadFile():
    global user
    global wahana
    global pembelian_tiket
    global kepemilikan_tiket
    global penggunaan_tiket
    global refund_tiket
    global kritik_dan_saran
    
    
    with open('file/user.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        user["Column"] = header
        user["Data"] = []
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                cacheData = {}
                for i in range(len(row)):
                    cacheData[header[i]] = row[i]
                user["Data"].append(cacheData)
    with open('file/wahana.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        wahana["Column"] = header
        wahana["Data"] = []
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                cacheData = {}
                for i in range(len(row)):
                    cacheData[header[i]] = row[i]
                wahana["Data"].append(cacheData)
    with open('file/pembelian_tiket.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        pembelian_tiket["Column"] = header
        pembelian_tiket["Data"] = []
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                cacheData = {}
                for i in range(len(row)):
                    cacheData[header[i]] = row[i]
                pembelian_tiket["Data"].append(cacheData)
    with open('file/kepemilikan_tiket.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        kepemilikan_tiket["Column"] = header
        kepemilikan_tiket["Data"] = []
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                cacheData = {}
                for i in range(len(row)):
                    cacheData[header[i]] = row[i]
                kepemilikan_tiket["Data"].append(cacheData)
    with open('file/penggunaan_tiket.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        penggunaan_tiket["Column"] = header
        penggunaan_tiket["Data"] = []
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                cacheData = {}
                for i in range(len(row)):
                    cacheData[header[i]] = row[i]
                penggunaan_tiket["Data"].append(cacheData)
    with open('file/refund_tiket.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        refund_tiket["Column"] = header
        refund_tiket["Data"] = []
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                cacheData = {}
                for i in range(len(row)):
                    cacheData[header[i]] = row[i]
                refund_tiket["Data"].append(cacheData)
    with open('file/kritik_dan_saran.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        kritik_dan_saran["Column"] = header
        kritik_dan_saran["Data"] = []
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                cacheData = {}
                for i in range(len(row)):
                    cacheData[header[i]] = row[i]
                kritik_dan_saran["Data"].append(cacheData)

def saveFile():
    global user
    global wahana
    global pembelian_tiket
    global kepemilikan_tiket
    global penggunaan_tiket
    global refund_tiket
    global kritik_dan_saran
    with open('file/user.csv', mode='w') as csv_file:
        fieldnames = user["Column"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in user["Data"]:
            writer.writerow(row)
    with open('file/wahana.csv', mode='w') as csv_file:
        fieldnames = wahana["Column"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in wahana["Data"]:
            writer.writerow(row)
    with open('file/pembelian_tiket.csv', mode='w') as csv_file:
        fieldnames = pembelian_tiket["Column"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in pembelian_tiket["Data"]:
            writer.writerow(row)
    with open('file/kepemilikan_tiket.csv', mode='w') as csv_file:
        fieldnames = kepemilikan_tiket["Column"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in kepemilikan_tiket["Data"]:
            writer.writerow(row)
    with open('file/penggunaan_tiket.csv', mode='w') as csv_file:
        fieldnames = penggunaan_tiket["Column"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in penggunaan_tiket["Data"]:
            writer.writerow(row)
    with open('file/refund_tiket.csv', mode='w') as csv_file:
        fieldnames = refund_tiket["Column"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in refund_tiket["Data"]:
            writer.writerow(row)
    with open('file/kritik_dan_saran.csv', mode='w') as csv_file:
        fieldnames = kritik_dan_saran["Column"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in kritik_dan_saran["Data"]:
            writer.writerow(row)