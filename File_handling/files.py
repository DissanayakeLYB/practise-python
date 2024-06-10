
# to write and read open the dopc twice separately.
# closing is not compulsory but good practise
doc = open("/File_handling/new.txt", "w")
doc.write("some text...")
doc.close()

doc = open("/File_handling/new.txt", "r")
content = doc.read()
print(content)
doc.close()

new_doc = open("D:/Github/practise-python/File_handling/new.txt", "r")
content = new_doc.read()
print(content)
new_doc.close()
