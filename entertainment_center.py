import media

toystory_title = "Toy Story"
toystory_storyline = "a boy yadiyadi"
toystory_img = "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
toystory_trailer = "https://www.youtube.com/watch?v=vwyZH85NQC4"


toy_story = media.Movie(toystory_title,
                        toystory_storyline,
                        toystory_img,
                        toystory_trailer)

avatar = media.Movie(toystory_title,
                     toystory_storyline,
                     toystory_img,
                     toystory_trailer)

print(toy_story.storyline)
print(avatar.storyline)

avatar.show_trailer()
