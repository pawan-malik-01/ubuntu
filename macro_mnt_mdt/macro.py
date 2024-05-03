import pandas as pd
f = open("D:\B-Tech\TY_SEM_2\lpcc\lpcc code\input.txt", 'r')
MNT = pd.DataFrame(columns=['Name', 'Parameter', 'Index'])
MDT = {}
iMNT = 0
iM = 1
m = 0
F = 0
count = 0
FPA = {}

for l in f:
    l = l.strip("\n").replace(",", " ").upper().split(" ")

    if l[0] == "MACRO":
        mdt = []
        m = 1
        c = len(l[2:])
        MNT.loc[iMNT, 'Name'] = l[1]
        MNT.loc[iMNT, 'Parameter'] = c
        MNT.loc[iMNT, 'Index'] = iM
        iMNT += 1
        FPA[l[1]] = {}
        j = 1
        for i in l[2:]:
            FPA[l[1]][i] = f'#{j}'
            j += 1
    if m == 1:
        if l[0] in list(MNT['Name']):
            argument = l[1:]
            APA = {}
            k = 0
            for i in FPA[l[0]].values():
                APA[i] = argument[k]
                k += 1
            print("APA: ", APA)
            ind = MNT[MNT['Name'] == l[0]].index
            a = MNT.loc[ind, 'Index']
            li = list(MDT[int(a)])
            for i in li[:-1]:
                for key in APA.keys():
                    if key in i:
                        ind = li.index(i)
                        a = i.split(" ")
                        a[a.index(key)] = APA[key]
                        b = " ".join(a)
                        li[ind] = b
            mdt.append(li[:-1])

        else:
            for i in l:
                if i in list(FPA[MNT.iloc[-1, 0]].keys()):
                    l[l.index(i)] = FPA[MNT.iloc[-1, 0]][i]
            mdt.append(" ".join(l))
            count += 1
    else:
        with open('Ouput2.txt', 'a') as t:
            t.write(" ".join(l))
            t.write("\n")

    if l[0] == "MEND":
        m = 0
        count -= 1
        finalmdt = []
        for item in mdt[1:]:
            if type(item) == list:
                finalmdt = finalmdt+item
            else:
                finalmdt.append(item)
        MDT[iM] = finalmdt
        iM = count+1
print("FPA ", FPA)
print("MNT ", MNT)
print("MDT ", MDT)
