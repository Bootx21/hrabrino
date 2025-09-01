ads_list = ['123', '234', '345', '456']
with open('/Users/nickboone/Documents/Coding/PycharmProjects/Hrabrino/homes.txt') as file:
    home_list = []
    for line in file.readlines():
        home_list.append(line.strip("\n"))
for _ in ads_list:
    if _ not in home_list:
        home_list.append(_)
with open('/Users/nickboone/Documents/Coding/PycharmProjects/Hrabrino/homes.txt', 'w') as file:
    for _ in home_list:
        file.write(f'{_}\n')
print(home_list)

