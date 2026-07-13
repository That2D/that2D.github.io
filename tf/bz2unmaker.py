# Script by Sour Dani for use with any fast-dl server.

from os import listdir
import bz2

def main():
    extension = ".bsp.bz2"
    dir = "maps"

    try:
        print("Beginning batch map compression.")
        for file in listdir(dir):
            if file.endswith(extension):
                print(f"Compressing: {file}")
                with open(f"{dir}/{file}", "rb") as data, open(f"{dir}/{file[:-4]}", "wb") as new_file:
                    bz2contents = bz2.decompress(data.read())
                    new_file.write(bz2contents)
        print("Batch map compression complete.")
    except Exception as ex:
        print("Epic Fail: Conversion incomplete.")
        print(ex)
if __name__ == "__main__":
    main()  
