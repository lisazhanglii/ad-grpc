import server.post_pb2
import server.post_pb2 as post_pb2
import server.comment_pb2 as comment_pb2

def retrieve_and_expand_post_comments(client, post_title):
    post_response = client.retrieve_post(post_title)
    if not post_response or not post_response.post:
        return None

    top_comments_response = client.retrieve_top_comments(post_response.post.post_id, top_n=1)
    if not top_comments_response.comments:
        return None

    most_upvoted_comment = top_comments_response.comments[0]
    expanded_comments_response = client.expand_comment_branch(most_upvoted_comment.comment_id, max_depth=1)

    if not expanded_comments_response.comments or not expanded_comments_response.comments[0].replies:
        return None

    # Sort replies by score and return the text of the most upvoted reply
    most_upvoted_reply = sorted(expanded_comments_response.comments[0].replies, key=lambda reply: reply.score, reverse=True)[0]
    return most_upvoted_reply.text