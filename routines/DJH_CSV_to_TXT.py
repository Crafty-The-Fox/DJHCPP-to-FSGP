"""
MIT License

Copyright (c) 2019 shockdude

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import csv
import os
import sys

# DJH Text/CSV converter v0.41
# Edited by Crafty


        
def csv_to_txt(csv_filename, folder_name):

    # read the CSV and write to text files
    print("Writing text files to folder {}".format(folder_name))
    with open(csv_filename, "r", encoding="utf_8_sig", newline="") as text_csvfile:
        text_csv = csv.reader(text_csvfile, dialect="excel")
        os.chdir(folder_name)
        text_files = []
        num_files = -1
        id_index = -1
        for row in text_csv:
            if num_files < 0:
                num_files = len(row)
                if num_files < 2: # need 1 ID file and at least 1 string file
                    error_and_exit("Error: corrupt CSV/Text files; need at least 2 columns")
                for i in range(num_files):
                    text_filename = row[i] + ".txt"
                    if row[i] == "DLCID":
                        id_index = i # string ID file
                        text_files.append(open(text_filename, "w", encoding="utf-8", newline="\r\n"))
                    elif row[i].find("DLC") == 0: # string file
                        text_files.append(open(text_filename, "wb"))
                    else:
                        print("Error: corrupt CSV/Text files; invalid header filename {}".format(row[i]))
                        exit()
                if id_index < 0:
                    error_and_exit("Error: corrupt CSV/Text files; missing {}ID in header row".format(folder_name))
            elif len(row) > 0: # ignore blank lines
                if row[0][0:2] == "//": # ignore commented lines
                    continue

                i = id_index
                text_files[i].write(row[i] + "\n")
                # use string id as text string if no other text string is provided
                string_bin = row[i].encode("utf-8") + b"\x00"
                
                for i in range(num_files):
                    if i == id_index:
                        continue
                    elif i < len(row):
                        string_bin = row[i].encode("utf-8") + b"\x00"
                        text_files[i].write(string_bin)
                    else: # copy the last string in the row to all remaining columns
                        text_files[i].write(string_bin)
                        
        for file in text_files:
            file.close()
        os.chdir("..")
    print("Text files written to folder {}".format(folder_name))
