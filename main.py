from pull_profiles import copy_folder
from pull_registry_data import export_reg_key

# Enter Default Chrome Profiles Folder Path
target_dir = ""

copy_folder(target_dir)
export_reg_key(key_path=r"SOFTWARE\Google\Chrome\PreferenceMACs", filename='chrome_registry_export.reg')
