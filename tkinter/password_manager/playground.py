import os 
script_dir = os.path.dirname(__file__)
file_path  = os.path.join(script_dir,"password_data.txt")
def save(text):
    with open(file_path,mode="a") as file:
        file.write(f"{text}\n")

save("print 3nd line")