import time
import matplotlib.pyplot as plt


#산성 / 염화수소, 황산, 질산
HCl = None
H2SO4 = None
HNO3 = None

#염기성 / 수산화나트륨, 수산화칼슘
NaOH = None
CaOH2 = None

#산성, 염기성 mL
acid_mL = None
basic_mL = None


#산성, 염기성 물질 입력
print("*현재 사용 가능: HCl, H2SO4, HNO3 / NaOH, CaOH2")
print('--------------------------------------------------')

acid = input("산성 물질을 입력하세요.\n: ")
time.sleep(0.5)
acid_mL = int(input("산성 물질의 양을 입력하세요. (mL)\n: "))
time.sleep(0.5)

basic = input("\n염기성 물질을 입력하세요.\n: ")
time.sleep(0.5)
basic_mL = int(input("염기성 물질의 양을 입력하세요. (mL)\n: "))
time.sleep(0.5)

print('--------------------------------------------------')


#분석
if acid == 'HCl':
    HCl = acid_mL
elif acid == 'H2SO4':
    H2SO4 = acid_mL
elif acid == 'HNO3':
    HNO3 = acid_mL

if basic == 'NaOH':
    NaOH = basic_mL
elif basic == 'CaOH2':
    CaOH2 = basic_mL


#화학식 출력
if HCl==NaOH:  #염산, 수산화나트륨
    print("HCl + NaOH -> H2O + NaCl")
    print("*1:1 반응")
    print("*중성")
elif HCl!=None and NaOH!=None and HCl > NaOH:
    print("HCl + NaOH -> H2O + NaCl")
    print("*1:1 반응")
    print(f"*반응 뒤 산성 물질이 {HCl-NaOH}개 남아 산성")
elif HCl!=None and NaOH!=None and HCl < NaOH:
    print("HCl + NaOH -> H2O + NaCl")
    print("*1:1 반응")
    print(f"*반응 뒤 염기성 물질이 {NaOH-HCl}개 남아 염기성")

elif HCl==2*CaOH2:   #염산, 수산화칼슘
    print("2HCl + CaOH2 -> CaCl2 + 2(H2O)")
    print("*2:1 반응")
    print("*중성")
elif HCl!=None and CaOH2!=None and HCl > CaOH2*2:
    print("2HCl + CaOH2 -> CaCl2 + 2(H2O)")
    print("*2:1 반응")
    print(f"*반응 뒤 산성 물질이 {HCl-2*CaOH2}개 남아 산성")
elif HCl!=None and CaOH2!=None and HCl < CaOH2*2:
    print("2HCl + CaOH2 -> CaCl2 + 2(H2O)")
    print("*2:1 반응")
    print(f"*반응 뒤 염기성 물질이 {int(CaOH2-0.5*HCl)}개 남아 염기성")

elif 2*H2SO4==NaOH:  #황산, 수산화나트륨
    print("H2SO4 + 2NaOH -> Na2SO4 + 2(H2O)")
    print("*1:2 반응")
    print("중성")
elif H2SO4!=None and NaOH!=None and H2SO4*2 > NaOH:
    print("H2SO4 + 2NaOH -> Na2SO4 + 2(H2O)")
    print("*1:2 반응")
    print(f"*반응 뒤 산성 물질이 {int(H2SO4-0.5*NaOH)}개 남아 산성")
elif H2SO4!=None and NaOH!=None and H2SO4*2 < NaOH:
    print("H2SO4 + 2NaOH -> Na2SO4 + 2(H2O)")
    print("*1:2 반응")
    print(f"*반응 뒤 염기성 물질이 {NaOH-2*H2SO4}개 남아 염기성")

elif H2SO4==CaOH2: #황산, 수산화칼슘
    print("H2SO4 + CaOH2 -> CaSO4 + 2(H2O)")
    print("*1:1 반응")
    print("중성")
elif H2SO4!=None and CaOH2!=None and H2SO4 > CaOH2:
    print("H2SO4 + CaOH2 -> CaSO4 + 2(H2O)")
    print("*1:1 반응")
    print(f"*반응 뒤 산성 물질이 {H2SO4-CaOH2}개 남아 산성")
elif H2SO4!=None and CaOH2!=None and H2SO4 < CaOH2:
    print("H2SO4 + CaOH2 -> CaSO4 + 2(H2O)")
    print("*1:1 반응")
    print(f"*반응 뒤 염기성 물질이 {CaOH2-H2SO4}개 남아 염기성")

elif HNO3==1:   #질산, 수산화나트륨
    print("HNO3 + NaOH -> NaNO3 + H2O")
    print("1:1 반응")
    print("중성")
elif HNO3!=None and NaOH!=None and HNO3 > NaOH:
    print("H2SO4 + CaOH2 -> CaSO4 + 2(H2O)")
    print("*1:1 반응")
    print(f"*반응 뒤 산성 물질이 {HNO3-NaOH}개 남아 산성")
elif HNO3!=None and NaOH!=None and HNO3 < NaOH:
    print("H2SO4 + CaOH2 -> CaSO4 + 2(H2O)")
    print("*1:1 반응")
    print(f"*반응 뒤 염기성 물질이 {NaOH-HNO3}개 남아 염기성")

elif HNO3==2*CaOH2:  #질산, 수산화칼슘
    print("2(HNO3) + CaOH2 -> Ca(NO3)2 + 2(H2O)")
    print("2:1 반응")
    print("*중성")
elif HNO3!=None and CaOH2!=None and HNO3 > CaOH2*2:
    print("2(HNO3) + CaOH2 -> Ca(NO3)2 + 2(H2O)")
    print("2:1 반응")
    print(f"*반응 뒤 산성 물질이 {HNO3-2*CaOH2}개 남아 산성")
elif HNO3!=None and CaOH2!=None and HNO3 < CaOH2*2:
    print("2(HNO3) + CaOH2 -> Ca(NO3)2 + 2(H2O)")
    print("2:1 반응")
    print(f"*반응 뒤 염기성 물질이 {int(CaOH2-0.5*HNO3)}개 남아 염기성")


#그래프
print("\n--------------------------------------------------")
graph = input('그래프 표시: ')
if graph == 'y':
    HCl = 3
    NaOH = 3
    H = HCl
    Cl = HCl
    Na = NaOH
    OH = NaOH

    plt.xlabel('count')
    plt.ylabel('number')
    plt.grid(True)
    plt.xlim([0, 5])
    plt.ylim([0, 5])

    plt.plot([0, 1, 2, 3, 4, 5], [H, H-1, H-2, H-3, 0, 0], label='H+')   #H+
    plt.plot([0, 1, 2, 3, 4, 5], [Cl, Cl, Cl, Cl, Cl, Cl], label='Cl-')   #Cl-
    plt.plot([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], label='Na+')    #Na+
    plt.plot([0, 1, 2, 3, 4, 5], [0, 0, 0, 0, 1, 2], label='OH-')    #OH-
    plt.plot([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 3, 3], label='H2O')    #H2O
    plt.legend(loc=(0.01, 0.7))

    plt.show()