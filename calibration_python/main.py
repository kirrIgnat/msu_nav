from all_calibration.acs import acs
from all_calibration.acs_sec import acs_sec
from all_calibration.dus import dus
from all_calibration.dus_sec import dus_sec

end = False


while end==False:
    print('input value')
    counter = input()
    if counter == '1':
        name = 'data/INS-MEMS1.LOG'
        file = open(name, 'r')
        fig = acs(file)
    elif counter == '2':
        name = 'data/INS-MEMS1.LOG'
        file = open(name, 'r')
        fig = acs_sec(file)
    elif counter == '3':
        name = 'data/INS-MEMS2b.LOG'
        file = open(name, 'r')
        fig = dus(file)
    elif counter == '4':
        name = 'data/INS-MEMS2b.LOG'
        file = open(name, 'r')
        fig = dus_sec(file)
    else:
        end = True
        break
    fig.show()


