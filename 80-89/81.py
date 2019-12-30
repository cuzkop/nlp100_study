# 81. 複合語からなる国名への対処
# 英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

import sys

with open('tmp/countries.txt', mode='r') as country_file, open('tmp/80.txt', mode='r') as file_80, open('tmp/81.txt', 'w') as complexed_file:
    '''
    スペース区切り2文字以上の文字を抽出
    改行コード消してlistへ
    '''
    country_more_len_two = filter(lambda x: len(x.split()) >= 2, country_file)
    country_more_len_two_list = [c.strip() for c in country_more_len_two]

    cnt = 0
    for f in file_80:
        for country in country_more_len_two_list:
            if country in f:
                under_score_country = country.replace(' ', '_')
                f = f.replace(country, under_score_country)

        complexed_file.write(f)
