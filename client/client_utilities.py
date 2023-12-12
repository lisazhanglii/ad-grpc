import server.post_pb2
import server.post_pb2 as post_pb2
import server.comment_pb2 as comment_pb2


def retrieve_and_expand_post_comments(client, post_title):
    """
    Retrieves a post, the most upvoted comments under it, and expands the most upvoted comment.
    """
    post_response = client.retrieve_post(post_title)
    if post_response is None or not hasattr(post_response, 'post'):
        return None

    post = post_response.post
    top_comments_response = client.retrieve_top_comments(post.post_id, top_n=1)
    if not top_comments_response.comments:
        return None

    most_upvoted_comment = top_comments_response.comments[0]
    expanded_comments_response = client.expand_comment_branch(most_upvoted_comment.comment_id, max_depth=1)
    if not expanded_comments_response.comments or not expanded_comments_response.comments[0].replies:
        return None

    return expanded_comments_response.comments[0].replies[0].text
