
age = input("당신의 나이는 몇년생 입니까?(4자리로 입력해주세요.)")

if int(age) in [1948, 1960, 1972, 1984, 1996, 2008]:
    age = "쥐띠"

elif int(age) in [1949, 1961, 1973, 1985, 1997, 2009]:
    age = "소띠"

elif int(age) in [1950, 1962, 1974, 1986, 1998, 2010]:
    age = "호랑이띠"

elif int(age) in [1951, 1963, 1975, 1987, 1999, 2011]:
    age = "토끼띠"

elif int(age) in [1944, 1956, 1968, 1980, 1992, 2004]:
    age = "원숭이띠"

elif int(age) in [1947, 1959, 1971, 1983, 1995, 2007]:
        age = "돼지띠"

print("당신은 {0}입니다. {0}운세:link".format(age))