POSITIEVE_RENTE = 1/10
NEGATIEVE_RENTE = 2/10
balans = 0
count = 1
rente_pos = 0
rente_neg = 0
rente = 0
inkomst = int(input())

while inkomst != 0:
    balans = balans + inkomst
    if count < 3:
        count += 1
    else:
        if balans < 0:
            rente = balans*NEGATIEVE_RENTE
            balans = balans + rente
            rente_neg = rente_neg + rente
            count = 1
        else:
            rente = balans*POSITIEVE_RENTE
            balans = balans + rente
            rente_pos = rente_pos + rente
            count = 1
    inkomst = int(input())

print(round(balans,2), round(rente_neg+rente_pos,2), round(rente_pos,2), round(rente_neg,2))
