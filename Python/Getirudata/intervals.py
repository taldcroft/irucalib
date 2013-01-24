"""
IRU processing intervals, for historical backward compatibility.
"""

def get_interval(interval):
    if (interval == 1):
        tstart = '2003:274:14:00:00.000'  # start time for interval 01
        tstop  = '2004:093:00:00:00.000'  # stop time for interval 01
        interval = 'i01'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 2):
        tstart = '2004:093:00:00:00.000'  # start time for interval 02
        tstop  = '2004:276:00:00:00.000'  # stop time for interval 02
        interval = 'i02'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 3):
        tstart = '2004:276:00:00:00.000'  # start time for interval 03
        tstop  = '2005:092:00:00:00.000'  # stop time for interval 03
        interval = 'i03'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 4):
        tstart = '2005:092:00:00:00.000'  # start time for interval 04
        tstop  = '2005:275:00:00:00.000'  # stop time for interval 04
        interval = 'i04'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 5):
        tstart = '2005:275:00:00:00.000'  # start time for interval 05
        tstop  = '2006:090:00:00:00.000'  # stop time for interval 05
        interval = 'i05'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 6):
        tstart = '2006:090:00:00:00.000'  # start time for interval 06
        tstop  = '2006:271:00:00:00.000'  # stop time for interval 06
        interval = 'i06'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 7):
        tstart = '2006:271:00:00:00.000'  # start time for interval 07
        tstop  = '2006:352:00:00:00.000'  # stop time for interval 07
        interval = 'i07'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 8):
        tstart = '2006:352:16:00:00.000'  # start time for interval 08
        tstop  = '2007:148:00:00:00.000'  # stop time for interval 08
        interval = 'i08'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 9):
        tstart = '2007:148:00:00:00.000'  # start time for interval 09
        tstop  = '2007:306:00:00:00.000'  # stop time for interval 09
        interval = 'i09'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 10):
        tstart = '2007:306:00:00:00.000'  # start time for interval 10
        tstop  = '2008:060:00:00:00.000'  # stop time for interval 10
        interval = 'i10'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 11):
        tstart = '2008:060:00:00:00.000'  # start time for interval 11
        tstop  = '2008:186:00:00:00.000'  # stop time for interval 11
        interval = 'i11'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 12):
        tstart = '2008:186:00:00:00.000'  # start time for interval 12
        tstop  = '2008:319:00:00:00.000'  # stop time for interval 12
        interval = 'i12'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 13):
        tstart = '2008:319:00:00:00.000'  # start time for interval 13
        tstop  = '2009:052:00:00:00.000'  # stop time for interval 13
        interval = 'i13'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 14):
        tstart = '2009:052:00:00:00.000'  # start time for interval 14
        tstop  = '2009:156:00:00:00.000'  # stop time for interval 14
        interval = 'i14'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 15):
        tstart = '2009:156:00:00:00.000'  # start time for interval 15
        tstop  = '2009:275:00:00:00.000'  # stop time for interval 15
        interval = 'i15'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 16):
        tstart = '2009:275:00:00:00.000'  # start time for interval 16
        tstop  = '2010:001:00:00:00.000'  # stop time for interval 16
        interval = 'i16'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 17):
        tstart = '2010:001:00:00:00.000'  # start time for interval 17
        tstop  = '2010:106:00:00:00.000'  # stop time for interval 17
        interval = 'i17'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 18):
        tstart = '2010:106:00:00:00.000'  # start time for interval 18
        tstop  = '2010:204:00:00:00.000'  # stop time for interval 18
        interval = 'i18'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 19):
        tstart = '2010:204:00:00:00.000'  # start time for interval 19
        tstop  = '2010:302:00:00:00.000'  # stop time for interval 19
        interval = 'i19'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 20):
        tstart = '2010:302:00:00:00.000'  # start time for interval 20
        tstop  = '2010:350:20:00:00.000'  # stop time for interval 20
        interval = 'i20'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 21):
        tstart = '2010:351:00:00:00.000'  # start time for interval 21
        tstop  = '2011:105:21:20:00.000'  # stop time for interval 21
        interval = 'i21'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 22):
        tstart = '2011:105:21:20:00.000'  # start time for interval 22
        tstop  = '2011:187:08:00:00.000'  # stop time for interval 22
        interval = 'i22'                  # stops before Safe Mode 4
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 23):                # starts after Safe Mode 4
        tstart = '2011:192:03:00:00.000'  # start time for interval 23
        tstop  = '2011:257:00:00:00.000'  # stop time for interval 23
        interval = 'i23'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 24):
        tstart = '2011:257:00:00:00.000'  # start time for interval 24
        tstop  = '2011:319:00:00:00.000'  # stop time for interval 24
        interval = 'i24'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 25):
        tstart = '2011:319:00:00:00.000'  # start time for interval 25
        tstop  = '2012:022:00:00:00.000'  # stop time for interval 25
        interval = 'i25'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 26):
        tstart = '2012:022:00:00:00.000'  # start time for interval 26
        tstop  = '2012:062:15:00:00.000'  # stop time for interval 26
        interval = 'i26'                  # stops before M-mat uplink 5
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 27):                # starts after M-mat uplink 5
        tstart = '2012:062:16:00:00.000'  # start time for interval 27
        tstop  = '2012:150:03:33:00.000'  # stop time for interval 27
        interval = 'i27'                  # stops before Safe Mode 5
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 28):                # starts after Safe Mode 5
        tstart = '2012:152:00:00:00.000'  # start time for interval 28
        tstop  = '2012:215:00:00:00.000'  # stop time for interval 28
        interval = 'i28'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 29):
        tstart = '2012:336:00:00:00.000'  # start time for interval 29
        tstop  = '2013:021:00:00:00.000'  # stop time for interval 29
        interval = 'i29c'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 30):
        tstart = '2012:062:16:00:00.000'  # start time for interval 30
        tstop  = '2012:364:00:00:00.000'  # stop time for interval 30
        interval = 'i30a'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    elif (interval == 99):
        tstart = '2003:207:00:00:00.000'  # start time for interval 99 (all)
        tstop  = '2099:365:23:59:59.999'  # stop time for interval 99 (all)
        interval = 'i99'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])
    else:
        tstart = '2012:338:00:00:00.000'  # start time for interval 00 (custom)
        tstop  = '2012:339:00:00:00.000'  # stop time for interval 00 (custom)
        interval = 'i00'
        Dmat = array([[ 0.0,  0.0,  0.0], # correction to Mmat
                      [ 0.0,  0.0,  0.0],
                      [ 0.0,  0.0,  0.0]])

    return tstart, tstop, interval, Dmat
