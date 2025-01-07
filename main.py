from SENSOR.exception import SensorException

import os
import sys

from SENSOR.logger import logging


def test_exception():
    try:
        logging.info("ki yaha p bhaia ek error ayegi divion by zero vali error")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)
    
    


if __name__ == "__main__":
    try:
        test_exception()
        pass
    except Exception as e:
        print(e)