# getCrossSectionFromGEN

CMSSW_10_6_4 was used to run this.
The purpose of this script is to provide the cross sections for the different signals. You will need to produce GEN files for these signals before being able to use this script.

Follow the steps below to get the cross sections:
1. Edit `batchGENXsec.py` to include the signals whose cross sections you care about. You may want to modify `signals`, `inputfold`, and `filename` in `batchGENXsec.py`.
2. Run `python batchGENXsec.py`. You should be able to see the cross sections printed on the terminal screen, but I usually do `python batchGENXsec.py > out.txt`, so that all the outputs are in `out.txt` instead.
