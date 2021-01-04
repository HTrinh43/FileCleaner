import file_handle
import os, shutil

destination_folder = r'/Users/alextrinh/Library/Mobile Documents/com~apple~CloudDocs/School'

def test_create_new_folder():
    file_handle.create_new_folder(destination_folder, r'TCSS 343')
    assert os.path.exists(destination_folder + r'/TCSS 343')
def test_get_file_name():
    name = file_handle.get_file_name(destination_folder + r'/TCSS 342')
    assert r'TCSS 342' == name 
