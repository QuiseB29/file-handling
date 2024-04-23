
import os
os.makedirs('my_directory.txt', exist_ok=True)
print("Created a new directory")


def list_files_and_directories(directory):
    print(f"Contents of directory '{directory}':")
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print(f"File: {item}")
        elif os.path.isdir(item_path):
            print(f"Directory: {item}")

def report_files_sizes(directory):
    print(f"File sizes in directory {directory}:")
    for item in os.listdir(directory):
        item_path = os.path.join(directory,item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"{item}: {size} bytes")
            



def main():
    directory = input("Enter directory path: ")
    if os.path.isdir(directory):
        list_files_and_directories(directory)
    else:
        print("Invalid directory path.")

if __name__ == "__main__":
    main()


def report_files_sizes(directory):
    print(f"File sizes in directory {directory}:")
    for item in os.listdir(directory):
        item_path = os.path.join(directory,item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"{item}: {size} bytes")
            
