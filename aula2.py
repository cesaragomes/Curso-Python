print(12, 34, sep="JOAO") #Muda o separador para JOAO ao invés de espaço
print(54,6, sep="-") #Muda o separador para um hífen
print(54,6, sep='-') #Muda o separador para um hífen
print(78, 9) #Separador normal como espaço
print(13, 78, 1015, 4489, sep="-", end='##') #Não vai ocorrer uma quebra de linha
print(78, 9)
#
#
print(13, 78, 1015, 4489, sep="-", end='##\r\n') #Vai ocorrer uma quebra de linha após o ##
print(78, 9) 

print(13, 78, 1015, 4489, sep="-", end='\r\n##') #Vai ocorrer uma quebra de linha antes do ##
print(78, 9) 