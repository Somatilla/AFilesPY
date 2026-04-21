import os
import shutil

running = True

while running:
    command = input("fm>")

    Splitted = command.split()

    if Splitted[0] == "mv":
        shutil.move(Splitted[1], Splitted[2])
        print(f"moved {Splitted[1]} to {Splitted[2]}")
    
    elif Splitted[0] == "ren":

        shutil.move(Splitted[1], Splitted[2])
        print(f"Renamed {Splitted[1]} to {Splitted[2]}")
    
    elif Splitted[0] == "crf":
        os.makedirs(Splitted[1] + Splitted[2], exist_ok=True)
        print(f"Created {Splitted[2]} at {Splitted[1]}")
    
    elif Splitted[0] == "ls":
        path = Splitted[1] if len(Splitted) > 1 else "."
        try:
            files = os.listdir(path)
            for file in files:
                print(file)
            print(f"listed {len(files)} files")
        except FileNotFoundError:
            print(f"Error: Path '{path}' not found")
        except NotADirectoryError:
            print(f"Error: '{path}' is not a directory")
        
    elif Splitted[0] == "quit":
        running = False
print("quitting terminal")
