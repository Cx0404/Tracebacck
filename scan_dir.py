import requests


list_dir = [
"alfa3.php",
"alfav3.0.1.php",
"andela.php",
"bloodsecv4.php",
"by.php",
"c99ud.php"
"cmd.php"
"configkillerionkros.php",
"jspshell.jsp",
"mini.php",
"obfuscated-punknopass.php",
"punk-nopass.php",
"punkholic.php",
"r57.php",
"smevk.php",
"wso2.8.5.php"]

url = "http://10.10.10.181/"

for x in list_dir:
	try:
		res = requests.get(url+x)
		print(url + x + "\t", res)
	except:
		pass


