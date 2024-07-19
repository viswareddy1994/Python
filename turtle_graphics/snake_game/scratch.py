# Write to the file


def high_score_storing(val='0'):
    with open(r"turtle_graphics\snake_game\data\demo.txt", mode="w") as file:
        file.write(val)
high_score_storing("hello")
# Read from the file
def high_score():
    with open(r"turtle_graphics\snake_game\data\demo.txt", mode="r") as file:
        content = file.read()
        return content
val = high_score()
print(val)

# turtle_graphics\snake_game\scratch.py
