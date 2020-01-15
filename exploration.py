#%%
import os
folder_name = 'Data'
sub_folder = 'training_set'
path = os.path.join(folder_name,sub_folder)
print(path)

# %%
class Dataset:
    def __init__(self):
        self.all = []

    def add_record(self, id='', group='', raw_text=None):
        self.all.append(Record(id, group, raw_text))
    
    def add_tag(self, id, text_tag):
        try:
            with self.all[id] as record:
                assert not record.labeled, 'already labeled'
                record.add_tag(text_tag)
        except:
            print("Unexpected error")
            


class Record:
    def __init__(self, id='', group='', raw_text=None):
        self.id = id
        self.group = group
        self.raw_text = raw_text
        self.labeled = False
        self.token_text = raw_text.split()
        self.raw_tag = None

    def add_tag(self, raw_text_tag):
        self.labeled = True
        self._add_raw_tag(raw_text_tag)

    def _add_raw_tag(self, raw_text_tag):
        self.raw_tag = raw_text_tag
# %%
dataset = Dataset()
for folder in os.listdir(path):
    sub_path = os.path.join(path,folder)
    for doc_name in os.listdir(sub_path):
        doc_path = os.path.join(sub_path,doc_name)
        with open(doc_path, 'r') as doc:
            dataset.add_record(doc_name, 'train', doc.read())
# %%
len(dataset.all)

# %%
dataset.all[0].raw_text.split('|')

# %%
