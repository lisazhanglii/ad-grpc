# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc



class UserServicerStub(object):
    """RPC methods go here
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """


class UserServicerServicer(object):
    """RPC methods go here
    """


def add_UserServicerServicer_to_server(servicer, server):
    rpc_method_handlers = {
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UserServicer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserServicer(object):
    """RPC methods go here
    """
