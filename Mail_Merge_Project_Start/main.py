#TODO: Create a letter using starting_letter.txt 

with open(r"Mail_Merge_Project_Start\Input\Names\invited_names.txt",mode="r") as file:
    names_list = file.readlines()
    
with open("Mail_Merge_Project_Start\Input\Letters\starting_letter.txt",mode="r") as file:
    text = file.read()


for txt in names_list:
    name = txt.strip()
    letter_content = text.replace("[name]",name)
   
    with open(f"Mail_Merge_Project_Start\Output\ReadyToSend\letter_for_{name}.txt",mode="w") as file:
        file.write(letter_content)


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp