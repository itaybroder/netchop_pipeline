import pandas as pd
import os

from netchop import create_dataframe, feed_to_Netchop
from MHCpan import split_for_all_peptides

#devide the different mutents from the .fasta to a dictionry
directory = '/home/itaybroder/Documents/GitHub/CovidResearch/CovSpikeMCHProject/input_files'
mutent_dict = {}
tmp = '!'
for txt in os.listdir(directory):
    if txt.endswith(".fasta"):
      with  open(directory+'/'+txt, "r+") as file:
        lis=[]
        for line in file:
            line = line.rstrip("\n")
            if line.startswith(">"):
                tmp = line[1:]
                continue
            if(tmp != '!'):
                mutent_dict[tmp] = line
                tmp = '!'

#choose you can choose the RNA either from here or through the .fasta file
#mutent_dict = {
#    'seq' : '',
#    'mutent': ''
#}

def netchop_mutation_pipeline(mutation_dict):  
    a1 = split_for_all_peptides(mutent_dict['seq1'])
    cols1 = ['peptide', 'start_pos','end_pos']
    df1 =  pd.DataFrame(a1, columns=cols1)
    df1["Chopped"] = ''
    a2 = split_for_all_peptides(mutent_dict['seq2'])
    cols2 = ['peptide_after_mutation', 'start_pos_after_mutation','end_pos_mutation']
    df2 =  pd.DataFrame(a2, columns=cols1)
    df2['Chopped'] = ''

    #add choped indicator to the df
    input_folder = "/home/itaybroder/Documents/GitHub/CovidResearch/CovSpikeMCHProject/input_files/spike.fasta"
    output_folder = "/home/itaybroder/Documents/GitHub/CovidResearch/CovSpikeMCHProject/output_files/out.txt"
    feed_to_Netchop(input_folder, output_folder)
    df1 = create_dataframe(output_folder, df1, 'seq1')
    df2 = create_dataframe(output_folder, df2, 'seq2')
        
     
    frames = [df1, df2]
    result = pd.concat(frames)
    df1.to_csv("big_pred.csv")
    
netchop_mutation_pipeline(mutent_dict)