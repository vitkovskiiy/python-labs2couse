import os 

total = 0

if not os.path.exists('text.txt'): 
    print("File don't exist")
else:
    with open('text.txt','r', encoding = 'utf-8') as infile:
        data = infile.readline().split()
        for item in data: 
            total+= int(item)
            
print(f"Avarage number from readed file: {total/len(data)}")
