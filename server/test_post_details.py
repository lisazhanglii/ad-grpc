import unittest
from unittest.mock import MagicMock
import comment_pb2
import post_pb2
from client.client_utilities import retrieve_and_expand_post_comments

class TestRetrievePostDetails(unittest.TestCase):
   def setUp(self):
        self.api_client = MagicMock()
      
        self.api_client.retrieve_post.return_value = post_pb2.PostResponse(post=post_pb2.Post(post_id='123', title='Test Post', text='Content', score=5))
     
        self.api_client.retrieve_top_comments.return_value = comment_pb2.TopCommentsResponse(comments=[comment_pb2.Comment(comment_id='456', text='Top Comment', score=10, replies=[])])
     
        self.api_client.expand_comment_branch.return_value = comment_pb2.CommentBranchResponse(comments=[comment_pb2.Comment(text='Top Reply', replies=[comment_pb2.Comment(text='Reply')])])

def test_retrieve_post_details_with_replies(self):
        mock_post_response = post_pb2.PostResponse(post=post_pb2.Post(post_id='123'))
        self.api_client.retrieve_post.return_value = mock_post_response

        mock_comments_response = comment_pb2.TopCommentsResponse(
            comments=[comment_pb2.Comment(comment_id='456', score=10, replies=[comment_pb2.Comment(text='Top Reply')])]
        )
        self.api_client.retrieve_top_comments.return_value = mock_comments_response

def test_retrieve_post_details_without_replies(self):
        self.mock_expanded_comment_response = comment_pb2.CommentBranchResponse(
            comments=[comment_pb2.Comment(text='Top Comment', replies=[])]
        )
        self.api_client.expand_comment_branch.return_value = self.mock_expanded_comment_response
        
        result = retrieve_and_expand_post_comments(self.api_client, 'Test Post')
        self.assertIsNone(result)

def test_retrieve_post_details_without_comments(self):
        self.mock_top_comments_response = comment_pb2.TopCommentsResponse(comments=[])
        self.api_client.retrieve_top_comments.return_value = self.mock_top_comments_response

        result = retrieve_and_expand_post_comments(self.api_client, 'Test Post')
        self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()
