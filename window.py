import pygetwindow as gw
import psutil

def list_open_windows():
    # Verkrijg een lijst van alle geopende vensters
    windows = gw.getAllTitles()
    window_dict = {i + 1: title for i, title in enumerate(windows)}
    
    return window_dict

def move_window(window_title):
    try:
        # Zoek het venster met de gegeven titel
        window = gw.getWindowsWithTitle(window_title)[0]
        # Verplaats het venster naar (0, 0)
        window.topleft = (0, 0)
        print(f"{window_title} is verplaatst naar (0, 0).")
    except Exception as e:
        print(f"Fout bij het verplaatsen van het venster: {e}")

def main():
    print("Geopende vensters:")
    
    # Verkrijg de geopende vensters en hun titels
    open_windows = list_open_windows()

    # Toon de vensters in een menu
    for index, title in open_windows.items():
        print(f"{index}: {title}")

    # Vraag de gebruiker om een keuze
    try:
        choice = int(input("Voer het nummer in van het venster dat je wilt verplaatsen: "))
        if choice in open_windows:
            move_window(open_windows[choice])
        else:
            print("Ongeldig nummer. Probeer het opnieuw.")
    except ValueError:
        print("Voer een geldig getal in.")
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

if __name__ == "__main__":
    main()
