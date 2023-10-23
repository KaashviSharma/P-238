import hashlib
img = "pic.jpg"
with open(img,"rb")as f:
	img_data = f.read()
	img_hash = hashlib.sha256(img_data).hexdigest()
	print("hashcode of image: ",img_hash)