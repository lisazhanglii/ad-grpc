import unittest
from unittest.mock import MagicMock
from client.client_utilities import retrieve_and_expand_post_comments

class TestRetrievePostDetails(unittest.TestCase):
    def setUp(self):
        self.api_client = MagicMock()
        self.api_client.post_stub.RetrievePost.return_value = MagicMock(post=MagicMock(post_id='123'))
        self.api_client.comment_stub.RetrieveTopComments.return_value = MagicMock(comments=[MagicMock(comment_id='456', score=10)])
        self.api_client.comment_stub.ExpandCommentBranch.return_value = MagicMock(comments=[MagicMock(replies=[MagicMock(text='Top Reply')])])

    def test_retrieve_post_details_with_replies(self):
        result = retrieve_and_expand_post_comments(self.api_client, 'Test Post')
        self.assertEqual(result, 'Top Reply')

    def test_retrieve_post_details_without_replies(self):
        self.api_client.comment_stub.ExpandCommentBranch.return_value = MagicMock(comments=[])
        result = retrieve_and_expand_post_comments(self.api_client, 'Test Post')
        self.assertIsNone(result)

    def test_retrieve_post_details_without_comments(self):
        self.api_client.comment_stub.RetrieveTopComments.return_value = MagicMock(comments=[])
        result = retrieve_and_expand_post_comments(self.api_client, 'Test Post')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
