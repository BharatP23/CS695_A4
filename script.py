import csv
import time

def read_file_of_ksm(file_path):
    with open(file_path, 'r') as file:
        return int(file.read())
    
if name == "main":
    files_of_KSM = ["/sys/kernel/mm/ksm/pages_shared", "/sys/kernel/mm/ksm/general_profit"]
    first_line = ["pages_shared", "general_profit"]
    
    with open("data_of_KSM.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(first_line)

    while True:
        current_data = []
        for f in files_of_KSM:
            current_data.append(read_file_of_ksm(f))

        with open("data_of_KSM.csv", 'a', newline='') as r:
            writer = csv.writer(r)
            writer.writerow(current_data)
        time.sleep(5)
