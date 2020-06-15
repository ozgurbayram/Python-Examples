import random

"Fake News Generator"

class Generate:
    
	def generate_name(self):
		names = ["ahmet","ali","mehmet","faruk"]
		return random.choice(names)

	def generate_surname(self):
		surnames = ["çan","şahin","çetin","yılmaz"]
		return random.choice(surnames)

	def events(self):
		events = [
			"{} {} isimli kullanıcı hacklendi",
			"{} {} öğrenci mit ye kabul edildi",
			"2000 doğumlu olan {} {} kişinin kemik testi 100 yaşında olduğunu söylüyor",
			"{} isimi kişi açgezen olan soyadını {}'a çevirdi",
			"{} {} isimli yaşlı kadının evine hırsız girdi",
			"{} {} şahıs 20 yıldır aranıyor !!",
			"yeni bir gezegene {} {} adı verildi",
		]

		return random.choice(events).format(self.generate_name(),self.generate_surname())


x=Generate()
print(x.events())