import math

ab = float(input())
bc = float(input())

cos_val = bc / math.sqrt(ab**2 + bc**2)
angle_rad = math.acos(cos_val)
angle_deg = math.degrees(angle_rad)
print(str(round(angle_deg))+"\u00B0")

'''https://drive.google.com/drive/folders/1wfNTKinBAV6CCxaI5lfSnnRFAYpy0uEl'''
