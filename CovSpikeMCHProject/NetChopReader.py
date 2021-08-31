""" imports """
# ------------------------------------------------------------------------ <editor-fold>
import sys
import subprocess
import os

# ------------------------------------------------------------------------ </editor-fold>

""" paths """
# ------------------------------------------------------------------------ <editor-fold>

path_to_tool = '/home/itaybroder/Desktop/netchop-3.1'
path_with_seq = '/home/itaybroder/Desktop/CovSpikeMCHProject/input_files'
path_to_save = '/home/itaybroder/Desktop/CovSpikeMCHProject/output_files'
if os.path.exists(path_to_tool) and os.path.exists(path_to_save) and os.path.exists(path_with_seq):
    print('found all paths  :) ')
else:
    print('cant find a path  :( ')

# ------------------------------------------------------------------------ </editor-fold>


""" global variables """
# ------------------------------------------------------------------------ <editor-fold>

input_file = path_with_seq + '/spike.fasta'
output_file = path_to_save + '/test.txt'

# ------------------------------------------------------------------------ </editor-fold>


""" MAIN """

# ------------------------------------------------------------------------ <editor-fold>


command = path_to_tool + "/netchop " + input_file + " >" + output_file
print(command)
subprocess.check_output('%s' % command, shell=True)

# ------------------------------------------------------------------------ </editor-fold>
