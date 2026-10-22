
def generate_header(headerPath, DLC_Name, DLC_ID):
    HeaderFile = open(headerPath, "wb")

    fullArray = bytearray()
    nameArray = bytearray()
    idArray = bytearray()

    header = b'\x00\x00\x00\x01\x00\x00\x00\x02'
    trail = b'\x41\x56\x08\x7F\x00\x00\x00\x00\x01\x00\x00\x00'
    null_byte = b'\x00'

    if len(DLC_Name) * 2 > 256 or len(DLC_ID) > 56:
        exit()


    for char in range(len(DLC_Name)):
        currInt = ord(DLC_Name[char])
        currByte = currInt.to_bytes(1, "little")

        nameArray.extend(null_byte)
        nameArray.extend(currByte)



    fill_zeros = 256 - len(DLC_Name) * 2 
    for char in range(fill_zeros):
        nameArray.extend(null_byte)

    for char in range(56):
        if char < len(DLC_ID):
            currInt = ord(DLC_ID[char])
            currByte = currInt.to_bytes(1, "little")
            idArray.extend(currByte)
        else:
            idArray.extend(null_byte)


    fullArray.extend(header)
    fullArray.extend(nameArray)
    fullArray.extend(idArray)
    fullArray.extend(trail)

    HeaderFile.write(fullArray)

