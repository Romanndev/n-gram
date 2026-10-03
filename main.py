

def read_file() -> dict[str,int]:
 lwords = []
 clearwords = []
 dbbewords = {}
 #bdthreewords = {}
 pairs = []
 with open("Search_terms_report.txt", "r", encoding="utf-8") as fh:
    for i in fh:
     lwords = i.lower().strip().split()
     if not lwords: continue
     clearwords = [i.strip(",!.?<>()[]+/") for i in lwords]
     if len(clearwords) < 2: continue
     qwe=(list(zip(clearwords, clearwords[1:])))
     for y in range(len(qwe)):
      pairsstap = qwe[y][0]+' '+qwe[y][1]
      pairs.append(pairsstap)
     

    for i in pairs:
      dbbewords[i] = dbbewords.get(i,0) + 1

    # По убыванию значений
    sorted_dbbewords = dict(sorted(dbbewords.items(), key=lambda item: item[1], reverse=True))

    # for key, value in sorted_dbbewords.items():
    #      print(key,value)


 return sorted_dbbewords  

def record_file(dbbewords:dict[str,int]):
  with open("result.txt", "w", encoding="utf-8") as fh:
    fh.writelines(f"{key}: {value}\n" for key,value in dbbewords.items())

  print(" Задача выполнена, результат в файле result.txt")

def be_grams(beparam:list): 
 pass

def three_grams(threeparam:list):
 pass

#------ main -----

record_file(read_file())