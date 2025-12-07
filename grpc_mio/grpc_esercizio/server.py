from concurrent import futures
import grpc,time,sys
import uuid
import order_management_pb2
import order_management_pb2_grpc
import logging


class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.order_dict = {}


    def addOrder(self,request,context):

        id = uuid.uuid1()
        request.id = str(id)
        self.order_dict[request.id]=request
        response = order_management_pb2.StringMessage(value =str(id))

        print("addOrder")
        print(self.order_dict)
        print(type(self.order_dict))
        types_keys = [type(k) for k in self.order_dict.keys()]
        types_values = [type(k) for k in self.order_dict.values() ]
        logging.debug("[OrderManagementService] AddOrder to dictionary, id: ",str(id))
        return response

    def getOrder(self,request,context):
        order = self.order_dict.get(request.value)

        if order is not None:
            logging.debug('[OrderManagementService] getOrder returning order: '+str(order))
            return order
        else:
            logging.debug('[OrderManagementService] order not found in dict '+request.value)

            context.set_code(grpc.StatusCode.NOT_FOUND)

            context.set_details('Order: ', request.value + " NOT FOUND!")

            return order_management_pb2.Order()

    


    def searchInventory(self,query):
        matching_orders = []
        for order_id,order in slef.order_dict.items:
            for itm in order.items:
                if query in itm:
                    matching_orders.append(order)
                    break
        return matching_orders

    def searchOrder(self,request,context):
        logging.debug('Searching order in the dict with item equal to:  ',request.item)

        matching_orders =self.searchInventory(request.value)
        for order in matching_orders:
            yield order
        
    def processOrder(self,request,context):
        location_dict = []
        logging.debug('[OrderManagementService] processing the order...')
        for order in request_iterator:
            if order.destination not in location_dict.keys:
                location_dict[order.destination]=[order]

            else:
                location_dict[order.destination].append(order)

        for key,value in location_dict.items():
            shipment_id =uuid.uuid1()
            order_management_pb2.CombinedShipment(id=str(shipment_id),status='PROCESED',order= location_dict[key])
            yield shipment
            logging.debug('[OrderManagementService] processed order with id: '+str(shipment_id))

        logging.debug('[OrderManagementService] Processing all the orders!')

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=[('grpc.so_reuseport', 0)])
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(),server)

    port = 0

    port = server.add_insecure_port('0.0.0.0:0'+str(port))
    logging.debug("Starting process on port: "+str(port))

    server.start()

    server.wait_for_termination()
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
    serve()
    