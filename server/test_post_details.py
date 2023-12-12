import unittest
from unittest.mock import MagicMock
import comment_pb2
import post_pb2
from client.client_utilities import retrieve_and_expand_post_comments

class TestRetrievePostDetails(unittest.TestCase):
    def setUp(self):
        self.api_client = MagicMock()

        # Mock post retrieval
        self.api_client.retrieve_post.return_value = post_pb2.PostResponse(
            post=post_pb2.Post(post_id='123', title='Test Post', text='Content', score=5)
        )

        # Mock top comments retrieval
        self.api_client.retrieve_top_comments.return_value = comment_pb2.TopCommentsResponse(
            comments=[comment_pb2.Comment(comment_id='456', text='Top Comment', score=10)]
        )

        # Mock expanded comment branch retrieval
        self.api_client.expand_comment_branch.return_value = comment_pb2.CommentBranchResponse(
            comments=[comment_pb2.Comment(text='Top Comment', replies=[
                comment_pb2.Comment(text='Top Reply', score=15),
                comment_pb2.Comment(text='Other Reply', score=5)
            ])]
        )

    def test_retrieve_post_details_with_most_upvoted_reply(self):
        result = retrieve_and_expand_post_comments(self.api_client, 'Test Post')
        self.assertEqual(result, 'Top Reply')  # Asserting the most upvoted reply is returned

    def test_retrieve_post_details_without_replies(self):
        self.api_client.expand_comment_branch.return_value = comment_pb2.CommentBranchResponse(
            comments=[comment_pb2.Comment(text='Top Comment', replies=[])]
        )
        result = retrieve_and_expand_post_comments(self.api_client, 'Test Post')
        self.assertIsNone(result)

    def test_retrieve_post_details_without_comments(self):
        self.api_client.retrieve_top_comments.return_value = comment_pb2.TopCommentsResponse(comments=[])
        result = retrieve_and_expand_post_comments(self.api_client, 'Test Post')
        self.assertIsNone(result)

    def test_retrieve_post_details_no_post(self):
        self.api_client.retrieve_post.return_value = None
        result = retrieve_and_expand_post_comments(self.api_client, 'Nonexistent Post')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
