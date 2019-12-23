import os

ff = 'C001A006D003P0000T0011.avi'

Cidx = 0
Aidx = 4
Didx = 8

A001 = 'A001' # violence
A002 = 'A002' # fall-down
A003 = 'A003' # panic
A004 = 'A004' # paper
A005 = 'A005' # escape
A006 = 'A006' # normal

action_list = [A002, A004, A006]


def infos(path):
    flist = os.listdir(path)
    flist.sort()


    for action in action_list:
        vlist = []
        for ff in flist:
            if action in ff:
                vlist.append(ff)

        dlist =[]
        for action_video in vlist:
            daction = action_video[Didx:Didx + 4]
            dlist.append(daction)

        dlist = list(set(dlist))
        dlist.sort()
        for daction in dlist:
            dcount = 0
            for action_video in vlist:
                if daction in action_video:
                    dcount += 1
            print(action, daction , dcount)
            # vaction = ff[Aidx:Aidx + 4]



# path = '/home/peter/workspace/code/elev/data'
# infos(path)


