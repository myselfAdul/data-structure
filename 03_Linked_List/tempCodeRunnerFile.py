def findGroups(money_list, fare):
    money_dict = {}
    ungrouped = []
    group_num = 1

    for i, money in enumerate(money_list):
        if fare - money in money_dict:
            print(f"Group {group_num} : {fare - money}, {money}")
            group_num += 1
            del money_dict[fare - money]
        else:
            
            money_dict[money] = i

  
    ungrouped = list(money_dict.keys())

   
    if ungrouped:
        print("Ungrouped :", " ".join(map(str, ungrouped)))


# Sample Inputs and Outputs
findGroups([120, 100, 150, 50, 30], 150)
print()  
findGroups([60, 150, 60, 30, 120, 30], 180)
findGroups ( [30, 150, 150], 180 )