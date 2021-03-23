import demographics


yr_ammount = int(input("How many people are we recording? "))
year_list = []

for itm in range(yr_ammount):
    ammount = input("what year was person {} born? ".format(itm+1))
    ammount_int = int(ammount)
    year_list.append(ammount_int)

# print("The list is: "+ str(year_list))

print("\nAll people entered:")
list_of_tuples = demographics.get_year_tuples(year_list)
print(demographics.get_table(list_of_tuples))
# print(listtt)
print("Oldest\t\t :  {}\n"
      "Youngest\t :  {}\n"
      "Average Year :  {}".format(demographics.get_oldest(list_of_tuples),
                                  demographics.get_newest(list_of_tuples),
                                  demographics.get_average(list_of_tuples)))

