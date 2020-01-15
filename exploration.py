# %%
class Dataset:
    def __init__(self):
        self.all = []

    def add_record(self, id='', group='', raw_text=None):
        self.all.append(Record(id, group, raw_text))
    
    def add_tag(self, id, text_tag):
        compt = True
        for i in range(len(self.all)):
            if self.all[i].id == id:
                assert not self.all[i].labeled, 'already labeled'
                self.all[i].add_tag(text_tag)
                compt = False
        if compt:
            print('Id didn t find')
            


class Record:
    def __init__(self, id='', group='', raw_text=None):
        self.id = id
        self.group = group
        self.raw_text = raw_text
        self.labeled = False
        self.raw_tag = None

    def add_tag(self, raw_text_tag):
        self.labeled = True
        self._add_raw_tag(raw_text_tag)
    
    def tokenize(self):
        lignes = self.raw_text.split('\n')
        token_text = []
        for lig in lignes:
            if lig:
                token_text.append([Word(tok) for tok in lig.split()])
            else:
                token_text.append([])

        self.token_text = token_text

    def _add_raw_tag(self, raw_text_tag):
        self.raw_tag = raw_text_tag

class Word:
    def __init__(self, token):
        self.token = token
        self.tag = 'O'

#%%
import os
import re

#%%
folder_name = 'Data'
# %%
dataset = Dataset()

#%%
# sub_folder = 'training_set'
# path = os.path.join(folder_name,sub_folder)
# for folder in os.listdir(path):
#     sub_path = os.path.join(path,folder)
#     for doc_name in os.listdir(sub_path):
#         doc_path = os.path.join(sub_path,doc_name)
#         with open(doc_path, 'r') as doc:
#             dataset.add_record(doc_name, 'train', doc.read())

#%%
sub_folder = 'train.test.released.8.17.09'
sub_path = os.path.join(folder_name,sub_folder)
for doc_name in os.listdir(sub_path):
    doc_path = os.path.join(sub_path,doc_name)
    with open(doc_path, 'r') as doc:
        dataset.add_record(doc_name, 'train', doc.read())
#%%
sub_folder = 'training.ground.truth'
path = os.path.join(folder_name,sub_folder)

for doc_name in os.listdir(path):
    doc_path = os.path.join(path,doc_name)
    with open(doc_path, 'r') as doc:
        id = re.sub('[^0-9]','', doc_name)
        print(id)
        dataset.add_tag(id, doc.read())

# %%
len(dataset.all)

# %%
# for i in range(len(dataset.all)):
#     if dataset.all[i].raw_tag:
#         print('--------------')
#         print(i)
#         print(dataset.all[i].raw_tag)

# %%




# %%
dataset.all[727].tokenize()

# %%
dataset.all[727].token_text[47][0].token

# %%
text_tag = dataset.all[727].raw_tag
print(dataset.all[727].id)
lignes = text_tag.split('\n')
tag = []
for lig in lignes :
    tag.append(lig.split('|| '))

for item in tag:
    for raw_tag in item:
        if len(raw_tag.split('\"')) == 3:
            tag, value, following = raw_tag.split('\"')
            tag = re.sub('=', '', tag)
            if len(following.split()) == 2:
                beg, end = following.split()
                l_beg, n_word_beg = map(int, beg.split(':'))
                l_end, n_word_end = map(int, end.split(':'))
                l_beg -= 1
                value = value.split()
                first_word = dataset.all[727].token_text[l_beg][n_word_beg].token
                if value[0] != first_word.lower():
                    print(f"value : {value}")
                    print(f"first_word : {first_word}")
                    print(f"l_beg : {l_beg}")
                    print(f"n_word_beg : {n_word_beg}")
        else:
            result = raw_tag.split('\"')
            print(f"pb avec tag : {result}")


# %%
tag

# %%
