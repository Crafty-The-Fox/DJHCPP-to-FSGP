def process_trac(Info_File_Path, Output_File_Path):

    Info_File_CSV = open(Info_File_Path, 'r')
    New_DLC_CSV = open(Output_File_Path, 'x')

    New_DLC_CSV.write('DLCID,DLCSNA,DLCS,DLCI,DLCG,DLCF,DLCE,DLCDEV\n')
    for index, info_line in enumerate(Info_File_CSV.readlines()):
        New_DLC_CSV.write(info_line)

    Info_File_CSV.close()
    New_DLC_CSV.close()


