def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res



def func(x):     
    res = 0
    for i in range(x):
        res += 1
    return res
    
print(func(3))


#შექმენი პროგრამა, რომელიც მიიღებს მომხმარებლის ასაკს და დააბრუნებს შეტყობინებას იმის მიხედვით, თუ რომელ ასაკობრივ კატეგორიაშია მომხმარებელი.


def age_category(age):
    if age < 0:
        return "ასაკი არასწორია."
    elif age <= 12:
        return "ბავშვი ხარ გაჩერდი"
    elif age <= 19:
        return "სკოლა დავასრულე ეეეეეეე"
    elif age <= 35:
        return "ახალგაზრდა"
    elif age <= 59:
        return "ზრდასრული ადამიანი ვარ პატივი მეცი"
    else:
        return "მოხუცი ვარ დამაჯინე თუ შეიძლება"









