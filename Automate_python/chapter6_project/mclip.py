# python3
# mclip.py - A multi-clipboard program.
import pyperclip
import sys
#step1:
TEXT = {
    'agree': """Ok,You are right! ^V^""",
    'busy': """I am busy, sorry...quq""",
    'disagree': """No,no,no,no,no! oNo""",
    'nomoney': """Can you give me some money? @w@""",
    'fuck': """fuck you bro...you know m3 bro?""",
    'loveyou': """i Love ui Love ui Love ui Love ui Love ui Love ui Love ui Love ui Love ui Love ui Love ui Love u"""
}

#step2:
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()


keyphrase = sys.argv[1]     # First command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
    print(f"copied text: {pyperclip.paste()}")
else:
    print(f"There is no text for {keyphrase}")






