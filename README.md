# AAC_Call_Gen
Current SHA256 checksum: fe2e1db824f5f278910aaeb1ebc8a34b1cc1776c8b7dfa830d7c0586edf69f29

Basic aircraft call generator for ATC tower local control training purposes.

Uses call signs and reporting points for the Academy Airport along with minor configurable variables.

Uses google text to speech to read out an aircraft calling in inbound.

To use:

1. Copy the contents of AAC_Call_Generator.py to a text file and change the filename (including file extension) to be EXACTLY the same.
2. Install Python (Anaconda is good)
3. Install packages gTTs and playsound (e.g. pip install gTTs; pip install playsound)
4. Run AAC_Call_Generator.py script (e.g. through a .bat, example bat file included)
NOTE: The script generates and removes .mp3 files for the voice in the directory you run the script from. 
Certain actions/bugs may result in files being leftover.

Disclaimer:
NO LIABILITY FOR DAMAGES.
In no event shall the Author be liable for any special, consequential, incidental or indirect damages whatsoever (including, without limitation, damages to hardware, software, mental health, pecuniary losses, fireballs, etc.) arising out of the use of or inability to use this product, even if the Author is aware of the possibility of such damages and known defects.
