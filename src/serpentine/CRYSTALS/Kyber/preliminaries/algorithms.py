def Parse(bytes_stream):
    return bytes_stream


def CBD(n, bytes_array):
    beta = BytesToBits(bytes_array)
    return bytes_array


def Decode(l, bytes_array):
    beta = BytesToBits(bytes_array)
    return bytes_array


def BytesToBits(bytes_array):
    list_of_bitlists_strings = [list('{0:08b}'.format(B)) for B in bytes_array]
    bits_array = [int(bit)
                  for bitlist in list_of_bitlists_strings for bit in bitlist]

    return bits_array


"""
from sympy import ntt

    q = 3329
    transform = ntt(byte_stream, q)
    return transform
"""
