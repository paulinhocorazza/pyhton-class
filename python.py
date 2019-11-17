import os
os.getcwd()
os.chdir('O:/paulocorazza')
os.getcwd()
man = []
other = []


try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
             line_spoken = line_spoken.strip()
             if role == 'Man':
                 man.append(line_spoken)
                 
             elif role == 'Other Man':
                 other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print ('O arquivo de dados não está na pasta')

try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')

    print (man, file = man_file)
    print (other, file = other_file)

    man_file.close()
    other_file.close()
except IOError:
    print('File Error')
    
    
            
'''

try:
     data = open('sketch.txt')
     for each_line in data:
            try:
                 (role,line_spoken) = each_line.split(':',1)
                 line_spoken = line_spoken.strip()
                 if role == 'Man':
                     man.append(line_spoken)
                 elif role == 'Other Man':
                     other.append(line_spoken)
            except ValueError:
                pass
    data.close()
except IOError
    print('O arquivo de dados não está na pasta')

print (man)
print (other)

'''
             '''     print(role,end='')
                  print(' disse:',end='')
                  print(line_spoken,end='')
            except:
                pass
        
                

print("...........................................")

for each_line in data:
    print(each_line,end='')

data.close()


print("...........................................")

''''''
data=open('sketch.txt')
for each_line in data:
    if not each_line.find(':')==-1:
        (role,line_spoken) = each_line.split(':',1)
        print(role,end='')
        print(' disse:',end='')
        print(line_spoken,end='')
    
data.close()
'''

'''data=open('sketch.txt')
for each_line in data:
    try:
        (role,line_spoken) = each_line.split(':',1)
        print(role,end='')
        print(' disse:',end='')
        print(line_spoken,end='')
    except:
        pass
    
data.close()'''

'''
if os.path.exists('sketch.txt'):
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            print(role,end='')
            print(' disse:',end='')
            print(line_spoken,end='')
        except:
            pass
        
    data.close()
else:
    print('O arquivos de dados na esta na pasta.')
