import json
import csv
class realworldapp:
    def __init__(self):
        self.operation=input("which opertion do you want to perform read,write,append=")
        if self.operation=="write":
            file=int(input("in which file\n1.text\n2.csv\n3.json "))
            if file==1:
                self.text_write()
            if file==2:
                self.csv_write()
            if file==3:
                self.json_write()
        if self.operation=="append":
            file = int(input("in which file\n1.text\n2.csv\n3.json "))
            if file == 1:
                self.text_append()
            if file == 2:
                self.csv_append()
            if file == 3:
                self.json_append()
        if self.operation=="read":
            file = int(input("in which file\n1.text\n2.csv\n3.json "))
            if file == 1:
                self.text_read()
            if file == 2:
                self.csv_read()
            if file == 3:
                self.json_read()

    def text_write(self):
        user = int(input("1.list \n,2.dict\n3.set\nenter your choice for write"))
        if user == 1:
            n = int(input("Enter the number of elements: "))
            user_list = []
            for i in range(n):
                element = input(f"Enter element {i + 1}: ")
                user_list.append(element)
            self.new = user_list

        if user == 2:
            user_input = input("Enter key-value pairs separated by commas (key:value format): ")
            key_value_pairs = user_input.split(',')  # Splitting the input string by commas to get pairs
            user_dict = {}

            for pair in key_value_pairs:
                key, value = pair.split(':')  # Splitting each pair by colon to get key and value
                user_dict[key.strip()] = value.strip()
            self.new = user_dict
        if user==3:
            input_values = input("Enter space-separated values to create a set: ")
            values_list = input_values.split()
            user_set = set(values_list)
            self.new=user_set
        f = open("myfile.txt", "w")
        f.write(self.new)
        f.close()

    def text_append(self):
        user = int(input("1.list \n,2.dict\n3.set\nenter your choice for write"))
        if user == 1:
            n = int(input("Enter the number of elements: "))
            user_list = []
            for i in range(n):
                element = input(f"Enter element {i + 1}: ")
                user_list.append(element)
            self.new = user_list

        if user == 2:
            user_input = input("Enter key-value pairs separated by commas (key:value format): ")
            key_value_pairs = user_input.split(',')  # Splitting the input string by commas to get pairs
            user_dict = {}

            for pair in key_value_pairs:
                key, value = pair.split(':')  # Splitting each pair by colon to get key and value
                user_dict[key.strip()] = value.strip()
            self.new = user_dict
        if user == 3:
            input_values = input("Enter space-separated values to create a set: ")
            values_list = input_values.split()
            user_set = set(values_list)
            self.new = user_set
        f = open("myfile.txt", "a")
        f.write(self.new)
        f.close()
    def text_read(self):
        f = open("myfile.txt", 'r')
        print(f.read())
        f.close()
    def csv_write(self):
        user = int(input("1.list \n,2.dict\n3.set\nenter your choice for write"))
        if user == 1:
            n = int(input("Enter the number of elements: "))
            user_list = []
            for i in range(n):
                element = input(f"Enter element {i + 1}: ")
                user_list.append(element)
            self.new = user_list

        if user == 2:
            user_input = input("Enter key-value pairs separated by commas (key:value format): ")
            key_value_pairs = user_input.split(',')  # Splitting the input string by commas to get pairs
            user_dict = {}

            for pair in key_value_pairs:
                key, value = pair.split(':')  # Splitting each pair by colon to get key and value
                user_dict[key.strip()] = value.strip()
            self.new = user_dict
        if user==3:
            input_values = input("Enter space-separated values to create a set: ")
            values_list = input_values.split()
            user_set = set(values_list)
            self.new=user_set

        with open('csvfile.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.new)
        file.close()

    def csv_append(self):
        user = int(input("1.list \n,2.dict\n3.set\nenter your choice for write"))
        if user == 1:
            n = int(input("Enter the number of elements: "))
            user_list = []
            for i in range(n):
                element = input(f"Enter element {i + 1}: ")
                user_list.append(element)
            self.new = user_list

        if user == 2:
            user_input = input("Enter key-value pairs separated by commas (key:value format): ")
            key_value_pairs = user_input.split(',')  # Splitting the input string by commas to get pairs
            user_dict = {}

            for pair in key_value_pairs:
                key, value = pair.split(':')  # Splitting each pair by colon to get key and value
                user_dict[key.strip()] = value.strip()
            self.new = user_dict
        if user == 3:
            input_values = input("Enter space-separated values to create a set: ")
            values_list = input_values.split()
            user_set = set(values_list)
            self.new = user_set

        with open('csvfile.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.new)
        file.close()

    def csv_read(self):
        with open("csvfile.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print(row)
    def json_write(self):
        user = int(input("1.list \n,2.dict\nenter your choice for write"))
        if user == 1:
            n = int(input("Enter the number of elements: "))
            user_list = []
            for i in range(n):
                element = input(f"Enter element {i + 1}: ")
                user_list.append(element)
            self.new=user_list

        if user==2:
            user_input = input("Enter key-value pairs separated by commas (key:value format): ")
            key_value_pairs = user_input.split(',')  # Splitting the input string by commas to get pairs
            user_dict = {}

            for pair in key_value_pairs:
                key, value = pair.split(':')  # Splitting each pair by colon to get key and value
                user_dict[key.strip()] = value.strip()
            self.new=user_dict
        with open('json_demo.json', 'w') as f:
            json.dump(self.new, f)
        f.close()
    def json_append(self):
        user = int(input("1.list \n,2.dict\n,enter your choice for append"))
        if user == 1:
            n = int(input("Enter the number of elements: "))
            user_list = []
            for i in range(n):
                element = input(f"Enter element {i + 1}: ")
                user_list.append(element)
            self.appen =user_list

        if user == 2:
            user_input = input("Enter key-value pairs separated by commas (key:value format): ")
            key_value_pairs = user_input.split(',')  # Splitting the input string by commas to get pairs
            user_dict = {}

            for pair in key_value_pairs:
                key, value = pair.split(':')  # Splitting each pair by colon to get key and value
                user_dict[key.strip()] = value.strip()
            self.appen = user_dict

        with open('json_demo.json', 'a') as f:
            json.dump(self.appen,f)
        f.close()

    def json_read(self):
        with open('json_demo.json', 'r') as f:
            d = json.load(f)
            print(d)
        f.close()


obj=realworldapp()




