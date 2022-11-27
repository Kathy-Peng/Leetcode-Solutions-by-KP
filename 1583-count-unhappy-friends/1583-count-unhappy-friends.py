class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        hashmap = {}
        for pair in pairs:
            person_one = pair[0]
            person_two = pair[1]
            pref_one = preferences[person_one]
            i = 0
            person_one_preferee = []
            while i < len(pref_one) and pref_one[i] != person_two:
                person_one_preferee.append(pref_one[i])
                i += 1
            hashmap[person_one] = person_one_preferee
            
            pref_two = preferences[person_two]
            i = 0
            person_two_preferee = []
            while i < len(pref_two) and pref_two[i] != person_one:
                person_two_preferee.append(pref_two[i])
                i += 1
            hashmap[person_two] = person_two_preferee
        print(hashmap)
        
        count = 0
        for person, preferee_list in hashmap.items():
            for preferee in preferee_list:
                if person in hashmap[preferee]:
                    count += 1
                    break
        return count
             
                