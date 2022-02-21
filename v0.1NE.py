#v0.1ne (non encrypted)
import secrets
import string
print("""
  _   _       _                                  
 | \ | |     | |                                 
 |  \| |_   _| |__  _ __   __ _ ___ _____      __
 | . ` | | | | '_ \| '_ \ / _` / __/ __\ \ /\ / /
 | |\  | |_| | |_) | |_) | (_| \__ \__ \\ V  V / 
 |_| \_|\__,_|_.__/| .__/ \__,_|___/___/ \_/\_/  
                   | |                           
                   |_|                           
ver:0.1NE
""")
def crt():
	h = input("Platform name: ")
	a = string.ascii_letters + string.digits + string.punctuation
	c = ''.join(secrets.choice(a) for i in range(16))
	print("your new password:     " + c)
	d = open(h + ".txt", "w")
	e = d.write(c)
	d.close
while True:
	print("\n\ntype $create to create new password")
	e = input("Platform: ")
	if e == "$create":
		crt()
	else:
		f = open(e + ".txt", "r")
		g = f.read()
		f.close
		print(g)
		
