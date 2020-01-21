from os import walk, listdir, path

separator_file = '➥   '
separator_folder = '⬇   '

output_string = []
output_string.append


def traverseFolder(dir, level):
    for file in listdir(dir):
        abs_path = path.join(dir, file)
        if (path.isdir(abs_path)):
            output_string.append(separator_folder * level + file)
            output_string.append(separator_folder * level + len(file) * '-')
            traverseFolder(abs_path, level + 1)
        else:
            output_string.append(separator_folder * (level - 1) + separator_file + file)

traverseFolder('<File Location>', 0)

with open('File_Structure.txt', 'wb') as file_structure:
    file_structure.write('\n'.join(output_string).encode())
    print('File written')
