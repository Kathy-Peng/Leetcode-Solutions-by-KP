class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        results = []
        maps = {}
        added = set()
        for idx in range(len(transactions)):
            item = transactions[idx]
            item_list = item.split(',')
            #if transaction amount exceeds 1000 we add this to the results set
            if int(item_list[2])>1000:
                results.append(item)
                added.add(idx)
            name = item_list[0]
            time = int(item_list[1])
            place = item_list[3]
            if name not in maps:
                maps[name]=[[time, place, idx]]
            else:
                ori_list = maps[name]
                ori_list.append([time, place, idx])
                maps[name]=ori_list
                
        for name, contents in maps.items():
            contents.sort()
            print(name, contents)
            l = 0
            while l < len(contents):
                tmp = l
                while l<len(contents) and int(contents[l][0])<=int(contents[tmp][0])+60:
                    #if city names are different
                    if contents[l][1]!=contents[tmp][1]:
                        if contents[l][2] not in added:
                            results.append(transactions[contents[l][2]])
                            added.add(contents[l][2])
                        if contents[tmp][2] not in added:
                            results.append(transactions[contents[tmp][2]])
                            added.add(contents[tmp][2])
                    l += 1
                l = tmp + 1
        return results