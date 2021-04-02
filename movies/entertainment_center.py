import media


if __name__ == '__main__':
	toyStory = media.Movie('Toy Story',
							'Astory of a boy and his toys that come to life.',
							'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
							'https://www.youtube.com/watch?v=rNk1Wi8SvNc')

	print('\n***Toy Story***')
	print('Title:', toyStory.title)
	print('Storyline:', toyStory.storyline)
	print('Image:', toyStory.image)
	print('Trailer:', toyStory.trailer)


	avatar = media.Movie('Avatar',
						'A marine on an alien planet',
						'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
						'https://www.youtube.com/watch?v=5PSNL1qE6VY')

	print('\n***Avatar***')
	print('Title:', avatar.title)
	print('Storyline:', avatar.storyline)
	print('Image:', avatar.image)
	print('Trailer:', avatar.trailer)