"""
Custom Functions (UDFs)
"""

from xlwings import pro


@pro.func
def add(first, second, third=None):
    return first + second + third if third else first + second


@pro.func
async def add2(first, second):
    return first + second
