import os, sys
import tkinter as tk
from tkinter import filedialog

from routines.DJH_File_Handler import handle_files
from routines.Info_XML_To_DLC import get_idtag, process_tracklisting
from routines.Info_Trac_To_DLC import process_trac
from routines.DJH_CSV_to_TXT import csv_to_txt
from routines.DJH_FSGP_Generator import Make_FSGP


def main():
    file_diag = tk.Tk()
    file_diag.withdraw()

    Tracklisting_Path = filedialog.askopenfilename(
        title="Select Info For TrackListing.xml",
        filetypes=(("TrackListing File", "*.xml"), ("All files", "*.*")))

    Output_Path = filedialog.askdirectory(title='Select the folder you want to output to.')
    Song_Path = os.path.dirname(Tracklisting_Path)
    IDTag = get_idtag(Tracklisting_Path)


    handle_files(Song_Path, Output_Path, IDTag)

    process_tracklisting(Tracklisting_Path, Output_Path + '/' + IDTag + '/DLC/' + IDTag + '/TrackListing.xml', IDTag)

    process_trac(
        Song_Path + '/Info For TRAC.csv',
        Output_Path + '/' + IDTag + '/Text/DLC.csv')

    csv_to_txt(Output_Path + '/' + IDTag + '/Text/DLC.csv', Output_Path + '/' + IDTag + '/Text/DLC')

    os.remove(Output_Path + '/' + IDTag + '/Text/DLC.csv') #cleanup

    Make_FSGP(IDTag, Output_Path + '/' + IDTag, Output_Path + '/' + IDTag + '/DLC/')

    os.removedirs(Output_Path + '/' + IDTag + '/Text') #cleanup

if __name__ == '__main__':
    sys.exit(main())
