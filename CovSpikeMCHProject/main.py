import pandas as pd
import os

#devide the different mutents from the .fasta to a dictionry
directory = 'input_files/'
mutent_dict = {}
tmp = '!'
for txt in os.listdir(directory):
    if txt.endswith(".fasta"):
      with  open(directory+txt, "r+") as file:
        lis=[]
        for line in file:
            line = line.rstrip("\n")
            if line.startswith(">"):
                tmp = line[1:]
                continue
            if(tmp != '!'):
                mutent_dict[tmp] = line
                tmp = '!'


#splitting RNA to all the possible peptides by certain k
def split_by_k(str, k):
    peptides = []
    pos_counter = 1
    for s in str[:len(str)-k]:
        peptides.append([str[pos_counter-1: pos_counter+k-1], pos_counter, pos_counter+k])
        pos_counter+=1
    return peptides

#returns a list with all peps
def split_for_all_peptides(str):
    return split_by_k(str, 8) + split_by_k(str, 9) + split_by_k(str, 10)

a = split_for_all_peptides(mutent_dict['seq1'])
cols = ['peptide', 'start_pos', 'end_pos']
df = pd.DataFrame(a,columns=cols);

with open('all_peps.txt', 'w') as f:
    for item in split_for_all_peptides(mutent_dict['seq1']):
        f.write("%s\n" % item[0])