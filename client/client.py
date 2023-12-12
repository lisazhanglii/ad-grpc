import grpc
import server.user_pb2_grpc
import server.post_pb2_grpc
import server.comment_pb2_grpc
import server.subreddit_pb2_grpc
import server.update_monitor_pb2_grpc
import server.post_pb2 as post_pb2
import server.comment_pb2 as comment_pb2
import time

class RedditClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.user_stub = server.user_pb2_grpc.UserStub(self.channel)
        self.post_stub = server.post_pb2_grpc.PostStub(self.channel)
        self.comment_stub = server.comment_pb2_grpc.CommentStub(self.channel)
        self.subreddit_stub = server.subreddit_pb2_grpc.SubredditStub(self.channel)
        self.update_monitor_stub = server.update_monitor_pb2_grpc.UpdateMonitorStub(self.channel)

    def create_user(self, user_id):
        # Implement the method to create a user
        pass

    def monitor_updates(self, post_id):
        request_iterator = self._generate_update_requests(post_id)
        for response in self.update_monitor_stub.MonitorUpdates(request_iterator):
            print(f"Received update: {response}")
    
    def _generate_update_requests(self, post_id):
        while True:
            # In a real application, this would be triggered by some condition
            yield server.update_monitor_pb2.UpdateRequest(id=post_id, type=server.update_monitor_pb2.UpdateRequest.POST)
            time.sleep(1)  # Simulate waiting for an update
    def retrieve_post(self, title):
        """Retrieve a post by its title."""
        return self.post_stub.RetrievePost(post_pb2.PostRequest(title=title))

    def retrieve_top_comments(self, post_id, top_n=1):
        """Retrieve the top N comments for a post."""
        return self.comment_stub.RetrieveTopComments(comment_pb2.TopCommentsRequest(post_id=post_id, top_n=top_n))

    def expand_comment_branch(self, comment_id, max_depth=1):
        """Expand the comment branch to retrieve replies."""
        return self.comment_stub.ExpandCommentBranch(comment_pb2.CommentBranchRequest(comment_id=comment_id, max_depth=max_depth))

if __name__ == '__main__':
    client = RedditClient()
    post = client.retrieve_post('xxpost')
    top_comments = client.retrieve_top_comments(post_id=post.post_id, top_n=1)
    if top_comments.comments:
        most_upvoted_comment = top_comments.comments[0]
        expanded_comment = client.expand_comment_branch(comment_id=most_upvoted_comment.comment_id, max_depth=1)
