import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story', 
'Story of a boy and his toys that come to life',
'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
'https://www.youtube.com/watch?v=CxwTLktovTU')

#print(toy_story.storyline)
avatar = media.Movie('Avatar',
'marine on an alien planet',
'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
'https://www.youtube.com/watch?v=5PSNL1qE6VY')

mission_impossible = media.Movie('Mission Impossible',
'A framed secret agent goes on to prove his innocence',
'https://upload.wikimedia.org/wikipedia/en/e/e1/MissionImpossiblePoster.jpg',
'https://www.youtube.com/watch?v=Ohws8y572KE')

national_treasure = media.Movie('National Treasure',
'A historian on a quest to find a lost treasure',
'https://upload.wikimedia.org/wikipedia/en/1/12/Movie_national_treasure.JPG',
'https://www.youtube.com/watch?v=mcf4tXYjaxo')

#toy_story.show_trailer()

movies = [toy_story, avatar, mission_impossible, national_treasure]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)