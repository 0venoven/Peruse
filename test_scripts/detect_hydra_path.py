import os

# dynamically get the path of thc-hydra-windows-master folder
def get_hydra_directory():
    downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    hydra_folder = os.path.join(downloads_dir, 'thc-hydra-windows-master')
    if os.path.exists(hydra_folder) and os.path.isdir(hydra_folder):
        print(hydra_folder)
        return hydra_folder
    else:
        print("Hydra binaries are not found. Please make sure it is downloaded and extracted to Downloads/thc-hydra-windows-master")
        return None

get_hydra_directory()