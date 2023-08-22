def convertToTitle(column_number: int) -> str:
        column_name = ""
        while column_number > 0:
            offset = (column_number - 1) % 26
            column_name += chr(ord('A') + offset)
            column_number = (column_number - 1) // 26
        return column_name[::-1]