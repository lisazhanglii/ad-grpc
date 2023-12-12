import server.post_pb2
import server.post_pb2 as post_pb2
import server.comment_pb2 as comment_pb2


def retrieve_and_expand_post_comments(client, post_title):
    """
    Retrieves a post, the most upvoted comments under it, and expands the most upvoted comment.
    :param client: Instance of RedditClient
    :param post_title: The title of the post
    :return: The most upvoted reply under the most upvoted comment or None
    """
    post = client.post_stub.RetrievePost(post_pb2.PostRequest(title=post_title))
    if not post:
        return None

    top_comments = client.comment_stub.RetrieveTopComments(comment_pb2.TopCommentsRequest(post_id=post.post_id, top_n=1))
    if not top_comments.comments:
        return None

    most_upvoted_comment = top_comments.comments[0]
    expanded_comments = client.comment_stub.ExpandCommentBranch(comment_pb2.CommentBranchRequest(comment_id=most_upvoted_comment.comment_id, max_depth=1))

    if expanded_comments and expanded_comments.comments:
        return expanded_comments.comments[0].text
    else:
        return None
