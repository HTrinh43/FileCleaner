import os, shutil
import logging
'''
Move files to folders depend on their name

Choose a source folder
CHoose a destination folder
Move file with name start with the class code

If destination folder does not exist, create one.
If file already exist, rename by number '1,2,...'
'''
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

class_folder = ['TCSS371', 'TCSS342']

destination_folder = r'/Users/alextrinh/Library/Mobile Documents/com~apple~CloudDocs/School'
source_folder = r'/Users/alextrinh/Downloads'

def folder_is_existed(path):
    return os.path.exists(path)

#create a folder
def create_new_folder(path):
    if os.path.exists(path):
        logging.debug('Folder already exists')
        return -1
    else:
        os.mkdir(path)
        return 0

def get_file_name(path):
    '''
    @type path: string
    @pram path: a path to the file
    @type return: dict
    @pram return: a dictionnary contains 'name' and 'extension' of the file
    '''
    path_list = path.split('/')
    name = path_list[-1]
    file_name = {}
    file_name['name'] = name.rsplit('.',1)[0]
    file_name['extension'] = name.rsplit('.',1)[1]
    return file_name

def move_file(source_path, destination_path):
    filename = get_file_name(source_path)

    des_path = destination_path
    if folder_is_existed(des_path):
        pass
    else:
        create_new_folder(destination_path)
    file_name_str = filename.get('name') + '.' + filename.get('extension')
    file_path = destination_path + '/' + file_name_str
    count = 0
    file_is_existed = os.path.exists(file_path)
    while file_is_existed is True:
        count += 1
        file_name_str = '{}{}{}{}'.format(filename.get('name'),count,'.',filename.get('extension'))
        logging.debug(file_name_str)
        file_path = destination_path + '/' + file_name_str
        file_is_existed = os.path.exists(file_path)

    file_path = destination_path + '/' + file_name_str
    shutil.move(source_path, file_path)

for file in os.listdir(source_folder):
    if file.startswith('TCSS342'):        
        file_path = os.path.join(source_folder, file)
        destination = destination_folder + r'/TCSS 342'
        move_file(file_path,destination)
    elif file.startswith('TCSS371'): 
        file_path = os.path.join(source_folder, file)
        destination = destination_folder + r'/TCSS 371'
        move_file(file_path,destination)
    elif file.startswith('TCSS390'): 
        file_path = os.path.join(source_folder, file)
        destination = destination_folder + r'/TCSS 390'
        move_file(file_path,destination)
