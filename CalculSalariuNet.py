def calcul_salariu_net (salariu_brut):
    impozit_1 = salariu_brut * 0.25
    impozit_2 = impozit_1 * 0.10
    impozit_3 = impozit_2 * 0.10
    impozit_final = impozit_1 + impozit_2 + impozit_3
    salariu_net = salariu_brut - impozit_final
    return(salariu_net)

keyboard_input = input()
salariu_brut = int(keyboard_input)
rezultat = calcul_salariu_net(salariu_brut)
print(rezultat)