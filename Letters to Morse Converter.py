x = input()

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
morseCode = [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",".... ",".. ",".--- ","-.- ",".-.. ","-- ","-. ","--- ",".--. ","--.- ",".-. ","... ","- ","..- ","...- ",".-- ","-..- ","-.-- ","--.. "]

for i in range(0, len(x), 1):
	for e in range(0, len(letters), 1):
		if(x[i] == letters[e]):
			print(morseCode[e], sep=' ', end='', flush=True)
	