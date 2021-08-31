import pandas as pd
import os
from IPython.display import display

directory="/home/itaybroder/Desktop/CovSpikeMCHProject/output_files//"
for txt in os.listdir(directory):   
    if txt.endswith(".txt"): 
      with  open(directory+txt, "r+") as file:
        lis=[]
        for line in file:
            line = line.rstrip("\n")
            if line.startswith("#"):
               continue
            if line.startswith("-"):
               continue
            if line.startswith("P"):
              continue
            if line.startswith("H"):
                continue
            else:
                line = line.split()
                lis.append(line)

for i in lis:
     del i[13:18]
#
col=["HLA","peptide","Core","Offset","I_pos","I_len","D_pos","D_len","iCore","Identity" ,"1-log50k(aff)","Affinity(nM)","%Rank"]


df = pd.DataFrame(lis,columns=col)
df = df.iloc[5: , :]
print(df.head())
df.to_csv("big_pred.csv")
df["%Rank"]= pd.to_numeric(df["%Rank"])
#
df=df.loc["%Rank"].astype(float)
#
for row in df["%Rank"]:
    int(float(row))


filtered = df[df["%Rank"] <=2]
print("H")

