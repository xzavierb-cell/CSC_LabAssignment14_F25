# Please open "data3.txt" to see the file content 
# there are 4 lines inthe file, lwts append one

file_obj = open("data3.txt", "a") # use mode "a" for append
file_obj.write ("this is 5th line\n")
file_obj.write ("this is 5th line\n")
file_obj.close()

# Please open "date3.txt" again after executipon to see the file content
# It should have 6 lines now.
