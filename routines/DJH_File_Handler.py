import os
import shutil


def handle_files(input_path, output_folder, IDTag):
    Chart_Input = input_path + '/' + IDTag
    Chart_Output = output_folder + '/' + IDTag + '/DLC/' + IDTag + '/' + IDTag

    os.makedirs(output_folder + '/' + IDTag + '/DLC/' + IDTag) #Main housing folder
    os.makedirs(output_folder + '/' + IDTag + '/Text/DLC') #Ingame Text folder
    shutil.copytree(Chart_Input, Chart_Output)


