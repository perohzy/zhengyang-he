import os

# this_file_path = __file__
# this_dir_path = os.path.dirname(this_file_path)
this_dir_path = './home/'
jpg_index =1
xml_index =1
for file in os.listdir(this_dir_path):
    file_path = os.path.join(this_dir_path, file)
    if os.path.splitext(file_path)[-1] == '.png':
        new_file_path = '.'+'/'.join((os.path.splitext(file_path)[0].split('\\'))[:-1]) + '/img_{:0>4}.jpg'.format(jpg_index)
        jpg_index += 1
        print(file_path+'---->'+new_file_path)
        os.rename(file_path, new_file_path)
    elif os.path.splitext(file_path)[-1] == '.xml':
        new_file_path = '.'+'/'.join((os.path.splitext(file_path)[0].split('\\'))[:-1]) + '/img_{:0>4}.xml'.format(xml_index)
        xml_index += 1
        print(file_path+'---->'+new_file_path)
        os.rename(file_path,new_file_path)
