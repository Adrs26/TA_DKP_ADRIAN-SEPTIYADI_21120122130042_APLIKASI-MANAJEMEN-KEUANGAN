# Function untuk membaca data yang ada pada database dalam bentuk list / array
def read_data() :
    with open("Database.txt", "r", encoding="UTF-8") as file :
        content = file.readlines()
        return content
