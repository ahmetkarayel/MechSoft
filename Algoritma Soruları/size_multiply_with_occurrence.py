'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''

from itertools import combinations

t = "acldm1labcdhsnd"
z = "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"

def find_max(t,z):
   
    # Olası tüm substringler kombinasyonlarını tutuyorum.
    all_combinations = set([''.join(t[i:j]) for i in range(len(t)) for j in range(i+1, len(t)+1)])
    #all_combinations = set([t[x:y] for x, y in combinations(range(len(t) + 1), r = 2)])
    
    # Her kombinasyon için "uzunluk * frekans" skorlarını tutuyorum.
    all_scores = [z.count(i)*len(i) for i in all_combinations]
    my_dict = dict(zip(all_combinations, all_scores))

    max_combination = max(my_dict, key=my_dict.get) # Maximum skora sahip "substring"
    
    return max_combination, z.count(max_combination), max(my_dict.values())


if __name__ == '__main__':
    max_combination, count, final_score = find_max(t,z)
    print(f"'{max_combination}' is a substring of '{t}', and it occurs {count} times in '{z}', len({max_combination}) x {count} = {final_score} is the solution")