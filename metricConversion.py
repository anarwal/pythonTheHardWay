inches=80
pounds=180

#converting inches to centimeter
cmResult=inches*2.4

#converting pounds to kilos and round upto two decimal places
kiloResult=round(pounds/2.205,2)

print ("converting %d inches to %r centimeter"%(inches, cmResult))
print ("converting %d poinds to %r kilos"%(inches, kiloResult))