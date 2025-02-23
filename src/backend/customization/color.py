import winreg
import os

class Highlight:
    def __init__(self, red: int, green: int, blue: int):
        self.r = red
        self.g = green
        self.b = blue

    def change_highlight_color(self):
        red = self.r
        green = self.g
        blue = self.b
        HilightColor = f"{red} {green} {blue}"

        if self.r > 20: red -= 20
        if self.g > 20: green -= 20
        if self.b > 20: blue -= 20

        HotTrackingColor = f"{red} {green} {blue}"

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Colors", 0, winreg.KEY_SET_VALUE) as regkey:
            winreg.SetValueEx(regkey, "Hilight", 0, winreg.REG_SZ, HilightColor)
            winreg.SetValueEx(regkey, "HotTrackingColor", 0, winreg.REG_SZ, HotTrackingColor)

        os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
        #os.system("shutdown -r -t 0")
    
    def reset(self):
        HilightColor = f"0 120 215"
        HotTrackingColor = f"0 102 204"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Colors", 0, winreg.KEY_SET_VALUE) as regkey:
            winreg.SetValueEx(regkey, "Hilight", 0, winreg.REG_SZ, HilightColor)
            winreg.SetValueEx(regkey, "HotTrackingColor", 0, winreg.REG_SZ, HotTrackingColor)
        
        os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
