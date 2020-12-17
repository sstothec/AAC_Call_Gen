import random
import os
import sys
import datetime
import time
import hashlib
from gtts import gTTS
from playsound import playsound

version = '0.5a'
current_path = os.path.dirname(__file__)
filename = current_path + '/' + os.path.basename(__file__)
sha256_hash = hashlib.sha256()
with open(filename,"rb") as f:
	for byte_block in iter(lambda: f.read(4096),b""):
		sha256_hash.update(byte_block)
	sha256_hash = sha256_hash.hexdigest()

print("\nVersion:",  version, "\nSHA256:", sha256_hash, "\n")
delayTime = int(input("Enter a time delay between aircraft in seconds >>>"))
print("Aircraft delay time:", delayTime)
ifrDelayTime = int(input("Enter a delay between IFR aircraft in rounds >>>"))
print ("IFR Cooldown:", ifrDelayTime)
information = input("Enter a valid ATIS information >>>")
print ("Information", information, "now current.")
atisChance = int(input("Enter a (1-100) chance for VFR arrivals to have the ATIS >>>"))
print ("Aircraft have a", atisChance, "% chance to have ATIS")

def convertACType(ac_type):
	if ac_type == 'C172' or ac_type == 'C208':
		ac_type = 'Cessna'
	elif ac_type == 'P28A':
		ac_type = 'Cherokee'
	elif ac_type == 'M20P':
		ac_type = 'Mooney'
	elif ac_type == 'PA46':
		ac_type = 'Malibu'
	elif ac_type == 'BE36':
		ac_type = 'Bonanza'
	elif ac_type == 'PA34':
		ac_type = 'Senneca'
	elif ac_type == 'SR22':
		ac_type = 'Sirrus'
	elif ac_type == 'C310' or ac_type == 'C421':
		ac_type = 'Twin Cessna'
	elif ac_type == 'BE58':
		ac_type = 'Baron'
	elif ac_type == 'PA31':
		ac_type = 'Navajo'
	elif ac_type == 'PAY3':
		ac_type = 'Cheyenne'
	elif ac_type == 'PC12':
		ac_type = 'Pilatus'
	elif ac_type == 'AC68':
		ac_type = 'Commander'
	elif ac_type == 'BE20':
		ac_type = 'King Air'
	elif ac_type == 'BE40':
		ac_type = 'Beechjet'
	elif ac_type == 'FA20':
		ac_type = 'Falcon'
	elif ac_type == 'CL60':
		ac_type = 'Challenger'
	elif ac_type == 'C550':
		ac_type = 'Citation'
	elif ac_type == 'GLF3':
		ac_type = 'Gulfstream'
	elif ac_type == 'LJ35':
		ac_type = 'Lear'
	return ac_type

def convertPhonetic(string):
	for k, v in phonetics.items():
		string = string.replace(k, v)
	return string

if __name__ == '__main__':
	sys.stdout.write("\n{}\n".format(datetime.datetime.now().time()))
	sys.stdout.write("Academy Airport Online\n\n")
	ifr_reporting = 'Woody'
	inbound_list = ['McDonalds Bridge', 'Riverside', 'Sand Springs', 'Owasso', 'Chandler']
	ga_ac_list = ['C172', 'P28A', 'M20P', 'C208', 'PA46', 'BE36', 'PA34', 'SR22', 'C310', 'BE58', 'PA31', 'PAY3', 'PC12', 'C421', 'AC68', 'BE20', 'BE40', 'FA20', 'CL60', 'C550', 'GLF3', 'LJ35']
	carrier_ac_list = ['A300', 'A320', 'A340', 'B727', 'B737', 'B747', 'B757', 'B767', 'B777', 'CRJ', 'DH8', 'MD11', 'MD81']
	C172_list = ['1204W', '172PT', '3455Y', '8689X', '690DA', '360LT', '535KS']
	AC68_list = ['466PF', '6080Y', '55BF', '242WB', '227GK', '58DZ', '416BR']
	BE20_list = ['4132B', '4351V', '617DL', '623SC', '858EF', '887JG', '20WK']
	BE36_list = ['11452', '427VV', '63RG', '622FG', '30450', '524AC', '801DF', '118BZ', '425ER', '342AB', '36BE', '288AT', '111WT', '515DF']
	BE40_list = ['40FD', '40MY', '801MB', '911RS', '411CS', '40CS', '68MY']
	BE58_list = ['407LY', '42WK', '429W', '56CD', '89TP', '8729B', '71GL']
	C208_list = ['208LT', 'MTN411', 'MTN401', 'IRO525', 'IRO515', '7123A', '373BD']
	C310_list = ['1388V', '310MN', '310DS', '313SN', '366QB', '507FS', '411CA']
	C421_list = ['10SU', '605JF', '421BC', '237RU', '455QT', '422LK', '503LJ']
	C550_list = ['10JR', '431L', '332VS', '635PN', '118KT', '911BT', '127BZ']
	CL60_list = ['1258E', '935TT', '39GC', '6585J', '112BS', '818CS', '858WT']
	FA20_list = ['735SH', '521SH', '25AB', '37AS', '46NT', '809BZ', '18NC']
	GLF3_list = ['19CH', '753WS', '322BC', '44LK', '125HD', '923FP', '5843A']
	LJ35_list = ['102KM', '123JL', '1HD', '455PV', '921RW', '8892G', '123DG']
	M20P_list = ['20PA', '123NR', '52124', '7634P', '2063W', '444TT', '610RW']
	P28A_list = ['288DS', '6206F', '355PL', '2991F', '288PM', '7643K', '371CK']
	PA31_list = ['630LT', '609MA', '85JR', '542AC', '43TP', '122CB', '576TP']
	PA34_list = ['9726Z', '911KT', '676PS', '157CF', '4359Y', '6297C', '328DG']
	PA46_list = ['577GL', '422TP', '381RG', '283RW', '771CB', '46PA', '634CL']
	PAY3_list = ['115SA', '230AX', '39AC', '921FA', '915MP', '51MF', '456AA', '783BT']
	PC12_list = ['12PC', '334LE', '772RP', '582TT', '246ML', '480BE', '647WW']
	SR22_list = ['22SR', '486CC', '371RT', '504SC', '181PP', '204DS', '615DL']
	A300_list = ['American 12 28 Heavy', 'American 6 23 Heavy', 'American 11 19 Heavy', 'American 3 Zero 2 Heavy', 'U P S 6 23 Heavy', 'U P S 13 42 Heavy']
	A320_list = ['Air Canada 5 25', 'Air Canada 7 51', 'Air Canada 2 99', 'Air Canada 3 22', 'Air Canada 3 24', 'Air Canada 1 27', 'Air Canada 3 15', 'Air Canada 1 17']
	A340_list = ['Air France 8 23 Heavy', 'Air France 1 13 Heavy', 'Air France 1 08 Heavy', 'Air France 4 11 Heavy', 'Air France 4 26 Heavy', 'Air France 3 19 Heavy', 'Air France 5 27 Heavy']
	B727_list = ['Fed X 62', 'Fed X 72', 'Fed X 82', 'Fed X 2 94']
	B737_list = ['Southwest 9 23', 'Southwest 8 58', 'Southwest 4 16', 'Southwest 19 85', 'Alaska 7 31', 'Alaska 3 47', 'Alaska 5 17', 'Delta 1 17', 'Delta 1 16', 'Delta 7 33', 'Delta 9 37', 'Alaska 1 22', 'Alaska 12 28']
	B747_list = ['United 4 92 Heavy', 'United 5 91 Heavy', 'United 12 87 Heavy', 'United 15 64 Heavy', 'K L M 6 23 Heavy', 'K L M 1 13 Heavy', 'K L M 7 91 Heavy', 'K L M 13 42 Heavy']
	B757_list = ['American 2 11', 'American 7 57', 'Delta 7 85', 'Delta 4 61', 'Delta 13 35', 'Delta 10 86', 'U P S 10 57', 'U P S 10 77', 'U P S 10 97', 'American 3 88', 'American 8 89']
	B767_list = ['United 8 zero 2 Heavy', 'United 23 Heavy', 'American 21 56 Heavy', 'American 10 Heavy', 'American 4 81 Heavy', 'American 7 63 Heavy', 'American 62 Heavy', 'American 6 42 Heavy', 'American 5 19 Heavy', 'United 5 14 Heavy', 'United 7 79 Heavy', 'United 11 72 Heavy', 'United 67 Heavy']
	B777_list = ['United 6 77 Heavy', 'United 4 33 Heavy', 'United 8 27 Heavy', 'United 1 17 Heavy', 'United 5 64 Heavy', 'United 12 55 Heavy', 'United 7 72 Heavy']
	CRJ_list = ['Jet Link 23 54', 'Jet Link 11 19', 'Sky West 10  zero 8', 'Envoy 11 24', 'Envoy 17 80', 'Envoy 22 50', 'Jet Link 12 42', 'Sky West 16 32',' Sky West 12 28']
	DH8_list = ['Piedmont 33 34', 'Piedmont 32 24', 'Alaska 11 22', 'Brickyard 11 zero 2', 'Piedmont 23 23', 'Piedmont 22 22', 'Brickyard 32 24']
	MD11_list = ['Fed X 9 42 Heavy', 'Fed X 22 85 Heavy', 'Fed X 19 63 Heavy', 'Fed X 1 67 Heavy']
	MD81_list = ['American 1 80', 'American 3 91', 'Delta 8 zero 2', 'Delta 1 43', 'Delta 7 98', 'Delta 13 31', 'American 5 85', 'American 7 39']

	phonetics = {
		'A': 'Alpha',
		'B': 'Bravo',
		'C': 'Charlie',
		'D': 'Delta',
		'E': 'Echo',
		'F': 'Foxtrot',
		'G': 'Golf',
		'H': 'Hotel',
		'I': 'India',
		'J': 'Juliet',
		'K': 'Kilo',
		'L': 'Lima',
		'M': 'Mike',
		'N': 'No vember',
		'O': 'Oscar',
		'P': 'Papa',
		'Q': 'Quebec',
		'R': 'Romeo',
		'S': 'Sierra',
		'T': 'Tango',
		'U': 'Uniform',
		'V': 'Victor',
		'W': 'Whisky',
		'X': 'XRay',
		'Y': 'Yankee',
		'Z': 'Zulu',
		'9': 'Niner',
		'0': 'Zero'
	}

	ifr_delay = True
	ifr_countdown = 0
	have_atis = True
	intentions_rng = -1
	while True:
		full_stop = False
		tg1_fs = False
		tg1_dep = False
		tg2_fs = False
		tg2_dep = False
		sg1_fs = False
		sg1_dep = False
		if ifr_countdown == 0:
			ifr_delay = False
		if ifr_delay == True:
			ifr_countdown -= 1
		vfr_rng = random.randint(1,100)
		if ifr_countdown != 0 or vfr_rng <= 75:
			is_vfr = True
		else:
			is_vfr = False
			ifr_countdown += ifrDelayTime
			ifr_delay = True
		request = 'none'
		if is_vfr == True:
			ac_type = random.choice(ga_ac_list)
			atis_rng = random.randint(1, 100)
			if atis_rng <=atisChance:
				have_atis = True
			else:
				have_atis = False
			compass_rng = random.randint(1,100)
			direction = 'west'
			if compass_rng <= 25:
				direction = 'north'
			elif compass_rng <= 50:
				direction = 'east'
			elif compass_rng <= 75:
				direction = 'south'
			elif compass_rng <= 100:
				direction = 'west'
			intentions_rng = random.randint(1,100)
			if intentions_rng <= 82:
				full_stop = True
			elif intentions_rng > 82 and intentions_rng <= 92:
				tg1_fs = True
				request = '1 touch and go and full stop'
			elif intentions_rng > 92 and intentions_rng <= 96:
				tg1_dep = True
				request = '1 touch and go and departure' + direction + 'bound'
			elif intentions_rng == 97:
				tg2_fs = True
				request = '2 touch and go and full stop'
			elif intentions_rng == 98:
				tg2_dep = True
				request = '2 touch and go and departure' + direction + 'bound'
			elif intentions_rng == 99:
				sg1_fs = True
				request = '1 stop and go and full stop'
			elif intentions_rng == 100:
				sg1_dep = True
				request = '1 stop and go and departure' + direction + 'bound'
		elif is_vfr == False:
			ac_type = random.choice(carrier_ac_list)
			inbound_location = ifr_reporting
			full_stop = True
		ga_ifr = False
		become_ifr_rng = 0
		if ifr_delay == False:
			become_ifr_rng = random.randint(1,100)
		if become_ifr_rng >= 90:
			is_vfr = False
			ifr_countdown += ifrDelayTime
			ifr_delay = True
			ga_ifr = True
			inbound_location = ifr_reporting
		print('is_vfr:', is_vfr)
		print('ifr_countdown:', ifr_countdown)
		text_ac_type = convertACType(ac_type)
		print('ac_type:', ac_type)
		ac_list = ac_type + '_list'
		ac_callsign = random.choice(eval(ac_list))
		if ac_callsign == 'IRO515' or ac_callsign == 'IRO525':
			text_ac_type = 'Iron Air'
			ac_callsign = ac_callsign.replace('IRO', '')
		if ac_callsign == 'MTN401' or ac_callsign == 'MTN411':
			text_ac_type = 'Mountain'
			ac_callsign = ac_callsign.replace('MTN', '')
		print('ac_callsign:', ac_callsign)
		if is_vfr == True:
			text_ac_callsign = " ".join(ac_callsign)
			text_ac_callsign = convertPhonetic(text_ac_callsign)
			inbound_location = random.choice(inbound_list)
			if have_atis == True:
				if full_stop == True:
					text = "Academy tower, " + text_ac_type + text_ac_callsign + " inbound over " + inbound_location + " with information " + information
				elif full_stop == False:
					text = "Academy tower, " + text_ac_type + text_ac_callsign + " inbound over " + inbound_location + " with information " + information + " request " + request
			elif have_atis == False:
				if full_stop == True:
					text = "Academy tower, " + text_ac_type + text_ac_callsign + " inbound over " + inbound_location
				if full_stop == False:
					text = "Academy tower, " + text_ac_type + text_ac_callsign + " inbound over " + inbound_location + " request " + request
			print('have_atis:', have_atis)
			print('full_stop:', full_stop)
		print('inbound_location:', inbound_location)
		if is_vfr == False:
			if ga_ifr == True:
				text_ac_callsign = " ".join(ac_callsign)
				for k, v in phonetics.items():
					text_ac_callsign = text_ac_callsign.replace(k, v)
				text = "Academy tower, " + text_ac_type + text_ac_callsign + " is over Woody"
			elif ga_ifr == False:
				text_ac_callsign = ac_callsign
				text = "Academy tower, " + text_ac_callsign + " is over Woody"
		tts = gTTS(text)
		file1 = str(ac_type + '_' + ac_callsign + '_' + inbound_location + '.mp3')
		tts.save(file1)
		playsound(file1,True)
		os.remove(file1)
		time.sleep(delayTime)