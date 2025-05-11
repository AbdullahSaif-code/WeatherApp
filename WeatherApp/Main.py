from MenuHandler import MenuHandler

API_KEY = " your openweathermap api key here"

def main():
    menu = MenuHandler(API_KEY)
    menu.display_menu()


main()
