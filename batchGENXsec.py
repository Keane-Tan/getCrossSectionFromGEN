import os
import sys

signals = [
["3000","20","0.3","peak"],
# ["2000","20","0.3","peak"],
# ["4000","20","0.3","peak"],
# ["3000","100","0.3","peak"],
# ["3000","1","0.3","peak"],
# ["3000","50","0.3","peak"],
# ["3000","20","0.5","peak"],
# ["3000","20","0.7","peak"],
# ["3000","20","0.1","peak"],
# ["3000","20","0.3","high"],
# ["3000","20","0.3","low"],
# ["400","20","0.3","peak"],
# ["500","20","0.3","peak"],
# ["600","20","0.3","peak"],
# ["800","20","0.3","peak"],
# ["1000","20","0.3","peak"],
# ["1500","20","0.3","peak"],
# ["6000","20","0.3","peak"],
# ["200","20","0.3","peak"],
# ["800","20","0.5","peak"],
# ["800","20","0.7","peak"],
# ["800","20","0.1","peak"],
]

for sig in signals:
    mMed = sig[0]
    mDark = sig[1]
    rinv = sig[2]
    alpha = sig[3]

    allFiles = ""

    for part in range(1,101):
        # if mMed == "400" and part == 72:
        #     continue
        # if mMed == "600" and part == 74:
        #     continue
        # if mMed == "800" and part == 15:
        #     continue
        # if mMed == "1000" and part == 96:
        #     continue

        inputfold = 'root://cmseos.fnal.gov//store/user/lpcdarkqcd/tchannel/Full/GEN/'
        # inputfold = 'root://cmseos.fnal.gov//store/user/keanet/tchannel/SVJP_08272020/GEN/'
        filename = inputfold + 'step1_LHE-GEN_t-channel_mMed-{}_mDark-{}_rinv-{}_alpha-{}_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000_part-{}.root'.format(mMed,mDark,rinv,alpha,part)

        if part == 100:
            allFiles += filename
        else:
            allFiles += filename + ","

    command = 'cmsRun ana.py inputFiles=\"' + allFiles + '\" maxEvents=-1 > GENXsec/{}_{}_{}_{}_p{}.txt'.format(mMed,mDark,rinv,alpha,part)
    os.system(command)
