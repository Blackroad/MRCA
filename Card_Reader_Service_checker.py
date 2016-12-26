import asyncio
import websockets
import re





async def Card_Reader_thread():

    async with websockets.connect('ws://localhost:4000') as websocket:
        while True:
            greeting = await websocket.recv()
            state = ["0", "1609561978", "1609562107", "-2146435049"]
            result = re.findall(r'\w+', greeting)
            if  result[1] == state[0]:
                result_state = '\nUser Card status: Card is initialized'
                result_data_name = '\nUser First Name / Last Name : {} {}\nUserlogin : {}\nUser ID : {}'.format(result[4], result [6], result [8], result [10])
                print (result_state,"\nRecieved Data:", result_data_name)
            elif result[1] == state[1]:
                 result_state = '\nUser Card status: Card not Initialized'
                 result_message = result[3:]
                 print (result_state,'\n'+ "Reason is:" + ' '+(' '.join([i for i in result_message])))
            elif result[1] == state[2]:
                 result_state = '\nUser Card status: Card not Initialized'
                 result_message = result[3:]
                 print(result_state, '\n' + "Reason is:" + ' ' + (' '.join([i for i in result_message])))
            elif state[3]:
                 result_state = '\nUser Card status: Card not Initialized'
                 result_message = result[2:]
                 print(result_state, '\n' + "Reason is:" + ' ' + (' '.join([i for i in result_message])))

asyncio.get_event_loop().run_until_complete(Card_Reader_thread())
