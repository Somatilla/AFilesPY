import os
import shutil
from pathlib import Path

running = True

print("  ______   ________  __  __                      _______  __      __ ")
print(" /      \\ |        \\|  \\|  \\                    |       \\|  \\    /  \\")
print("|  $$$$$$\\| $$$$$$$$ \\$$| $$  ______    _______ | $$$$$$$\\\\$$\\  /  $$")
print("| $$__| $$| $$__    |  \\| $$ /      \\  /       \\| $$__/ $$ \\$$\\/  $$ ")
print("| $$    $$| $$  \\   | $$| $$|  $$$$$$\\|  $$$$$$$| $$    $$  \\$$  $$  ")
print("| $$$$$$$$| $$$$$   | $$| $$| $$    $$ \\$$    \\ | $$$$$$$    \\$$$$   ")
print("| $$  | $$| $$      | $$| $$| $$$$$$$$ _\\$$$$$$\\| $$         | $$    ")
print("| $$  | $$| $$      | $$| $$ \\$$     \\|       $$| $$         | $$    ")
print(" \\$$   \\$$ \\$$       \\$$ \\$$  \\$$$$$$$ \\$$$$$$$  \\$$          \\$$    ")
print("")
print("type help for command list")
print("")

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
        os.makedirs(Splitted[1] + "/" + Splitted[2], exist_ok=True)
        print(f"Created {Splitted[2]} at {Splitted[1]}")
    
    elif Splitted[0] == "del":
        file = Path(Splitted[1] + "/" + Splitted[2])
        if file.exists() == True:
            os.remove(file)
        else:
            print("file doesnt exist")
    
    elif Splitted[0] == "cp":
        cpfolder = Splitted[1]
        cpfile = Splitted[2]

        print(f"Copied{cpfolder}/{cpfile}")
    
    elif Splitted[0] == "ps":
        pfolder = Splitted[1]
        pfile = Splitted[2]

        shutil.copyfile(cpfolder + "/" + cpfile, pfolder + "/" + pfile)

        print(f"Pasted {cpfolder}/{cpfile} to {pfolder}/{pfile}")

    elif Splitted[0] == "rdtxt":
        print(open(Splitted[1] + "/" + Splitted[2]).read())
        print("end of file")
    
    elif Splitted[0] == "help":
        print("commands:")
        print("mv <directory/file> <directory2/file> -- moves <directory/file> to <directory2/file>")
        print("ren <directory/file> <directory/file2> -- renames <directory/file> to <directory/file2>")
        print("crf <folder> <newfolder> -- creates a folder at <folder>")
        print("del <directory> <file> -- deletes <file> at <director>")
        print("cp <directory> <file> -- copies <file> at <directory>")
        print("ps <folder> <file> pastes copied files to <folder/file>")
        print("rdtxt <directory> <file> -- reads <file> at <directory>")
        print("ls <directory> lists all files in <directory>")
        print("quit -- quits AFilesPY")

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
