import media


if __name__ == '__main__':
	toyStory = media.Movie('Toy Story',
							'Astory of a boy and his toys that come to life.',
							'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
							'https://www.youtube.com/watch?v=rNk1Wi8SvNc')

	print('Title:', toyStory.title)
	print('Storyline:', toyStory.storyline)
	print('Image:', toyStory.image)
	print('Trailer:', toyStory.trailer)