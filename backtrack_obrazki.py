import random
import queue
import copy

kol = []
wier = []
n = 0
m = 0

with open('zad_input.txt', 'r') as f:

	line1 = f.readline().split()
	if len(line1) == 2:
		n, m = map(int, line1)
		
	for i in range(n):
		line = f.readline()
		wier.append([int(x) for x in line.split()])

	for i in range(m):
		line = f.readline()
		kol.append([int(x) for x in line.split()])
		

tab = [[0 for i in range(m)] for j in range(n)]

def possible(D, napis, dl):
	
	ile1 = [0]
	ilem1 = [0]

	for i in range(1, dl+1):

		ile1.append(ile1[i-1])
		ilem1.append(ilem1[i-1])
		if napis[i-1] == 1:
			ile1[i] += 1 
		if napis[i-1] == -1:
			ilem1[i] += 1

	#print(ile1, '\n', ilem1)

	if not D or D == [0]:
		return (ile1[dl] == 0)
		
	pop = []
	for i in range(1, dl + 1):

		if i < D[0]:
			continue
			
		pm1 = ilem1[i] - ilem1[i - D[0]]

		if pm1 == 0 and ile1[i - D[0]] == 0:
			pop.append(i)

	#print(napis)
	#print(pop)

	for j in range (1, len(D)):
		ob = []
		blok = D[j]
		for i in range (1, dl + 1):
			
			for k in pop:
				if k >= i - blok:
					break
				pm1 = ilem1[i] - ilem1[i - blok]
				p1 = ile1[i - blok - 1] - ile1[k]
				if (ilem1[i] - ilem1[i - blok] == 0) and (napis[i - blok - 1] != 1):
					if pm1 == 0 and p1 == 0:
						ob.append(i)
						break
		#print(ob)	
		if not ob:
			return False
		pop = ob
		
	for i in pop:
		if ile1[dl] - ile1[i] == 0:
			return True
			 
	return False
	
	
def elimination(nr, kolumna, count0):

	to_analize = []

	D = kol[nr] if kolumna else wier[nr]
	dl = n if kolumna else m
	
	if not kolumna:	
		napis = tab[nr][:]
	else: 
		napis = [tab[i][nr] for i in range(dl)]
	
	for i in range (dl):
		if napis[i] == 0:
			napis[i] = 1
			i1 = possible(D, napis, dl)
			napis[i] = -1 
			i2 = possible(D, napis, dl)
			if i1 and not i2:
				count0 -= 1
				napis[i] = 1
				to_analize.append(i)
			elif not i1 and i2:
				count0 -= 1
				napis[i] = -1
				to_analize.append(i)
			elif not i1 and not i2:
				return (count0, [-1])
			else: 
				napis[i] = 0
				
	if 0 not in napis:
		if not possible(D, napis, dl):
			return (count0, [-1])
				
	if not kolumna:	
		tab[nr] = napis
	else: 
		for i in range(dl):
			tab[i][nr] = napis[i]
	
	return (count0, to_analize)
	

def deduction(to_check, count0):

	q = queue.Queue()

	for i in to_check:
		q.put(i)

	in_q = set(list(q.queue))

	while not q.empty():
		top = q.get()
		in_q.remove(top)

		if_kol = (top % 2 == 1)
		nr = top // 2

		(count0, to_analize) = elimination(nr, if_kol, count0)
		if to_analize and to_analize[0] == -1:
			return (False, count0)

		for i in to_analize:
			sasiad = 2 * i + (0 if if_kol else 1)
			
			if sasiad not in in_q:
				q.put(sasiad)
				in_q.add(sasiad)
	return (True, count0)


def backtrack(count0, check):
	
	global tab
	(p, count0) = deduction(check, count0)	
	
	if p == True and count0 == 0:
		return True
	if p == False:
		return False
	
	for i in range(n):
		for j in range(m):
		    if tab[i][j] == 0:
		        lab = copy.deepcopy(tab)
		        tab[i][j] = 1
		        check = [2 * i, 2 * j + 1]
		        if backtrack(count0 - 1, check): 
		            return True
		        tab = copy.deepcopy(lab)
		        tab[i][j] = -1
		        if backtrack(count0 - 1, check): 
		            return True
		        tab = copy.deepcopy(lab)
		        return False

	return True
		
def start():

	count0 = n * m
	
	check = []
	
	for i in range(n): 
		check.append(2 * i)      # Wiersze 
	for i in range(m): 
		check.append(2 * i + 1)  # Kolumny 
	
	
	backtrack(count0, check)
		
		
	
	with open('zad_output.txt', 'w') as f_out:
		for i in range(n):
			row_str = ""
			for j in range(m):
				if tab[i][j] == -1:
					row_str += "."
				else:
					row_str += "#"
			f_out.write(row_str + "\n")
	

start()



