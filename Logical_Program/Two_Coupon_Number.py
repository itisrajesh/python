import random

class CouponNumber:
    @staticmethod
    def coupon_number():
        """
        Description : This method is used to generate distinct coupon number.
        Input: None
        Output: None
        """
        n = int(input("Enter the number of distinct coupon number: "))
        random_number = random.randint(1, n)
        count = 0
        distinct = []
        while True:
            count += 1
            if random_number not in distinct:
                distinct.append(random_number)
            if len(distinct) == n:
                break
            random_number = random.randint(1, n)
        print("Total random number needed to have all distinct numbers: ", count)


if __name__ == '__main__':
    CouponNumber.coupon_number()