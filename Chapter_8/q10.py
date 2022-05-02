# 10. Most Frequent Character

def main():
  
  string = "Hello my name is dasaruu".lower()

  string_list = []
  occurence = []

  for i in string:
    if i.isalnum():
      if i not in string_list:
        string_list.append(i)
        occurence.append(1)

      elif i in string_list:
        occurence[string_list.index(i)]+=1

  max_occ = max(occurence)


  print(string_list[occurence.index(max_occ)])
  print(max_occ)



  print(string_list)
  print(occurence)
    

# Call the main function    
main()