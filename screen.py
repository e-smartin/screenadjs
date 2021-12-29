
from subprocess import call
import sys

vga = "VGA-1"
dp = "DP-1"
lvds = "LVDS-1"

try:
    if (len(sys.argv) > 2 and sys.argv[1] == 'b' and int(sys.argv[2]) > 0 and int(sys.argv[2]) < 11):
        div = int(sys.argv[2])/10
        call("xrandr --output {}  --brightness {}".format(vga,div),shell=True)
        call("xrandr --output {}  --brightness {}".format(dp,div),shell=True)
    elif (sys.argv[1]=='d'):
        call('xrandr --output {} --auto --output {} --auto --right-of {}'.format(lvds,lvds,vga),shell=True)
    elif sys.argv[1]=='s':
        call('xrandr --output {} --off --output {} --auto --output {} --off'.format(vga,dp, lvds), shell= True) if sys.argv[2]=="0" else call ("xrandr --output {} --off --output {} --auto --output {} --off".format(dp,vga, lvds), shell=True)

    else:
        print(" Introduce:\n\t b [int from 1 to 10]\n\t\t or\n\t d")

        
except:
    print(" Introduce:\n\t b [int from 1 to 10]\n\t\tor\n\t s [0 or 1]  \n\t \tor\n\t d")
