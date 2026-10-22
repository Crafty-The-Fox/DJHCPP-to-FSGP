import os
import shutil


def handle_files(input_path, output_folder, IDTag):
    Chart_Input = input_path + '/' + IDTag
    Chart_Output = output_folder + '/' + IDTag + '/DLC/' + IDTag + '/' + IDTag

    os.makedirs(output_folder + '/' + IDTag + '/DLC/' + IDTag) #Main housing folder
    os.makedirs(output_folder + '/' + IDTag + '/Text/DLC') #Ingame Text folder
    shutil.copytree(Chart_Input, Chart_Output)


def handle_files_xenia(input_path, output_folder, IDTag):

    files_output = output_folder + '/' + IDTag + '_Xenia/0000000000000000/4156087F/00000002'
    header_output_folder = output_folder + '/' + IDTag + '_Xenia/0000000000000000/4156087F/Headers/00000002'
    os.makedirs(files_output)
    os.makedirs(header_output_folder)
    shutil.copytree(input_path, files_output + '/' + IDTag)
    return header_output_folder


