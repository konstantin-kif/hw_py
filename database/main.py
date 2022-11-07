import fileio
import display
import UI

# def start():
#     mode = UI.start_message()
#     match mode:
#         case 1:
#             data = fileio.read_data("data.csv")
#         case 2:
#             fileio.write_data("data.csv", data)

data = fileio.read_data("data.csv")
UI.menu(data)
