# Указываем ниже данные из таблицы расчета трудозатрат (минимальное и максимальное время)
data = [
    {'t_min': 1,'t_max': 3},
    {'t_min': 1,'t_max': 3},
    {'t_min': 2,'t_max': 6},
    {'t_min': 4,'t_max': 12},
    {'t_min': 8,'t_max': 24},
    {'t_min': 8,'t_max': 24},
    {'t_min': 4,'t_max': 12},
    {'t_min': 60,'t_max': 100},
    {'t_min': 16,'t_max': 32},
    {'t_min': 4,'t_max': 12},
    {'t_min': 8,'t_max': 24},
    {'t_min': 4,'t_max': 12},
    {'t_min': 4,'t_max': 12},
]

# Эффективный фонд времени 1973 часов:12 = 164часа
t = 164
s_min = []
s_max = []
s = []
ss = []

for i in data:
    q = (i['t_min'] + i['t_max'])/2
    tog = q/8
    print(i['t_min'],'-', i['t_max'],'-', q,'-', tog)
    s.append(q)
    ss.append(tog)
    s_min.append(i['t_min'])
    s_max.append(i['t_max'])

s_min = sum(s_min)
s_max = sum(s_max)
s = round(sum(s),2)
ss = round(sum(ss),2)

print('\n', s_min,'-', s_max,'-', s,'-', ss)

# Зарплата техника-программиста
zp = 35000
zzosn = round(zp/t*s, 2)
print('Зз осн =',  zzosn)

zzdop = round(zzosn*0.10, 2)
print('Зз доп =', zzdop)

zzpl = round(zzosn+zzdop, 2)
print('Зз/пл =', zzpl)

print('\nРасчет суммы страховых взносов')
list1 = [0.22, 0.051, 0.029, 0.002]
strvzn = []
for count, i in enumerate(list1):
    a = round(zzpl*i,2)
    print(count+1,'=',a)
    strvzn.append(a)
strvzn = round(sum(strvzn),2)
print('Всего =', strvzn)

# Стомость средств вычислительной техники
F_balance = 100000

# Ликвидационная стоимость ( стоимость по которой вы сможете продать
# вычислительную технику после окончания срока экплуатации
# напимер 5000 рублей
F_likv = 40000


apr = round((F_balance-F_likv)/36*s/t, 2)
print('\nАпр =', apr)

# Суммарная мощность вКт потребляемая техническими средствами 0.7 = 700 Вт
kVT = 0.7

# стоимость 1 кВт/час
cost_kVT = 8.05

zel = round(kVT*s*cost_kVT,2)
print('Зэл =', zel)

kisp = 0
print('Кисп =', kisp)

ksvt = apr + zel
print('Ксвт =', ksvt)

mv = round(ksvt/s,2)
print('Мв =', mv)

# указаываем в квадратных скобках через запятую стоимость
# материалов и покупных изделий
stm = sum([900, 700])
stm_10percent = round(stm*0.1,2)
all_stm = stm + stm_10percent
print('\nСтоимость материалов и покупных изделий =', stm)
print('Транспортные расходы (10% от стоимости материалов) =', stm_10percent)
print('Всего =', all_stm)

kpr = zzpl + strvzn + kisp + ksvt + all_stm
print('\nКпр =', kpr)

# Если необходимо, стоимость средств приобретенных технических средств управления
kts = 0
print('Ктс =', kts)

# Стоимость интернета в месяц
enternet = 400
kls = round(enternet/t*s, 2)
print('Клс =', kls)

# Стоимость программных средств (например оплата хостинга и домен) (посчитать самому и вписать)
kpo = 2770
print('Кпо =', kpo)

# Затраты на формирование информационной базы (возможно 0)
kio = 0
print('Кио =', kio)

# Затраты на обучение персонала (возможно 0)
kob = 0
print('Коб =', kob)

# Затраты на опытную эксплуатацию (возможно 0)
koe = 0
print('Коэ =', koe)

print('\nСумма капитальных затрат при разработке чат-бота')
print('Затраты на заработную плату проектировщиков с начислениями', round(zzpl+strvzn,2))
de1 = round(zzpl+strvzn,2) + kisp + ksvt + all_stm + kts + kls + kpo + kio + kob + koe
print('Всего DE1: ', de1)

# Сотрудник будет уделять сайту в среднем час в неделю, то есть около 10 минут рабочего
# времени в день, 10 минут заменяем на свое значение.
minutes_for_control_in_day = 10

zp_in_hour = round(zp/t, 2)
szp = round(zp_in_hour*(minutes_for_control_in_day / 60)*20.55*12, 2)
print('\nСзп =', szp)

sao = round((F_balance-F_likv)/3,2)
print('Сао =', sao)

# Затраты на техническое обслуживание (Сто) примем равными 600 руб. в месяц.
sto_month = 600
sto_year = sto_month*12
print('Сто =', sto_year)

sepc = round(kVT * t * cost_kVT * 12 * 1.1, 2)
print('Сэ пк =', sepc)

sls = round(enternet*12 + kpo,2)
print('Слс =', sls)

# Затраты на Яндекс Директ (посчитать самому и вписать)
yandex = 0
print('Сяд =', yandex)

sproch = round((szp+sao+sto_year+sepc+sls+yandex)*0.03,2)
print('Спроч =', sproch)
c = round(szp+sao+sto_year+sepc+sls+yandex+sproch,2)
print('Общая сумма эксплуатационных затрат будет равна =', c)

# Количество лет эксплуатации (обычно 2-3 года)
years = 3

print('Расчет эксплуатационных затрат до 2024 года = ', c*years)

de2 = szp*years
print('DE2 =', de2)

de3 = sto_year*years
print('DE3 =', de3)

de4 = 0
print('DE4 =', de4)

de5 = 0
print('DE5 =', de5)

de6 = 0
print('DE6 =', de6)

de7 = sls * years
print('DE7 =', de7)

de8 = round((de1 + de2 + de3 + de4 + de5 + de6 + de7) * 0.03,2)
print('DE8 =', de8)

de = de1 + de2 + de3 + de4 + de5 + de6 + de7 + de8
print('DE =', de)

ic = round(zp_in_hour * 12 * years, 2)
print('IC =', ic)

tco = round(de + ic, 2)
print('Тсо =', tco)