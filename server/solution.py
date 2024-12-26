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


#create a production model 
class production(db.Model):
    __tablename__ = 'productiion'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.column(db.String)
    ongoing = db.column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    update_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f'Production Title: {self.title}, Genre: {self.genre}, Budget: {self.budget}, Image: {self.image}, Director: {self.description}, Ongoing: {self.ongoing}, Creted_at: {self.created_at}, Updated_at: {self.updated_at}'

#createing app route
@app.route('/productions/<string:title>')
def production = Production.query.filter(Production.title == title).first()
    production_response = {
        "title": production.title,
        "genre": production.genre,
        "director": production.director,
        "description": production.description,
        "image": production.image,
        "budget": production.budget,
        "ongoing": productiion.ongoing
    }

    response = make_response(jsonify(production_response), 200)
    return response


#create a get all request 
class Production(Resource):
def get(self):
    production_list = [p.to_dict() for p in Production.query.all()]
    response = make_response(
        production_list, 200
    )
    return response

#create a post request
    def post(self):
        form_json = request.get_json()
        try:
            new_production = Production(
                title = form_json['title'],
                genre = form_json['genre'],
                budget = int(form_json['budget']),
                image = form_json['image'],
                director = form_json['director'],
                description = form_json['description']
            )
        except ValueError as e:
            abort(422,e.args[0])

        db.session.add(new_production)
        db.session.commit()

        response_dict = new_production.to_dict()

        response = make_response(
            response_dict,
            201,
        )

        return response
api.add_resource(Productions, '/productions')

class ProductionByID(Resource):
    def get(self, id):
        production = Production.query.filter_by(id=id).first()
        if not Production:
            abort(404, 'The production you were looking for was not found')
        production_dict = production.to_dict()
        response = make_response(
            production_dict,
            200
        )

        return response

    def patch(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
                abort(404, 'The production you were trying to update was not found')
        request_json = request.get_json()
        for key in request_json:
            setattr(production, key, request_json[key])

        db.session.add(production)
        db.session.commit()

        response = make_response(
            production.to_dict(),
            200
        )

        return response

    def delete(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            abort(404, 'The Production you were lookingfor was not found!')
        db.session.delete(production)
        db.session.commit()

        response = make_response(', 204')

        return response

    api.add_resource(ProductionByID, '/production/<int:id>')


@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        'Not Found: Sorry the resource you are looking for does not exist',
        404
    )

    return respionse

class CastMembers(Resource):
    def get(self):
        cast_members_list = [cast_member.to_dict() for cast_member in CastMember.query.all()]

        resonse = make_response(
            cast_members_list,
            200
        )
        return response

    def post(self):
        request_json = request.get_json()
        new_cast = CastMember(
            name = request_json['name'],
            role = request_json['role'],
            production_id = request_json['production_id']
        )

        db.session.add(new_cast)
        db.session.commit()

        response_dict = new_cast.to_dict()

        response = make_response(
            response_dict,
            201
        )
        return response

api.add_resource(CastMembers, '/cast_members')

class CastMembersById(Resource):
    def get(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            abourt(404, 'The Production you were looking for was not found!')

        production_dict = production.to_dict()
        response = make_response(
            production_dict,
            200
        )

        return resonse

    def delete(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            abort(404, 'The production you were trying to delete was not found!')

        db.session.delete(production)
        db.session.commit()

        response = make_response('', 204)

        return response

api.add_resource()CastMembersById, '/cast_members/<int:id>'

#create user table db https://github.com/learn-co-curriculum/SENG-LIVE-Phase-4-flask-010923/blob/06-solution/06-Auth-pt2/server/models.py
#class signup, login, log out app.py


#create a login
class Login(resource):
    def post(self):
        username = request.get_json()['username']
        user = User.query.filter(User.username == username).first()

        session['user_id'] = user.id

        return user.to_dict(), 200

api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None

        return {}, 204

api.add_resource(Logout, '/logout')

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            return user.to_dict(), 200

        return {}, 401

api.add_resource(CheckSession, '/check_session')


#Authorization for members restricted articles
class MembersOnlyIndex(Resource):
    def get(self):
        if not session.get('user_id'):
            return {'message': 'unauthorized access'}, 401

        articles = Article.query.filter(Article.is_member_only == True).all()
        return [article.to_dict() for article in articles], 200

api.add_resource(MemberOnlyIndex, '/members_only_articles', endpoint='member_index')

class MemberOnlyArticle(Resource):
    def get(self, id):
        if not session.get('user_id'):
            return {'message': 'Unauthorized access'}, 401

        article = Article.query.filter(Article.id == id).first()
        return article.to_dict(), 200

api.add_resource(MemberOnlyArticle, '/members_only_articles/<int:id>', endpoint='member_article')
