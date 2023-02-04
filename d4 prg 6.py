def check_vow(string, vowels):
    final=(each for each in string if each in vowels)
    print(len(final))
    print(final)
string=' geetha madhuri '
vowels=' AaEeIiOoUu '
check_vow(string, vowels);
