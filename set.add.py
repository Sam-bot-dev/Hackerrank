# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
i=1
country = list()
while(i<=n):
    name=input()
    country.append(name)
    i= i+1
country = set(country)
print(len(country))
# sample input
'''7
UK
China
USA
France
New Zealand
UK
France '''

# sample output 5