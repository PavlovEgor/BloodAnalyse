import seaborn as sns
import matplotlib.pyplot as plt


max_WBC = []
for j in range(1, 10):
    filename = 'Result00' + str(j)+ '.txt'
    file = open(filename, 'r')

    d = {}
    lines = list(file.readlines())

    for i in range(len(lines)):
        line = lines[i]

        if line == 'WBC\n':
            d['WBC'] = lines[i+1][:-2]

        elif line == 'Rouges :\n':
            d['Rouges'] = lines[i + 1][:-2]

        elif line == 'Plaquettes :\n':
            d['Plaquettes'] = lines[i + 1][:-2]

    def make_massive_from_str(text):
        a = []
        tmp = ''
        for s in text[1:]:
            if s == '{':
                a.append(int(tmp))
                tmp = ''

            else:
                tmp += s

        return a


    # sns.histplot(make_massive_from_str(d['WBC']), label='WBC')
    # sns.histplot(make_massive_from_str(d['Rouges']), label='Rouges')
    # sns.histplot(make_massive_from_str(d['Plaquettes']), label='Plaquettes')

    # plt.plot(range(len(make_massive_from_str(d['WBC']))), make_massive_from_str(d['WBC']), label='WBC')
    # plt.plot(range(len(make_massive_from_str(d['Rouges']))), make_massive_from_str(d['Rouges']), label='Rouges')
    # plt.plot(range(len(make_massive_from_str(d['Plaquettes']))), make_massive_from_str(d['Plaquettes']), label='Plaquettes')

    max_WBC.append(max(make_massive_from_str(d['WBC'])))

plt.plot(range(1, 10), max_WBC)
# plt.ylabel('Value')
# plt.xlabel('Order in massive')
# plt.legend()
plt.show()