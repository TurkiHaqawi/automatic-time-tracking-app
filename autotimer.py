from AppKit import NSWorkspace
import time

active_window_name = ""
while True:
    
    # First activate to get which app is being used now (macOS)
    new_window_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
    if active_window_name != new_window_name:
        active_window_name = new_window_name
        print(active_window_name)
    
    time.sleep(2)
