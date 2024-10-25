import pygetwindow as gw
import psutil

def list_open_windows():
    # Gets list with opened windows.
    windows = gw.getAllTitles()
    window_dict = {i + 1: title for i, title in enumerate(windows)}
    
    return window_dict

def move_window(window_title):
    try:
        # Searches the Window with the Title
        window = gw.getWindowsWithTitle(window_title)[0]
        # Moves the window to 0, 0
        window.topleft = (0, 0)
        print(f"{window_title} is moved to (0, 0).")
    except Exception as e:
        print(f"Error by moving window: {e}")

def main():
    print("Opened windows:")
    
    # Gets titles of opened windows
    open_windows = list_open_windows()

    # Puts the windows in a list
    for index, title in open_windows.items():
        print(f"{index}: {title}")

    # Asks the user for a choise.
    try:
        choice = int(input("Number of window you want to move: "))
        if choice in open_windows:
            move_window(open_windows[choice])
        else:
            print("Invalid number, try a valid one.")
    except ValueError:
        print("Put a valid number.")
    except Exception as e:
        print(f"There is an error: {e}")

if __name__ == "__main__":
    main()
