import zipfile

def extract_archive(archivepath, dest_dir): #destination directionry
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("Users/as/bonus/compressed.zip", dest_dir, 
                    "Users/as/bonus/files")