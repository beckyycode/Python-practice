from lib import sequence_scanner, mRNAtranscription
from script_5_basepaircomparison_practice_lacZ import lacopcombined

# print (lacopcombined)

lacopRNA = mRNAtranscription (lacopcombined)
sequence_scanner (lacopRNA, "Agga")
