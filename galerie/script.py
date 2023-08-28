import os

folder_path = "C:/Users/Adrian/Downloads/StronaInternetowaMBUD/galerie/galeria1"

counter = 1

# Create a new directory for the galerie if it doesn't exist
galerie_dir = os.path.join(folder_path, "C:/Users/Adrian/Downloads/StronaInternetowaMBUD/galerie/")
os.makedirs(galerie_dir, exist_ok=True)

# Create a new text file for galerie and clear it
galerie_file_path = os.path.join(galerie_dir, "galeria.txt")
open(galerie_file_path, "w").close()

for filename in os.listdir(folder_path):
    while True:
        new_filename = str(counter) + ".jpg"
        new_filepath = os.path.join(folder_path, new_filename)

        if not os.path.exists(new_filepath):
            old_filepath = os.path.join(folder_path, filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {filename} to {new_filename}")
            
            if counter > 1:
                # Write to galeria1.txt (omit the first file)
                with open(galerie_file_path, "a") as galeria_file:
                    galeria_file.write(f"'galerie/galeria1/{new_filename}',\n")

            counter += 1
            break

        counter += 1