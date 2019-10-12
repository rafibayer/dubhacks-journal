import json
import datetime
import time

DATA_LOCATION = "src/text_data/"

class TextRecorder:


    # string filepath: path to file containing user data as json, may be None
    # if no filepath is passed, data will be loaded for the current day
    # a new file will be created if one doesn't exist for the current day
    def __init__(self, filepath=None):

        self.filepath = filepath

        if self.filepath is not None:
            print("Loading entries from existing file...")

            self.data = self.load_data(self.filepath)

        else:
            print("no existing file path, creating new file...")

            filename = DATA_LOCATION + self.get_date() + ".txt"

            self.filepath = filename
            self.data = dict()


    # string filepath: path to file where data should be written as json
    # writes the recorded data to the specified file
    def serialize_data(self, filepath):
        print(f"saving entries to {filepath}")

        with open(filepath, 'w+') as json_file:
            json.dump(self.data, json_file)



    # string filepath: path to file contain json to populate data for user
    # return dict: dict containing loaded userdata
    # loads the data for the specified filepath into this.data
    def load_data(self, filepath):
        print(f"loading data from file {filepath}")
        with open(filepath) as json_file:
            loaded_data = json.loads(json_file.read())
        
        print(loaded_data)
        return loaded_data


    # populates self.data with json template
    def populate_data_with_template(self):
        print("populating data with template")

        template = dict()
        template["filename"] = self.filepath
        template["date"] = self.get_date()
        template['text_entries'] = dict()
        self.data = template


    # string text: user input text to add to journal as new entry
    # return string: entry_id
    def add_entry(self, text):
        print(f"adding new entry with content: {text}")

        self.data["text_entries"][self.next_id()] = self.get_date_time() + "\n" + text

    # string entry_id: id of entry to change
    # string text: new text for entry
    def edit_entry(self, entry_id, text):
        entry_id = str(entry_id)
        print(f"editing entry with id {entry_id}")

        if entry_id in self.data['text_entries']:
            print("\tEntry found, editing...")
            self.data["text_entries"][entry_id] = self.get_date_time() + "\n" + text
        else:
            print("\tEntry not found")

    # int entry_id: id of entry to add to
    # string text: text to add to entry
    def append_entry(self, entry_id, text):
        entry_id = str(entry_id)
        print(f"appending to entry with id{entry_id}")

        if entry_id in self.data['text_entries']:
            print("\tEntry found, appending...")
            self.data['text_entries'][entry_id] += "\n" + text
        else:
            print("\tEntry not found")
        

    # string or int: id of entry
    # return string: entry with id 
    def get_entry(self, entry_id):
        entry_id = str(entry_id)
        print(f"getting entry with id: {entry_id}")

        if entry_id in self.data['text_entries']:
            print("\tEntry found")
            return self.data['text_entries'][entry_id]
        else:
            print("\tEntry NOT found")
            return f"No entry with id: {entry_id} was found in file f{self.filepath}"

    # string entry_id: the id of the entry to clear
    def clear_entry(self, entry_id):
        entry_id = str(entry_id)
        print(f"clearing entry with id: {entry_id}")

        if entry_id in self.data['text_entries']:
            print("\tEntry found")
            self.data['text_entries'][entry_id] = "==DELETED ENTRY=="
        else:
            print("\tEntry NOT found")
            return f"No entry with id: {entry_id} was found in file f{self.filepath}"
        

    # return string: the number of entries in text_entries
    def get_num_entries(self):
        return str(len(self.data['text_entries']))

    # return string: next availible number as new entry id string
    # same as get_num_entries()
    def next_id(self):
        return self.get_num_entries()


    def print_data(self):
        print(self.data)

    # return string: date and time in '%Y-%m-%d %H-%M-%S' format
    @staticmethod
    def get_date_time():
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')
        return timestamp

    # return string: date in '%Y-%m-%d' format
    @staticmethod
    def get_date():
        ts = time.time()
        datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        return datestamp


tr = TextRecorder()
tr.populate_data_with_template()
tr.add_entry("today was a good day :)")
time.sleep(0.1)
tr.add_entry("today sucked")
print(tr.get_entry(0))
tr.serialize_data(tr.filepath)
tr.load_data(tr.filepath)
print(tr.get_entry(1))
tr.append_entry(1, "jk today was gr8")
print(tr.get_entry(1))
tr.serialize_data(tr.filepath)
time.sleep(0.1)

tr2 = TextRecorder(DATA_LOCATION + tr.get_date() + ".txt")
tr2.add_entry("another entry for the day")
tr2.clear_entry(0)
tr2.serialize_data(tr.filepath)

print(tr2.get_entry(0))
print(tr2.get_entry(1))

print(tr2.data['text_entries'].keys())

