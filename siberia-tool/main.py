# mv - cmd for move
from rich.console import Console
console=Console()
import os, sys

console.print("""[bold red]

░██████╗██╗██████╗░███████╗██████╗░██╗░█████╗░
██╔════╝██║██╔══██╗██╔════╝██╔══██╗██║██╔══██╗
╚█████╗░██║██████╦╝█████╗░░██████╔╝██║███████║
░╚═══██╗██║██╔══██╗██╔══╝░░██╔══██╗██║██╔══██║
██████╔╝██║██████╦╝███████╗██║░░██║██║██║░░██║
╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝

██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░█████╗░░██████╔╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗███████╗██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝
                                            
[bold black]VERSION : [ 1.0.0 ]
[bold white]=============================================
[bold black]CHOOSE NUMBER
[bold white]
[ 1 ] Install Siberia 1.0.3
[ 2 ] Install Siberia 1.0.5
[ 3 ] Install Siberia 1.0.6
[ 4 ] Uninstall all
[ 5 ] Exit
""")
def functions():
     menu = console.input(
      "[bold white]choose number: "
       )
     if menu == "1":
        console.print(
        "[bold red][ wait ] Siberia 1.0.3 is proceed to installing..."
         )
        os.system("git clone https://github.com/MFDGaming/ubuntu-in-termux")
        console.print(
        "[bold green][ + ] Installation completed\n[ √ ] tool saved in $HOME"
         )
