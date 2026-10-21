def process_tracklisting(Info_File_Path, Output_File_Path, IDTag):

    Info_File_XML = open(Info_File_Path, 'r')
    New_DLC_XML = open(Output_File_Path, 'x')
    Default_Folder_Location = "<FolderLocation>AUDIO\\Audiotracks\\"


    New_DLC_XML.write('<?xml version=\'1.0\' encoding=\'iso-8859-1\'?>\n')
    for index, info_line in enumerate(Info_File_XML.readlines()):
        if index == 0:
            New_DLC_XML.write('<TrackList DJHeroDLCVersion=\"2\">\n')
        elif Default_Folder_Location in info_line:
            FL_Start_idx = info_line.find(Default_Folder_Location, 0, len(info_line))
            #IDTag_End_idx = info_line.find('</FolderLocation>', 0, len(info_line))
            #IDTag_Start_idx = FL_Start_idx + len(Default_Folder_Location)
            #IDTag = info_line[IDTag_Start_idx:IDTag_End_idx]

            indent = ''
            for i in range(FL_Start_idx):
                indent += '\t'

            New_Folder_Location = indent + '<FolderLocation>DLC\\' + IDTag + '\\' + IDTag + '</FolderLocation>\n'
            New_DLC_XML.write(New_Folder_Location)
        else:
            New_DLC_XML.write(info_line)

    Info_File_XML.close()
    New_DLC_XML.close()

##this is very hacky but honestly idrc
def get_idtag(Info_File_Path):

    Info_File_XML = open(Info_File_Path, 'r')
    Default_Folder_Location = "<FolderLocation>AUDIO\\Audiotracks\\"

    for index, info_line in enumerate(Info_File_XML.readlines()):
        if Default_Folder_Location in info_line:
            FL_Start_idx = info_line.find(Default_Folder_Location, 0, len(info_line))
            IDTag_End_idx = info_line.find('</FolderLocation>', 0, len(info_line))
            IDTag_Start_idx = FL_Start_idx + len(Default_Folder_Location)
            IDTag = info_line[IDTag_Start_idx:IDTag_End_idx]
            Info_File_XML.close()

            return IDTag







