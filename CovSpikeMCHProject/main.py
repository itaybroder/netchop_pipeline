import pandas as pd
import os

from netchop import create_dataframe, feed_to_Netchop
from MHCpan import split_for_all_peptides

HOME_DIRECTORY = '/home/itaybroder/Documents/GitHub/CovidResearch/CovSpikeMCHProject'
INPUT_DIR = os.path.join(HOME_DIRECTORY, 'input_files')
OUTPUT_DIR = os.path.join(HOME_DIRECTORY, 'output_files')
PATH_TO_NETCHOP = '/home/itaybroder/Documents/netchop-3.1'
#choose you can choose the RNA either from here or through the .fasta file
mutent_dict = {
   'seq1' : 'MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT',
   'seq2': 'MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLFDTQDLFLPFFSNVTWFHAIHVSGTNGTKRDFNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQFDFFYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT'
}
if(not os.path.isdir(INPUT_DIR)):
    os.mkdir(INPUT_DIR)

if(not os.path.isdir(OUTPUT_DIR)):
    os.mkdir(OUTPUT_DIR)

input_file = open(INPUT_DIR+"/spike.fasta", "w")
for i in mutent_dict:
  input_file.write(">" + i)
  input_file.write("\n")
  input_file.write(mutent_dict[i])
  input_file.write("\n")
input_file.close()



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
    feed_to_Netchop(input_folder, output_folder, PATH_TO_NETCHOP)
    df1 = create_dataframe(output_folder, df1, 'seq1')
    df2 = create_dataframe(output_folder, df2, 'seq2')
        
    result = df1.merge(df2, how='left', left_on=['start_pos', 'end_pos'], right_on=['start_pos','end_pos'], suffixes=['_before_mutation', '_after_mutation'])
    return result
    
result = netchop_mutation_pipeline(mutent_dict)
result.to_csv(OUTPUT_DIR + "/result.csv")