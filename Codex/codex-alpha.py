#Gizli alfabe için alfabe ve karşılıklarını üretir.
from random import randint
characters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZWQXabcçdefgğhıijklmnoöprsştuüvyzwqx,._-<>!'^+%&/()=?£#$½¾{[]}0123456789 ~â—àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝßêîôûåÂÊÎÔÛãñõÃÑÕŸäëïÿ"
character_array = []
for a in characters:
    character_array.append(a)
nums = []
new_list = []
while True:
    if len(nums)==len(character_array):
        break
    num = randint(0, len(character_array) - 1)
    num2 = randint(0, len(character_array) - 1)
    if num in nums or num2 in nums or num == num2:
        continue
    else:
        nums.append(num)
        nums.append(num2)
        pair1 = character_array[num]
        pair2 = character_array[num2]
        new = pair1 + pair2
        new_list.append(new)

print(*new_list,sep="  ")
print(f"Len of the character array is {len(character_array)}")
print(f"Len of the new list is {len(new_list)}")
