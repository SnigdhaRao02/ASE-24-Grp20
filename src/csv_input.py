import re,ast,fileinput

def coerce(s):
  try: return ast.literal_eval(s)
  except Exception: return s

def csv(file="-"):
  with  fileinput.FileInput(None if file=="-" else file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
      if line: yield [coerce(x) for x in line.split(",")]
      

# #def get_csv_rows(src):
#   rows=[]
#   for row in csv(src): 
#     print(row)
#     rows.append(row)
#   return rows


