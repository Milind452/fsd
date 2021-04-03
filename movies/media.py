import webbrowser


class Movie():
	def __init__(self, title, storyline, image, trailer):
		self.title = title
		self.storyline = storyline
		self.image = image
		self.trailer = trailer

	def showTrailer(self):
		webbrowser.open(self.trailer)

	def __str__(self):
		return '\nTitle: {}\nStoryline: {}\nImage: {}\nTrailer: {}\n'.format(self.title, self.storyline, self.image, self.trailer)