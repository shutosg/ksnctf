import subprocess, re, urllib
from urllib import parse
uri = 'http://ctfq.sweetduet.info:10080/\~q31/kangacha.php'
ship = 0
signature = 'a7aff87d838a07da5005733c836fdf385509be83c82032c5a8f3962753ebc85ed6cfae2565eb2c98bc6d70648c7e7078a6265cfdbd89341fe05e1305d7840983'
for i in range(15, 30):
	hashpump = 'hashpump -s "' + signature + '" -d "' + str(ship) + '" -a ",10" -k ' + str(i)
	hp = subprocess.check_output(hashpump, shell=True, universal_newlines=True).split("\n")
	newsig = hp[0]
	newship = hp[1]
	curl = 'curl -b "ship=' + newship.replace('\\x', '%') + ';signature=' + newsig + '" ' + uri
	#print(curl)
	result = subprocess.check_output(curl, shell=True, universal_newlines=True)
	s = re.search("(FLAG_[a-zA-Z0-9]+)", result)
	if s:
		print("success!: " + str(i))
		print(s.group(0))
		break
	else:
		print("faild: " + str(i))
	

