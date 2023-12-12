import grpc
from concurrent import futures
import time
import argparse
import user_pb2
import user_pb2_grpc
import post_pb2
import post_pb2_grpc
import comment_pb2
import comment_pb2_grpc
import update_monitor_pb2
import update_monitor_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime
import subreddit_pb2
import subreddit_pb2_grpc

# Mock database for subreddits
subreddits = {}

# Mock database (for demonstration purposes)
users = {}
posts = {}
comments = {}

# Implement the service classes
class UserService(user_pb2_grpc.UserServicer):
    def CreateUser(self, request, context):
        if request.user_id in users:
            return user_pb2.UserResponse(status="User already exists.")
        users[request.user_id] = request
        return user_pb2.UserResponse(status="User created successfully.")

class PostService(post_pb2_grpc.PostServicer):
    def __init__(self, db):
        self.db = db
    def CreatePost(self, request, context):
        if self.db.post_exists(request.title):
            return post_pb2.PostResponse(status="Post already exists.")
        success = self.db.add_post(request.title, request.text, request.video_url, request.image_url, request.author, request.score, request.state, request.publication_date)
        if success:
            return post_pb2.PostResponse(status="Post created successfully.")
        else:
            return post_pb2.PostResponse(status="Failed to create post.")
    
    def UpvotePost(self, request, context):
        if self.db.post_exists(request.title):
            self.db.update_post_score(request.title, 1)
            return post_pb2.PostResponse(status="Post upvoted.")
        return post_pb2.PostResponse(status="Post not found.")

    def DownvotePost(self, request, context):
        if self.db.post_exists(request.title):
            self.db.update_post_score(request.title, -1)
            return post_pb2.PostResponse(status="Post downvoted.")
        return post_pb2.PostResponse(status="Post not found.")

    def RetrievePost(self, request, context):
        post = self.db.get_post(request.title)
        if post:
            return post
        return post_pb2.Post(status="Post not found.")

class CommentService(comment_pb2_grpc.CommentServicer):
    def CreateComment(self, request, context):
        if request.text in comments:
            return comment_pb2.CommentResponse(status="Comment already exists.")
        comments[request.text] = request
        return comment_pb2.CommentResponse(status="Comment created successfully.")
    def UpvoteComment(self, request, context):
        if request.text in comments:
            comments[request.text].score += 1
            return comment_pb2.CommentResponse(status="Comment upvoted.")
        return comment_pb2.CommentResponse(status="Comment not found.")

    def DownvoteComment(self, request, context):
        if request.text in comments:
            comments[request.text].score -= 1
            return comment_pb2.CommentResponse(status="Comment downvoted.")
        return comment_pb2.CommentResponse(status="Comment not found.")

    def RetrieveTopComments(self, request, context):
        post_id = request.post_id
        top_n = request.top_n

        # Filter comments for the given post
        post_comments = [comment for comment in comments.values() if comment.post_id == post_id]

        # Sort comments by score (descending)
        sorted_comments = sorted(post_comments, key=lambda c: c.score, reverse=True)

        # Select the top N comments
        top_comments = sorted_comments[:top_n]

        return comment_pb2.TopCommentsResponse(comments=top_comments)


    def ExpandCommentBranch(self, request, context):
        root_comment_id = request.comment_id
        max_depth = 2  # As specified in your requirements

        expanded_comments = expand_branch(root_comment_id, 0, max_depth)

        return comment_pb2.CommentBranchResponse(comments=expanded_comments)

    def expand_branch(comment_id, depth, max_depth):
        if depth > max_depth:
            return []

        # Find child comments
        child_comments = [comment for comment in comments.values() if comment.parent_id == comment_id]

        # Sort by score
        sorted_child_comments = sorted(child_comments, key=lambda c: c.score, reverse=True)

        # Expand each child comment's branch
        for child_comment in sorted_child_comments:
            child_comment.replies = expand_branch(child_comment.id, depth + 1, max_depth)

        return sorted_child_comments
class UpdateMonitorService(update_monitor_pb2_grpc.UpdateMonitorServicer):
    def MonitorUpdates(self, request_iterator, context):
        # Implementation for streaming updates
        for request in request_iterator:
            # Logic to handle incoming requests and stream updates
            yield update_monitor_pb2.UpdateResponse(status="Update Received")



class SubredditService(subreddit_pb2_grpc.SubredditServicer):
    def CreateSubreddit(self, request, context):
        if request.name in subreddits:
            return subreddit_pb2.SubredditResponse(status="Subreddit already exists.")
        subreddits[request.name] = request
        return subreddit_pb2.SubredditResponse(status="Subreddit created successfully.")


class UpdateMonitorService(update_monitor_pb2_grpc.UpdateMonitorServicer):
    def MonitorUpdates(self, request_iterator, context):
        for request in request_iterator:
            if request.type == update_monitor_pb2.UpdateRequest.POST:
                post = posts.get(request.id, None)
                if post:
                    yield update_monitor_pb2.UpdateResponse(post_title=post.title, post_score=post.score)
            elif request.type == update_monitor_pb2.UpdateRequest.COMMENT:
                comment = comments.get(request.id, None)
                if comment:
                    yield update_monitor_pb2.UpdateResponse(comment_text=comment.text, comment_score=comment.score)

# Create a server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicerServicer_to_server(UserService(), server)
    post_pb2_grpc.add_PostServicerServicer_to_server(PostService(), server)
    comment_pb2_grpc.add_CommentServicerServicer_to_server(CommentService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gRPC Server for Reddit-like Service')
    parser.add_argument('--port', type=int, default=50051, help='Port to listen on')
    args = parser.parse_args()

    serve(args.port)
