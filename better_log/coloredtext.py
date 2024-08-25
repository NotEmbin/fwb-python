from colorama import Fore, Back, Style

def color(text: str, foreg, backg=None) -> str:
  colored_text = f'{foreg}{text}{Style.RESET_ALL}'

  return colored_text if backg is None else backg + colored_text
