from spyne import rpc, ServiceBase, Iterable, Integer, Unicode

class MultiplyService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def multiply(ctx, first_number, second_number):
        return first_number * second_number