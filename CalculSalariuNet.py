def calcul_salariu_net (salariu_brut):
    CAS = salariu_brut * 0.25
    CASS= salariu_brut * 0.10
    impozit_3 = (salariu_brut - CAS - CASS) * 0.10
    impozit_pe_venit = CAS + CASS + impozit_3
    salariu_net = salariu_brut - impozit_pe_venit
    return(salariu_net)

salariu_brut = int(input())
rezultat = calcul_salariu_net(salariu_brut)
print(rezultat)