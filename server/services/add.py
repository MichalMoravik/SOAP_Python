from spyne import rpc, ServiceBase, Iterable, Integer, Unicode

class AddService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, first_number, second_number):
        return first_number + second_number 