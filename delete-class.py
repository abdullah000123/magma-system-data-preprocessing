import os

# Parameters
directory = '/home/abdullah/abdullah-dev/object-segmentation/grapes/valid/labels'  # Replace with the path to your YOLO label text files
class_to_delete = '0'  # Replace with the index of the class you want to delete

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)

        # Read the file and filter out lines with the unwanted class
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Keep lines that don't start with the specified class index
        filtered_lines = [line for line in lines if not line.startswith(class_to_delete + ' ')]

        # Write the filtered lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(filtered_lines)

print("Lines with class", class_to_delete, "have been deleted from all text files.")
