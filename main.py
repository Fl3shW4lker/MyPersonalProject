#impor
import termcolor
from termcolor import colored
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m' # Resets color and style


print(Colors.GREEN + "Hello, Mr.Anderson." + Colors.RESET)
print(colored('Hello, Mr.Anderson.', 'green', 'on_red'))
