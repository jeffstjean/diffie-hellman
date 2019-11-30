import random
import time

def main():
	# message we wish to send
	msg = 'Hello, how are you?'

	# create our two devices
	d1 = Device()
	d2 = Device()

	# perform Diffie-Hellman key exchange
	print('\nPerforming key exchange...\n')
	Device.keygen(d1, d2)

	# encrypt the message to be sent
	encrypted = d1.encrypt(msg)
	print('[Device1] encrypting message ', msg)

	# 'send' the message
	print('[Device1] sending message...\n')
	time.sleep(0.5)

	# decrypt the encrypted message using the other device
	decrypted = d2.decrypt(encrypted)
	print('[Device2] received message')
	print('[Device2] decrypted message as ',  decrypted, '\n')
	

class Device: 
	n = random.randint(1000, 5000)
	g = 15319

	def __init__(self):
		self.private = random.randint(1, Device.n)
		self.public = (Device.g**self.private)%Device.n
		self.key = None

	@staticmethod
	def keygen(d1, d2):
		d1.key = (d2.public**d1.private)%Device.n
		d2.key = (d1.public**d2.private)%Device.n

	def encrypt(self, msg):
		unencrypted = []
		encrypted = []
		final = []
		for letter in msg:
			unencrypted.append(ord(letter))
			encrypted.append(ord(letter) + self.key)
		for byte in encrypted:
			final.append(byte - self.key)
		return encrypted

	def decrypt(self, encrypted):
		unencrypted = ''
		for byte in encrypted:
			unencrypted += chr(byte - self.key)
		return unencrypted



if __name__ == "__main__":
    main()