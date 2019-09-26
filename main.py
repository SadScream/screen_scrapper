import sys
import requests
import os
import string
import random
import threading


if len(sys.argv) < 2:
    sys.exit(f"\t[Usage: python {sys.argv[0]} (Number of threads)")

count = int(sys.argv[1])


class Scrapper():

	def __init__(self):
		path = os.getcwd()
		if "pics" not in os.listdir(path):
			os.mkdir("pics")
		self.path = os.path.join(path, "pics\\")

	def run(self):
		while True:
			amount = random.choice([5, 3])

			if amount == 3:
				firstPart = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(amount)))
				secondPart = str(''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(amount)))	
				name = (f"{firstPart}{secondPart}.jpg")

			elif amount == 5:
				name = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(amount)))
				name += ".jpg"
			
			URL = (f"https://i.imgur.com/{name}")
			r = requests.get(URL, stream=True)
			contentType = r.headers['Content-Type'] # if image not found it takes 'image/png' value otherwise 'image/jpeg'(I suppose)
			status = r.status_code

			if contentType == 'image/png' or status == 404:
				continue

			if status == 200:
				print("[+] Valid: " + URL)

			with open(f"{self.path}{name}", "wb+") as out:
				for chunk in r.iter_content(512):
					out.write(chunk)


for i in range(count):
	thread = threading.Thread(target=Scrapper().run)
	thread.start()


































