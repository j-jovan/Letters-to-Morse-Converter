nastavi = True;
while(nastavi):
	userInput = input("Unesite tekst.")

	letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	morseCode = [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",".... ",".. ",".--- ","-.- ",".-.. ","-- ","-. ","--- ",".--. ","--.- ",".-. ","... ","- ","..- ","...- ",".-- ","-..- ","-.-- ","--.. "]

	for a in range(0, len(userInput), 1):
		for b in range(0, len(letters), 1):
			if(userInput[a] == letters[b]):
				print(morseCode[b], sep=' ', end='', flush=True)
	