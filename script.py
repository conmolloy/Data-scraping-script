import urllib2
import itertools
import re

print('Downloading...')
response = urllib2.urlopen('http://www.clal.it/en/?section=world_map_consegne_latte')
html = response.read()

#This is where we use regular expressions to get the data
print('Download finnished, running script')
Arg_data = re.findall(r'<td class="data0"><b><a target="blank"  href="index\.php\?section=consegne_argentina">ARGENTINA<\/a><\/td>\n\t\t<td class="value0" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value0" style="text-align:right">(.*?)<\/td>', str(html)) 
Aus_data = re.findall(r'<td class="data1"><b><a target="blank"  href="index\.php\?section=consegne_australia">AUSTRALIA<\/a><\/td>\n\t\t<td class="value1" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value1" style="text-align:right">(.*?)<\/td>', str(html))
Bel_data = re.findall(r'<td class="data0"><b><a target="blank"  href="index\.php\?section=consegne_bielorussia">BELARUS<\/a><\/td>\n\t\t<td class="value0" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value0" style="text-align:right">(.*?)<\/td>', str(html))
Chili_data = re.findall(r'<td class="data1"><b><a target="blank"  href="index\.php\?section=consegne_cile">CHILE<\/a><\/td>\n\t\t<td class="value1" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value1" style="text-align:right">(.*?)<\/td>', str(html))
Nz_data = re.findall(r'<td class="data0"><b><a target="blank"  href="index\.php\?section=consegne_new_zealand">NEW ZEALAND<\/a><\/td>\n\t\t<td class="value0" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value0" style="text-align:right">(.*?)<\/td>', str(html))
Tur_data = re.findall(r'<td class="data1"><b><a target="blank"  href="index\.php\?section=consegne_turchia">TURKEY<\/a><\/td>\n\t\t<td class="value1" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value1" style="text-align:right">(.*?)<\/td>', str(html))
Ukr_data = re.findall(r'<td class="data0"><b><a target="blank"  href="index\.php\?section=consegne_ucraina">UKRAINE<\/a><\/td>\n\t\t<td class="value0" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value0" style="text-align:right">(.*?)<\/td>', str(html))
EU_data = re.findall(r'<td class="data1"><a target="blank"  href="index\.php\?section=consegne">EU-28<\/a><\/td>\n\t\t\t\t<td class="value1" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t\t\t<td class="value1" style="text-align:right">(.*?)<\/td>', str(html))
USA_data = re.findall(r'<td class="data0"><b><a target="blank"  href="index\.php\?section=produzioni_usa_latte_bovino">USA<\/a><\/td>\n\t\t<td class="value0" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value0" style="text-align:right">(.*?)<\/td>', str(html))
Urg_data = re.findall(r'<td class="data1"><b><a target="blank"  href="index\.php\?section=consegne_uruguay">URUGUAY<\/a><\/td>\n\t\t<td class="value1" style="font-style:italic;text-align:center">(.*?)<\/td>\n\t\t<td class="value1" style="text-align:right">(.*?)<\/td>', str(html))



#Below is where we clean the data of all potential brackets or other html tags that might appear in the text
insert_list = ['Country,Month range,Milk production']
#Argentina
Argen = str(Arg_data[0]).split(',')
Argen = [item.replace("'", '') for item in Argen]
Argen = [item.replace("(", '') for item in Argen]
Argen = [item.replace(")", '') for item in Argen]
Argen = [item.replace("<small>e</small>", '') for item in Argen]
insert_list.append('Argentina,' +Argen[0]+','+Argen[1])
#Austrailia
AUS = str(Aus_data[0]).split(',')
AUS = [item.replace("'", '') for item in AUS]
AUS = [item.replace("(", '') for item in AUS]
AUS = [item.replace(")", '') for item in AUS]
AUS = [item.replace("<small>e</small>", '') for item in AUS]
insert_list.append('Australia,'+AUS[0]+','+AUS[1])
#Balarus
Bel = str(Bel_data[0]).split(',')
Bel = [item.replace("'", '') for item in Bel]
Bel = [item.replace("(", '') for item in Bel]
Bel = [item.replace(")", '') for item in Bel]
Bel = [item.replace("<small>e</small>", '') for item in Bel]
insert_list.append('Belarus,'+Bel[0]+','+Bel[1])
#Chile
Chli = str(Chili_data[0]).split(',')
Chli = [item.replace("'", '') for item in Chli]
Chli = [item.replace("(", '') for item in Chli]
Chli = [item.replace(")", '') for item in Chli]
Chli = [item.replace("<small>e</small>", '') for item in Chli]
insert_list.append('Chlie,'+Chli[0]+','+Chli[1])
#New Zealand
NZ = str(Nz_data[0]).split(',')
NZ = [item.replace("'", '') for item in NZ]
NZ = [item.replace("(", '') for item in NZ]
NZ = [item.replace(")", '') for item in NZ]
NZ = [item.replace("<small>e</small>", '') for item in NZ]
insert_list.append('New Zealand,' + NZ[0]+',' + NZ[1])
#Turkey
Tur = str(Tur_data[0]).split(',')
Tur = [item.replace("'", '') for item in Tur]
Tur = [item.replace("(", '') for item in Tur]
Tur = [item.replace(")", '') for item in Tur]
Tur = [item.replace("<small>e</small>", '') for item in Tur]
insert_list.append('Turkey,'+Tur[0]+','+Tur[1])
#Ukraine
Ukr = str(Ukr_data[0]).split(',')
Ukr = [item.replace("'", '') for item in Ukr]
Ukr = [item.replace("(", '') for item in Ukr]
Ukr = [item.replace(")", '') for item in Ukr]
Ukr = [item.replace("<small>e</small>", '') for item in Ukr]
insert_list.append('Ukraine,'+Ukr[0]+','+Ukr[1])
#Eu-28
EU = str(EU_data[0]).split(',')
EU = [item.replace("'", '') for item in EU]
EU = [item.replace("(", '') for item in EU]
EU = [item.replace(")", '') for item in EU]
EU = [item.replace("<small>e</small>", '') for item in EU]
insert_list.append('EU-28,'+EU[0]+','+EU[1])
#USA
USA = str(USA_data[0]).split(',')
USA = [item.replace("'", '') for item in USA]
USA = [item.replace(")", '') for item in USA]
USA = [item.replace("(", '') for item in USA]
USA = [item.replace("<small>e</small>", '') for item in USA]
insert_list.append('USA,'+USA[0]+','+USA[1])
#Uruguay
Urg = str(Urg_data[0]).split(',')
Urg = [item.replace("'", '') for item in Urg]
Urg = [item.replace(")", '') for item in Urg]
Urg = [item.replace("(", '') for item in Urg]
Urg = [item.replace("<small>e</small>", '') for item in Urg]
insert_list.append('Uruguay,'+Urg[0]+','+Urg[1])


#outputting the file
print("Writing data to file")
for line in insert_list:
    with open("../DataExtract3.csv", "a") as outputFile:
        outputFile.write(line + '\n')


print("Finnished!")






    
 
