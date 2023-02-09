#read the file and save every word as a list item.
text_file = open("p042_words.txt", "r")
text_list = text_file.readlines()

#getting rid of " symbols and seperating from commas.
text_list[0] = text_list[0].replace('"', '')
mylist = text_list[0].split(",")

#checks given number if its triangle number
def triangle_check(mynumber):
    i = 1
    triangle = 1
    while triangle <= mynumber:
        if triangle == mynumber:
            return 1
        i += 1
        triangle = 0.5*i*(i + 1)
    return (0)

#calculates the number of the word and checks if its triangle         
def is_triangle_word(mystr):
    score = 0
    for letter in mystr:
        score += (ord(letter) - 64)
        #converting every letter to ascii values(A = 65)
    return triangle_check(score)


triangle_words = [] 
for item in mylist:
    if is_triangle_word(item):
        triangle_words.append(item) #if the word is triangle, we append it to the list.

print(len(triangle_words))