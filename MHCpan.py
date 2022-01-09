import subprocess
import os
import pandas as pd
from config import HOME_DIRECTORY, INPUT_DIR, OUTPUT_DIR, PATH_TO_NETCHOP

#splitting RNA to all the possible peptides by certain k
def split_by_k(RNA, k):
    peptides = []
    pos_counter = 1
    for s in RNA[:len(RNA)-k]:
        peptides.append([RNA[pos_counter-1: pos_counter+k-1], pos_counter, pos_counter+k])
        pos_counter+=1
    return peptides

#returns a list with all peps
def split_for_all_peptides(str):
    return split_by_k(str, 8) + split_by_k(str, 9) + split_by_k(str, 10)


def feed_to_NetMHCPan(input_file_path, output_file_path, pep_length):
    path_to_tool = '/home/itaybroder/Downloads/netMHCpan-4.1'
    if os.path.exists(path_to_tool):
        print('found all paths  :) ')
    else:
        print("coudn't find ", " ", path_to_tool)

    if os.path.exists(output_file_path):
        print('found all paths  :) ')
    else:
        print("coudn't find ", " ", output_file_path)
    if os.path.exists(input_file_path):
         print('found all paths  :) ')
    else:
        print("coudn't find ", " ", input_file_path)


    HLA_str = 'HLA-A01:01,HLA-A02:01,HLA-A03:01,HLA-A24:02,HLA-A26:01,HLA-B07:02,HLA-B08:01,HLA-B27:05,HLA-B39:01,' \
              'HLA-B40:01,HLA-B58:01,HLA-B15:01'
    for length in pep_length:
        command = path_to_tool + "/netMHCpan -p " + input_file_path + " -xls " + " -l " + str(length) + " -a " + HLA_str + " -s " + " >" + output_file_path
    print(command)
    subprocess.check_output('%s' % command, shell=True)

input_folder = "/home/itaybroder/Desktop/netchop_pipeline/input_files"
output_folder = "/home/itaybroder/Desktop/netchop_pipeline/output_files"
pep_length = [8, 9, 10]

pep_list = split_for_all_peptides("MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT");

textfile = open("input_files/all_peps.txt", "w")
for element in pep_list:
   textfile.write(element[0] + "\n")
textfile.close()


feed_to_NetMHCPan(input_folder + '/all_peps.txt', output_folder + '/netMHCpan.txt', pep_length)


def create_mhcpan_dataframe(output_file):
    with open(output_file, 'r') as f:
        output_file_lines = f.readlines()
        lis=[]
        i = 0
        while(i<len(output_file_lines)):
            
            while(i<len(output_file_lines)):
                print("line line i  "+ output_file_lines[i])
                if(output_file_lines[i].startswith(" Pos")):
                    i+=2
                    break
                i+=1
            while(i<len(output_file_lines) and output_file_lines[i].startswith("-")):
                line = output_file_lines[i].split()
                mhc_type = line[1]
                peptide = line[2]
                rank = line[12]
                BindLevel = line[14]
                row = [mhc_type, peptide, rank, BindLevel]
                print(row)
                lis.append(row)
                i+=1
        
        cols = ["mhc_type", "peptide", "rank", "BindLevel"]
        mhc_frame = pd.DataFrame(lis, columns=cols)
        mhc_frame.to_csv(OUTPUT_DIR + "/mhc_resualt.csv")