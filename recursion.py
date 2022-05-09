def fibonnaci(n):
	if n == 0 or n == 1:
		return(n)
	return(fibonnaci(n - 1) + fibonnaci(n - 2))

def gcd(m, n):
	if m < n:
		(m, n) = (n, m)
	if (m % n) == 0:
		return(n)
	else:
		return(gcd(n, m % n))

def compareTo(s1, s2):
	if len(s1) > len(s2):
		return 1
	elif len(s1) < len(s2):
		return -1
	elif len(s1) == len(s2):
		if len(s1) == 1 and len(s2) == 1:
			return(ord(s1) - ord(s2))

	return(compareTo(s1[0], s2[0]) - compareTo(s1[1:], s2[1:]))

def main():
	print("Fibonnaci of place 6: ", fibonnaci(6))
	print("GCD of 100 and 25: ", gcd(100, 25))
	print("String comparison of hello and hello: ", compareTo('hello', 'hello'))
	print("String comparison of hello and hellq: ", compareTo('hello', 'hellq'))
	print("String comparison of hello and hella: ", compareTo('hello', 'hella'))

if __name__ == '__main__':
	main()