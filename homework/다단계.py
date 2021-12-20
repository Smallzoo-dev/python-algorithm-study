def solution(enroll, referral, seller, amount):
    answer = []
    people_arr = []
    for i in range(len(enroll)):
        member = People(enroll[i])
        people_arr.append(member)

    for i in range(len(referral)):
        for j in people_arr:
            if j.name == referral[i]:
                people_arr[i].set_referrer(j)

    for i in range(len(seller)):
        idx = enroll.index(seller[i])
        people_arr[idx].earn_money(amount[i] * 100)

    for i in people_arr:
        answer.append(i.get_money())

    return answer


class People:
    def __init__(self, name):
        self.name = name
        self.referrer = None
        self.money = 0

    def set_referrer(self, referrer):
        if referrer == "-":
            return
        self.referrer = referrer

    def earn_money(self, money):
        if self.referrer:
            self.referrer.earn_money(money // 10)
        money -= money//10
        self.money += money

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))