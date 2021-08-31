import subprocess
import os

def feed_to_NetMHCPan(input_file_path, output_file_path, pep_length):
    path_to_tool = '/home/itaybroder/Desktop/netMHCpan-4.1'
    if os.path.exists(path_to_tool) and os.path.exists(output_file_path) and os.path.exists(input_file_path):
        print('found all paths  :) ')
    else:
        print('cant find a path  :( ')

    HLA_str = 'HLA-A01:01,HLA-A02:01,HLA-A03:01,HLA-A24:02,HLA-A26:01,HLA-B07:02,HLA-B08:01,HLA-B27:05,HLA-B39:01,' \
              'HLA-B40:01,HLA-B58:01,HLA-B15:01'
    for length in pep_length:
        command = path_to_tool + "/netMHCpan -p " + input_file_path + " -l " + length + " -a " + HLA_str + " -s " + " >" + output_file_path
    print(command)
    subprocess.check_output('%s' % command, shell=True)

