from config import app, api
from models import Post, Comment
from flask_restful import Resource
from flask import make_response, jsonify

#Challenge 1
# Create a GET route that goes to /api/sorted_posts. This route should return as json all the posts alphabetized by title.

# Challenge 2
# Create a GET route that goes to /api/posts_by_author/<author_name>. This route should return as json the post by the author's name. For example: /api/posts_by_author/sara would return all post that belong to sara.


# Challenge 3
# Create a GET route that goes to /api/search_posts/<title>. This route should return as json all the posts that include the title. Capitalization shouldn't matter. So if you were to use this route like /api/search_posts/frog. It would give back all post that include frog in the title.


# Challenge 4
# Create a GET route that goes to /api/posts_ordered_by_comments. This route should return as json the posts ordered by how many comments the post contains in descendeding order. So the post with the most comments would show first all the way to the post with the least showing last.

# Challenge 5
# Create a GET route that goes to /api/most_popular_commenter. This route should return as json a dictionary like { commenter: "Bob" } of the commenter that's made the most comments. Since commenter isn't a model, think of how you can count the comments that has the same commenter name.

if __name__ == "__main__":
  app.run(port=5555, debug=True)