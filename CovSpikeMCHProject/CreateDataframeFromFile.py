import pandas as pd
import os
from IPython.display import display

directory="/home/itaybroder/Desktop/CovidResearch/CovSpikeMCHProject/output_files/"
for txt in os.listdir(directory):
    if txt.endswith(".txt"):
      with  open(directory+txt, "r+") as file:
        lis=[]
        for line in file:
            line = line.rstrip("\n")

            if line.startswith("#"):
               continue
            elif line.startswith("-"):
               continue
            elif line.startswith("P"):
              continue
            elif line.startswith("H"):
                continue
            elif line.startswith(" P"):
                continue
            else:
                line = line.split()
                lis.append(line)



for i in lis:
    if(len(i) == 13):
        i.append("n")
    if(len(i) == 0):
        lis.pop(lis.index(i))
    if(len(i) == 15):
        i.pop(13)

for i in lis:
    if len(i) == 15:
        print(i)
        i.pop(13)
        print(i)


col=["Pos","MHC","Peptide","Core","Of","Gp","Gl","Ip",
"Il","Icore" ,"Identity","Score_EL","%Rank_EL", "BindLevel"]


df = pd.DataFrame(lis,columns=col)
df = df.iloc[5: , :]
print(df.head())
df.to_csv("big_pred.csv")
