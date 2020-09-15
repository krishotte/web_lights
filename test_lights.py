from m_socket import socket_data as sdata
from m_socket import socket_connection as sconn


conn = sconn()
s_data = sdata()


def get_lights():

    conn.connect()

    sockstr = s_data.constr(1, 0, [0, 0, 0, 0])
    # print(f' socket sending: {sockstr}')
    conn.client_socket.send(sockstr)
    recv1 = conn.client_socket.recv(32)
    # print(f' socet receiving: {recv1}')

    curr_setup = s_data.deconstr(recv1)
    # print(f'current setup: {curr_setup}')

    conn.disconnect()
    return curr_setup[2]


def set_lights(channel, level):
    current_setup = get_lights()
    current_setup[channel] = level

    conn.connect()

    sockstr = s_data.constr(2, channel, current_setup)
    print(f' socket sending: {sockstr}')
    conn.client_socket.send(sockstr)
    recv1 = conn.client_socket.recv(32)
    print(f' socet receiving: {recv1}')

    curr_setup = s_data.deconstr(recv1)
    print(f'current setup: {curr_setup}')

    conn.disconnect()


if __name__ == '__main__':
    print(f' current setup: {get_lights()}')
