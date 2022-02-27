# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pingpong_pb2 as pingpong__pb2


class PingPongServiceStub(object):
    """my service is called PingPongService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping = channel.unary_unary(
                '/PingPongService/ping',
                request_serializer=pingpong__pb2.Ping.SerializeToString,
                response_deserializer=pingpong__pb2.Pong.FromString,
                )


class PingPongServiceServicer(object):
    """my service is called PingPongService
    """

    def ping(self, request, context):
        """an example of getting a feature
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PingPongServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=pingpong__pb2.Ping.FromString,
                    response_serializer=pingpong__pb2.Pong.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PingPongService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PingPongService(object):
    """my service is called PingPongService
    """

    @staticmethod
    def ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PingPongService/ping',
            pingpong__pb2.Ping.SerializeToString,
            pingpong__pb2.Pong.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
