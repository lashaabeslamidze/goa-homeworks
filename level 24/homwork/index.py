# ააგეთ პროგრამა, რომელიც მოსთხოვს მომხმარებელს, რომ შეიყვანეს რიცხვი 1 - 100 მდე.
# პროგრამის დანიშნულება არის ის, რომგამოიცნოს მომხმარებლის მიერ შემოტანილი რიცხვი, იმდენჯერ მიეცეს გამოცნობის შესაძლებლობა სანამ საბოლოოდ არ გამოიცნობს


ricxvi1 = int(input("gtxov shemoitane ricxvi"))
ricxvi2 = 99.9

if ricxvi1 <= ricxvi2:
    print("arasworia")

else:
    print("sworia")

    



#'FizzBuzz' მიზანი
#შექმენით პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 100-მდე. თუმცა 3-ის ჯერადებისთვის რიცხვის ნაცვლად დაბეჭდეთ „Fizz“, ხოლო 5-ის ჯერადებისთვის დაბეჭდეთ „Buzz“. 3-ისა და 5-ის ჯერადი რიცხვებისთვის დაბეჭდეთ "FizzBuzz".  მოთხოვნები: გამოიყენეთ მარყუჟი 1-დან 100-მდე რიცხვების გასამეორებლად.
#გამოიყენეთ პირობითი განცხადებები, რათა შეამოწმოთ რიცხვი იყოფა 3-ზე, 5-ზე ან ორივეზე. დაბეჭდეთ შესაბამისი სიტყვა ("Fizz", "Buzz" ან "FizzBuzz") ან ნომერი


jeradi = 100
gamyofi = 1
for i in range(jeradi):
    if gamyofi % 15 == 0:
        print("FizzBuzz")
    elif gamyofi % 3 == 0:
        print("Fizz")
    elif gamyofi % 5 == 0:
        print("Buzz")
    else:
        print(gamyofi)
    gamyofi = gamyofi + 1







#დაწერეთ პროგრამა სადაც შეამოწმეთ, სტუდენტმა ჩააბარა თუ არა ჩააბარა კურსი მათი გამოცდის ქულების მიხედვით. სთხოვეთ მომხმარებელს შეიყვანოს ქულები შუალედური გამოცდისთვის, დასკვნითი გამოცდისთვის და პროექტისთვის. დარწმუნდით, რომ მომხმარებელმა შეიყვანოს სწორი ქულები (პოზიტიური რიცხვები 0-დან 100-მდე) თითოეული კომპონენტისთვის.
#გამოიყენეთ შემდეგი შეფასების კრიტერიუმები: თუ საშუალო ქულა (20% შუალედური კურსისთვის, 40% საბოლოო და 40% პროექტისთვის) არის 70 ან მეტი, სტუდენტი გაივლის კურსს. თუ საშუალო ქულა 70-ზე დაბალია, სტუდენტი ვერ ახერხებს კურსის ჩაბარებას. აჩვენეთ მომხმარებლისთვის შეტყობინება, რომელშიც მითითებულია მისი გავლის/ჩავარდნის სტატუსი და გამოთვლილი საშუალო ქულა.
 


sashualo_qula = int(input('chasvi sashualo qula: '))
saboloo_qula = int(input('chasvi saboloo qula: '))
proeqtis_qula = int(input('chasvi proeqtis qula: '))

print((sashualo_qula + saboloo_qula + proeqtis_qula) /3)

chaabare_an_ver_chaabare = (sashualo_qula + saboloo_qula + proeqtis_qula) /3

if chaabare_an_ver_chaabare >= 70:
    print("yochag tqven chaabared")
else:
    print("samwuxarod tqven ver chaabared")



# დაწერეთ პროგრამა სადაც შეამოწმებთ, აქვს თუ არა ადამიანს მართვის მოწმობის აღების უფლება მისი ასაკისა და მართვის გამოცდილებიდან გამომდინარე. დარწმუნდით, რომ მომხმარებელი შეიყვანს თავისი ასაკს და წლების რაოდენობა, რომელსაც მანქანას მართავდა.მომხმარებელმა უნდა შეიყვანოს დადებითი მთელი რიცხვები ასაკისა და მართვის გამოცდილებისთვის. (დაგნა მოხდეს ოპერაციები)
# გამოიყენეთ შემდეგი საკვალიფიკაციო კრიტერიუმები: პირი უნდა იყოს მინიმუმ 18 წლის მართვის მოწმობის მისაღებად. თუ პირი 18 წლამდეა, მას არ შეეძლება მართვის მოწმობის აღება. თუ პირი არის 18 წლის ან მეტი, მას უნდა ჰქონდეს მინიმუმ 1 წლიანი მართვის გამოცდილება, რომ დაშვებული იყოს მართვის მოწმობის აღებისთვის.
# მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია მართვის მოწმობის მიღების უფლება

weli = input("shemoitanet tqveni weli: ")
gamocdileba_martvis_mowmobashi = input("gamocdileba martvis mowmobashi")

if weli < 18:
        print("shen patara xar martvs mowmobistvis")
else:
    print("aiget tqveni martvis mowmoba")










