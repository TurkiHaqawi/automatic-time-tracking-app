from AppKit import NSWorkspace, NSAppleScript
import time

active_window_name = ""
while True:
    
    # First activity to get which app is being used now (macOS)
    new_window_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
    if active_window_name != new_window_name:
        active_window_name = new_window_name
        print(active_window_name)
        # Second activity to get active window
        if active_window_name == 'Google Chrome':
            text = """tell app "Google Chrome" to get the url of the active tab of window 1"""
            s = NSAppleScript.initWithSource_(NSAppleScript.alloc(), text)
            result, err = s.executeAndReturnError_(None)
            print(result.stringValue())
    time.sleep(2)
