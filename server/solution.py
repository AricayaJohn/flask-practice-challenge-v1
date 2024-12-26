# from config import app, api
# from models import Post, Comment
# from flask_restful import Resource
# from flask import make_response, jsonify

# #Challenge 1
# # Create a GET route that goes to /api/sorted_posts. This route should return as json all the posts alphabetized by title.
# class SortedPosts(Resource):
#   def get(self):
#     posts = Post.query.order_by(Post.title).all()
#     post_dict = [post.to_dict() for post in posts]
#     return make_response(jsonify(post_dict), 200)

# api.add_resource(SortedPosts, '/api/sorted_posts')

# # Challenge 2
# # Create a GET route that goes to /api/posts_by_author/<author_name>. This route should return as json the post by the author's name. For example: /api/posts_by_author/sara would return all post that belong to sara.
# class PostsByAuthor(Resource):
#   def get(self, author_name):
#     name = author_name.title()
#     posts = Post.query.filter(Post.author == name).all()
#     if posts:
#       post_dict = [post.to_dict() for post in posts]
#       return make_response(jsonify(post_dict), 200)
#     return make_response(jsonify({'Error': 'Not Found'}), 404)

# api.add_resource(PostsByAuthor, '/api/posts_by_author/<author_name>')

# # Challenge 3
# # Create a GET route that goes to /api/search_posts/<title>. This route should return as json all the posts that include the title. Capitalization shouldn't matter. So if you were to use this route like /api/search_posts/frog. It would give back all post that include frog in the title.
# class PostsByTitle(Resource):
#   def get(self, title):
#     posts = Post.query.filter(Post.title.contains(title)).all()
#     if posts:
#       post_dict = [post.to_dict() for post in posts]
#       return make_response(jsonify(post_dict), 200)
#     return make_response(jsonify({'Error': "not found"}), 404)

# api.add_resource(PostsByTitle, '/api/search_posts/<title>')

# # Challenge 4
# # Create a GET route that goes to /api/posts_ordered_by_comments. This route should return as json the posts ordered by how many comments the post contains in descendeding order. So the post with the most comments would show first all the way to the post with the least showing last.
# class PostsByComments(Resource):
#   def get(self):
#     posts = Post.query.outerjoin(Comment).group_by(Post.id).order_by(func.count(Comment.id).desc()).all()
#     post_dict = [post.to_dict for post in posts]
#     return make_response(jsonify(post_dict), 200)

# api.add_resource(PostsByComments, '/api/posts_ordered_by_comments')

# # Challenge 5
# # Create a GET route that goes to /api/most_popular_commenter. This route should return as json a dictionary like { commenter: "Bob" } of the commenter that's made the most comments. Since commenter isn't a model, think of how you can count the comments that has the same commenter name.
# class MostPopularCommenter(Resource):
#   def get(self):
#     most_popular_commenter = (
#       Comment.query.group_by(Comment.commenter)
#       .order_by(func.count(Comment.id).desc())
#       .first()
#     )
#     if most_popular_commenter:
#     return make_response(jsonify({'commenter': most_popular_commenter.commenter}), 200)

#   return make_response(jsonify({'error': "not found"}), 404)

# api.add_resource(MostPopularCommenter, '/api/most_popular_commenter')

# if __name__ == "__main__":
#   app.run(port=5555, debug=True)