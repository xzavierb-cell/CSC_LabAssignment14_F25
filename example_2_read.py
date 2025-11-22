file_obj = open("datal.txt", "r")
content = file_obj.read()

# You would see the entire poem "The Zen of Python"
# You can open the file "datal.txt" to see it.
print (content)

# Remember to close the file after file manipulation
file_obj.close()